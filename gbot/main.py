# gianpiertoldium
# (c) Stockdroid Fans, 2021

'''
  App: Gianpiertolda
  Platform: PowerScript (python3 + JSON)
  Version: dwstr.__version__
  Developer: !stockdroidfans developer team
'''
'''
  File: main.py
  Applet: GianpiertoldaBot
  Platform: python3
  Version: dwstr.__version__
  Developer: !stockdroidfans developer team
'''

#———————————————————#———————————————————#———————————————————#———————————————————#———————————————————#

# Imports
""" Sistema """
import sys, os, time, json, html, random, logging, traceback

""" Telegramma """
import telegram, telegram.ext, telegram.utils, ptbstats

""" Moduli """
import main, crisiologie, sudo, pwsc, gbot

""" JSON """
with open("local.json") as l:
  local = json.load(l)
with open("log.json") as l:
  log = json.load(l)
with open("commands.json") as c:
  commands = json.load(c)
with open("settings.json") as s:
  settings = json.load(s)

# Shortcuts
""" Telegramma """
from telegram import (
  Update,
  constants,
  ChatPermissions,
  ParseMode,
  InlineKeyboardButton,
  InlineQueryResultArticle,
  InputTextMessageContent,
)
from telegram.ext import (
  Updater,
  CallbackContext,
  MessageHandler,
  Filters,
  PicklePersistence,
  Defaults,
)
from telegram.utils.helpers import mention_html, escape_markdown
from ptbstats import set_dispatcher, register_stats, SimpleStats, basestats

# Impostazione del bot(to)🧨
class Setup:
  defaults = Defaults(**settings["updater"][0]["defaults"])

  updater = Updater(
    token=settings["token"],
    defaults=defaults,
    use_context=settings["updater"][0]["use_context"],
  )
  set_dispatcher(updater.dispatcher)
  register_stats(SimpleStats("text", lambda u: bool(u.message and (Filters.all)(u))))

  logging.basicConfig(
    **settings["logging"]["basic_config"], level=eval(settings["logging"]["level"])
  )
  Logger = logging.getLogger(__name__)

CommandFiles = os.listdir("./Commands/")

class Handling:
  def UpdateHandler(update, context):
    if type(update) == int():
      UpdateId = int(update)
      update = log["updates"].keys()[
        list(log["updates"].values()).index(UpdateId)
      ]
    else:
      UpdateId = update.update_id

    try:
      UpdateDict = {"id": UpdateId, "update": update}
      a = log["updates"].append(dict(UpdateDict))
      # log.update(json.dumps(a))
      # update.effective_message.reply_text(UpdateDict['update'].to_dict())
      print(UpdateDict["id"])
      return UpdateDict
    except Exception as ex:
      raise type(ex)(
        f"Could not retrieve the update {UpdateId} [{type(update)}]: {type(ex)}: {ex}."
      )

  def ErrorHandler(update, context) -> None:
    Setup.Logger.error(
      msg="Exception while handling an update: ", exc_info=context.error
    )
    TracebackList = traceback.format_exception(
      None, context.error, context.error.__traceback__
    )
    TracebackString = ''.join(TracebackList)
    UpdateString = update.to_dict() if isinstance(update, Update) else str(update)

    if len(html.escape(TracebackString)) < 200:
      ErrorDump = html.escape(TracebackString)
    else:
      ErrorDump = strintable["misc"][0]["text_overflow"]

    context.bot.send_message(
      chat_id=local["special"]["chats"]["devs"],
      text='<b>{str(stringtable["updater"][0]["error"][0]).upper()}</b>\n{str(stringtable["updater"][0]["error"][1])}---BEGIN CONTEXT DATA---\n<b>update</b> = <code>{html.escape(json.dumps(UpdateString, indent=2, ensure_ascii=False))}</code>\n\n<b>context.user_data</b> = <code>{html.escape(str(context.user_data))}</code>\n\n<b>context.user_data</b> = <code>{html.escape(str(context.user_data))}</code>\n---BEGIN ERROR DUMP---\n<code>{ErrorDump}</code>',
    )

# DEF ECHAZIONE PROTONICA ._.
def echo(update, context):
  Update = Handling.UpdateHandler(update, context)

  EchoLocal = local["echo"] # vuoto atm, non utilizzato
  EchoSettings = settings["echo"]

  Chat = context.bot.get_chat(update.effective_chat.id)
  User = context.bot.get_chat(update.effective_user.id)
  ChatMember = context.bot.get_chat_member(update.effective_chat.id, update.effective_user.id)
  Sudo = sudo.sudo(ChatMember, context) # to check
  UserName = str(update.effective_user.name).lower()
  UserTitle = update.effective_user.full_name
  UserBio = str(User.bio).lower()
  MessageText = str(update.effective_message.text_html_urled).lower()
  print(MessageText)

  # Command handling
  rw = 0
  for s in list(settings["commands"]["prefix"]["requires_sudo"].keys()):
    if Sudo['sudo_lvl'] >= int(s):
      for p in settings["commands"]["prefix"]["requires_sudo"][s]:
        for c in CommandFiles:
          CommandName = str('.'.join(c.split('.')[:-1]))
          with open(f'Commands/{c}') as cc:
            Command = json.loads(cc.read())
            Function = Command['function']
          try:
            requires_prefix = Command["requires_prefix"]
          except:
            requires_prefix = True
          try:
            search_anywhere = Command["search_anywhere"]
          except:
            search_anywhere = False
          try:
            requires_sudo = Command["requires_sudo"]
          except:
            requires_sudo = 0
            
          if (
            MessageText.startswith(p) and MessageText.split(' ')[0] == str(p + CommandName)
            or
            requires_prefix == False and MessageText == CommandName
            or
            search_anywhere == True and CommandName in MessageText
          ):
            print(f"\nCommand detected. Parsing... [{Update['id']}]\n\nFile: {c} | Command: {str('.'.join(c.split('.')[:-1]))} | Prefix: {p}\n")
            if Sudo['sudo_lvl'] >= requires_sudo and rw <= 0:
              pwsc.parse(Function, update, context)
              rw = 1
            else:
              pass
  
  # Filtering
  rw = 0
  # tbd
  

updater = Setup.updater
dispatcher = Setup.updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.all, echo))
dispatcher.add_error_handler(Handling.ErrorHandler)

updater.start_polling()
updater.idle()

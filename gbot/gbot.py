import pwsc

def send(key, update, context):
  Types = {"text": "message", "message": "message", "photo": "photo", "video": "video", "gif": "animation", "animation": "animation", "album": "media_group", "media_group": "media_group", "sticker": "sticker", "audio": "audio", "music": "audio", "voice": "voice", "voice_note": "voice", "video_note": "video_note", "file": "document", "document": "document", "action": "chat_action", "chat_action": "chat_action", "contact": "contact", "dice": "dice", "game": "game", "payment": "invoice", "invoice": "invoice", "location": "location", "venue": "venue"}

  for t in list(Types.keys()):
    try:
      if key[t] != None:
        eval(f"update.effective_message.reply_{t}(**key)")
    except:
      pass

def reply(key, update, context):
  Types = {"text": "text", "message": "text", "photo": "photo", "video": "video", "gif": "animation", "animation": "animation", "album": "media_group", "media_group": "media_group", "sticker": "sticker", "audio": "audio", "music": "audio", "voice": "voice", "voice_note": "voice", "video_note": "video_note", "file": "document", "document": "document", "action": "chat_action", "chat_action": "chat_action", "contact": "contact", "dice": "dice", "game": "game", "payment": "invoice", "invoice": "invoice", "location": "location", "venue": "venue"}

  for t in list(Types.keys()):
    try:
      if key[t] != None:
        eval(f"update.effective_message.reply_{t}(**key)")
    except:
      pass

def delete(key, update, context):
  try:
    try:
      eval(f"context.bot.delete_message(**key)")
    except KeyError:
      raise TypeError(f'{key} does not contain a valid argument')
  except Exception as ex:
    raise type(ex)(f'An error has occurred during handling of the above callback function:\n{ex}')

def edit(key, update, context):
  try:
    try:
      eval(f"context.bot.edit_message_text(**key)")
    except KeyError:
      raise TypeError(f'{key} does not contain a valid argument')
  except Exception as ex:
    raise type(ex)(f'An error has occurred during handling of the above callback function:\n{ex}')

def pin(key, update, context):
  try:
    try:
      eval(f"context.bot.pin_chat_message(**key)")
    except KeyError:
      raise TypeError(f'{key} does not contain a valid argument')
  except Exception as ex:
    raise type(ex)(f'An error has occurred during handling of the above callback function:\n{ex}')

def unpin(key, update, context):
  try:
    try:
      eval(f"context.bot.unpin_chat_message(**key)")
    except KeyError:
      raise TypeError(f'{key} does not contain a valid argument')
  except Exception as ex:
    raise type(ex)(f'An error has occurred during handling of the above callback function:\n{ex}')

def kick(key, update, context):
  try:
    try:
      eval(f"context.bot.kick_chat_member(**key)")
      eval(f"context.bot.unban_chat_member(**key)")
    except KeyError:
      raise TypeError(f'{key} does not contain a valid argument')
  except Exception as ex:
    raise type(ex)(f'An error has occurred during handling of the above callback function:\n{ex}')

def addban(key, update, context):
  try:
    try:
      eval(f"context.bot.ban_chat_member(**key)")
    except KeyError:
      raise TypeError(f'{key} does not contain a valid argument')
  except Exception as ex:
    raise type(ex)(f'An error has occurred during handling of the above callback function:\n{ex}')

def delban(key, update, context):
  try:
    try:
      eval(f"context.bot.unban_chat_member(**key)")
    except KeyError:
      raise TypeError(f'{key} does not contain a valid argument')
  except Exception as ex:
    raise type(ex)(f'An error has occurred during handling of the above callback function:\n{ex}')

def addwarn(key, update, context):
  try:
    try:
      update.effective_message.reply_text('MONA! I warn funzionano solo se abbiamo un database e non abbiamo un database quindi siccome serve un database e non abbiamo un database ci serve un database grazie')
    except KeyError:
      raise TypeError(f'{key} does not contain a valid argument')
  except Exception as ex:
    raise type(ex)(f'An error has occurred during handling of the above callback function:\n{ex}')

def addrestriction(key, update, context):
  try:
    try:
      eval(f"context.bot.restrict_chat_member(**key)")
    except KeyError:
      raise TypeError(f'{key} does not contain a valid argument')
  except Exception as ex:
    raise type(ex)(f'An error has occurred during handling of the above callback function:\n{ex}')

def delrestriction(key, update, context):
  try:
    try:
      eval(f"context.bot.restrict_chat_member(**key)")
    except KeyError:
      raise TypeError(f'{key} does not contain a valid argument')
  except Exception as ex:
    raise type(ex)(f'An error has occurred during handling of the above callback function:\n{ex}')

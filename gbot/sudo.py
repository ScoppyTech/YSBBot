# gianpiertoldium
# (c) Stockdroid Fans, 2021

'''
  App: Gianpiertolda
  Platform: PowerScript (python3 + JSON)
  Version: dwstr.__version__
  Developer: !stockdroidfans developer team
'''
'''
  File: sudo.py
  Applet: GianpiertoldaBot Sudo
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

def UserLevel(user, context):
  if user.status == 'creator':
    return 3
  elif user.status == 'administrator':
    if user['can_promote_members'] == True:
      return 2
    elif user['can_promote_members'] == False:
      return 1
  elif user.is_anonymous == False:
    if user.custom_title == 'annuncio':
      return -1
    elif user.custom_title == 'gruppo':
      return -2
    else:
      return -3
  else:
    return 0

def sudo(user, context):
  owner = {'user': user.user.id, 'global': True, 'sudo_lvl': 3, 'gianfraschio': True, 'timebomb': False}
  admin = {'user': user.user.id, 'global': False, 'sudo_lvl': 2, 'gianfraschio': True, 'timebomb': False}
  mod = {'user': user.user.id, 'global': False, 'sudo_lvl': 1, 'gianfraschio': 'mod', 'timebomb': False}
  standard = {'user': user.user.id, 'global': False, 'sudo_lvl': 0, 'gianfraschio': False, 'timebomb': False}
  announcement = {'user': 'NaN', 'global': 'N/A', 'sudo_lvl': -1, 'gianfraschio': 'N/A', 'timebomb': False}
  group = {'user': 'NaN', 'global': 'N/A', 'sudo_lvl': -2, 'gianfraschio': 'N/A', 'timebomb': False}
  anon = {'user': 'NaN', 'global': 'N/A', 'sudo_lvl': -3, 'gianfraschio': 'N/A', 'timebomb': False}

  if UserLevel(user, context) == 3:
    return owner
  elif UserLevel(user, context) == 2:
    return admin 
  elif UserLevel(user, context) == 1:
    return mod
  elif UserLevel(user, context) == 0:
    '''for x in sudolist:
      if x['user'] == user_id:
        temp = {'user': user_id, 'global': False, 'sudo_lvl': 0, 'gianfraschio': 'temp', 'timebomb': int(x['time'] - time.time())}

        return temp
      else:
        return standard'''
    return standard
  elif UserLevel(user, context) == -1:
    return announcement
  elif UserLevel(user, context) == -2:
    return group
  elif UserLevel(user, context) == -3:
    return anon
  else:
    return standard

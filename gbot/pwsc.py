def callback(key, update, context):
  try:
    return eval(key)
  except Exception as ex:
    raise type(ex)(f'An error has occurred during handling of the above callback function:\n{ex}')

def evaluate(key, update, context):
  try:
    return eval(key)
  except Exception as ex:
    raise type(ex)(f'An error has occurred during evaluation of the specified value:\n{ex}')

from gbot import *

# Parser
def parse(key, update, context):
  for k in list(key.keys()):
    if key[k] == str():
      try:
        import re
        Objects = re.compile(r"/{.{0,}}/g")
        key[k] = re.sub(Objects, "update.update_id", key[k])
      except:
        pass
  return eval(f'{k}({key[k]}, update, context)')

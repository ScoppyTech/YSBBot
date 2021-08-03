import json, telegram, main
with open local as local:
  json.loads(local)
return {'gbot': local['__version__'], 'lib': telegram.__version__}

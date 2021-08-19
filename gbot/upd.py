import json, telegram, main
with open local as local:
  json.loads(local)

version = {'gbot': local['__version__'], 'lib': telegram.__version__}
print(version)
return version

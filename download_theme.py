import requests
import json

content = requests.get("https://bootswatch.com/api/3.json")
content = content.text
themes=json.loads(content)['themes']
for theme in themes:
    name = str(theme['name']).lower()
    print("""%s_theme = static('xadmin/css/themes/%s-theme.css')""" % (name, name))
for theme in themes:
    with open(theme['name']+'-theme.css', 'w') as f:
        content = requests.get(theme['cssCdn'])
        f.write(content.text)
    name = str(theme['name']).lower()
    print("""{'name': _(u"%s"), 'description': _(u"%s theme"), 'css': self.%s_theme},""" % (name, name, name))

import zlib
from itsdangerous import base64_decode

compressed = False
payload = ".eJw9jt0KgzAMhV9Fct0LhxejvsomktWsijUZaTsZ4ruvhbGrjxPOTw5wWZU4QQ8OdcOVwMBLYlwegaC_wUwq5fQUmQqcBNHKn3cwoIuf0-gk15LWQI6k44QJoT-gSbUjMoVQUraz10vXWduCKU5RZF_3duGJtNllQy7yLWGNO3qqov73KfSobsE7w3CWgAr7_-b5BR2QQMw.DtdKZQ.Vblje7sSvLXuLDNpu4D0XiHQxZ8"

if payload.startswith('.'):
    compressed = True
    payload = payload[1:]

data = payload.split(".")[0]

data = base64_decode(data)
if compressed:
    data = zlib.decompress(data)
print(data)

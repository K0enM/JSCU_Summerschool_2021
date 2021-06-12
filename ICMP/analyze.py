import json
import binascii
import base64

f = open('packets.json')

packets = json.load(f)

data = ''

for i in packets:
    data += i['_source']['layers']['icmp']['data']['data.data'].replace(':', '')

data = binascii.unhexlify(data)
data = base64.decodebytes(data)

with open('image.png', 'wb') as img:
    img.write(data);

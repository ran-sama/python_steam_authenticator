import hmac, time, base64, hashlib

code = ''
char = '23456789BCDFGHJKMNPQRTVWXY'

hex_time = ('%016x' % (time.time() // 30))
byte_time = hex_time.decode('hex')

digest = hmac.new(base64.b32decode('SHARED_SECRET_KEY'), byte_time, hashlib.sha1).digest()
begin = ord(digest[19:20]) & 0xF
c_int = int((digest[begin:begin + 4]).encode('hex'), 16) & 0x7fffffff

for r in range(5):
    code += char[c_int % len(char)]
    c_int /= len(char)
print code

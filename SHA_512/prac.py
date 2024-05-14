import hashlib

message = "abc"
hash_object = hashlib.sha512(message.encode())
hex_dig = hash_object.hexdigest()
print(hex_dig)


tmp = 'ami to tumi no connection.... sad :<('
byte_tmp = bytearray(tmp, encoding='utf-8')
print(byte_tmp)
print(type(byte_tmp))
a = bin(byte_tmp[0])[2:].zfill(8)
print(a)
print(int(a, 2))
print(type(a))

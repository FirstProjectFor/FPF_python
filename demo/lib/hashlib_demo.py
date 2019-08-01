import hashlib
import base64

print("可用的 签名算法: {}".format(hashlib.algorithms_guaranteed))

print('hashlib.md5(b\'name\').hexdigest(): \n{}'.format(hashlib.md5(b'name').hexdigest().upper()))
print('hashlib.sha1(b\'name\').hexdigest(): \n{}'.format(hashlib.sha1(b'name').hexdigest().upper()))
print('hashlib.sha512(b\'name\').hexdigest(): \n{}'.format(hashlib.sha512(b'name').hexdigest().upper()))

name = 'name'
print('base64.encodebytes(bname): {}'.format(base64.encodebytes(bytes(name, encoding='utf-8'))))
print('base64.b32encode(bname): {}'.format(base64.b32encode(bytes(name, encoding='utf-8'))))
print('base64.b85decode(bname): {}'.format(base64.b85decode(bytes(name, encoding='utf-8'))))

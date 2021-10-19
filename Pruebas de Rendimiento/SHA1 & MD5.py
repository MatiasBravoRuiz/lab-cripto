import hashlib
import time

start = time.time()

route = "C:/Users/Zenith/Downloads/wealabqlao/50.txt"
with open(route, mode='rb') as objeto_fichero:
    content = objeto_fichero.read()
    sha1_hash=hashlib.md5(content)
print(sha1_hash.hexdigest())

end =  time.time()

print(f"runtime {end-start}")

""" f = open("C:/Users/Zenith/Downloads/wealabqlao/50.txt", "r")
f1 = f.readlines()
for i in f1:
    result = hashlib.sha1(i.encode)
    print(result.hexdigest()) """
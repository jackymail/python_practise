
MEM_SERVER = '127.0.0.1'
MEM_PORT = '11211'
MEM_TIMEOUT = 30

import memcache,hashlib

mem = memcache.Client(['%s:%s' % (MEM_SERVER,MEM_PORT)])

def get_result(query):
    if query:
        hash = hashlib.md5(query).hexdigest()
        result = mem.get(hash)
        if result:
            return result
        else:
            return False

def set_result(query,result):
    # type: (object, object) -> object
    if query:
        hash = hashlib.md5(query).hexdigest()
        mem.set(hash,result,MEM_TIMEOUT)
import redis
class redisHelper():
    def __init__(self,host,port,passwd,db):
        self.__redis=redis.StrictRedis(host=host,port=port,password=passwd,db=db)
    def set(self,key,value):
        self.__redis.set(key,value)
    def get(self,key):
        return self.__redis.get(key)
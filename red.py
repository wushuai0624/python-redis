import redis

r = redis.StrictRedis(host='localhost',port=6379,password='123456',db='0') #建立连接
#写
pipe = r.pipeline()
pipe.set('py10','hello1')
pipe.set('py11','world')  #本地写
pipe.execute()      #提交到服务

#读
temp = r.get('py10')
print(temp)
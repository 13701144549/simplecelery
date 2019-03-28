import redis

class RedisHelper(object):
    def __init__(self,host,port,db,password):
        self.__con = redis.Redis(host=host,port=port,db=db,password=password)

    def publish(self,chanel,msg):
        '''
        发布
        :return:
        '''
        self.publish(chanel,msg)

    def subscribe(self,channel):
        '''
        订阅
        :return:
        '''
        pub = self.__con.pubsub()
        pub.subscribe(channel)
        pub.parse_response()
        return pub

    def Lpush(self,key,value):
        return self.__con.lpush(key,value)

    def Lpop(self,key):
        return self.__con.lpop(key)

    def Rpush(self,key,value):
        return self.__con.rpush(key,value)

    def Rpop(self,key):
        return self.__con.rpop(key)
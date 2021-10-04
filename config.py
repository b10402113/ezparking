import os
from datetime import timedelta

# 封裝配置類
class BaseConfig(object):
    # 數據庫部分s
    DEBUG = None
    SECRET_KEY = 'dsafkj2oijrmfclk13dmc'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:123123@localhost/ezparking'
    JWT_EXPIRE_TIME = 24
    # 動態追蹤修改，如果沒配置，只會提示警告消息
    # 如果True 會跟蹤數據庫信號變化，對性能有影響，
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_NAME = 'google-login-session'
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)



class DevelopmentConfig(BaseConfig):
    DEBUG = True
    pass

class ProductionConfig(BaseConfig):
    DEBUG = False
    pass

config_dict={
    'base_config': BaseConfig,
    'dev_config':DevelopmentConfig
}
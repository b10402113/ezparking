from flask import Flask
from authlib.integrations.flask_client import OAuth
import os
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(level=logging.INFO)

file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)

formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')

file_log_handler.setFormatter(formatter)

logging.getLogger().addHandler(file_log_handler)

logging.basicConfig(level=logging.INFO)

file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)

formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')

file_log_handler.setFormatter(formatter)

logging.getLogger().addHandler(file_log_handler)

# 定義工廠函數
def create_app(config_name=None):
    app = Flask(__name__)
    app.config.from_object(config_name)


    # 導入藍圖
    from .user import user_bp
    app.register_blueprint(user_bp)
    from .car import car_bp
    app.register_blueprint(car_bp)
    from .order import order_bp
    app.register_blueprint(order_bp)
    from models import db
    db.init_app(app)



    # 導入請求鉤子
    from lib.middleware import before_request
    # 相當於裝飾器調用
    app.before_request(before_request)

    return app



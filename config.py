import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql://root:password@localhost/ad_platform'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # 广告相关配置
    AD_TYPES = ['banner', 'popup', 'video', 'native']
    AD_STATUS = ['pending', 'approved', 'rejected', 'active', 'paused', 'completed']
    
    # 支付相关配置
    PAYMENT_METHODS = ['alipay', 'wechat', 'bank_transfer']
    PAYMENT_STATUS = ['pending', 'success', 'failed']
    
    # 发票相关配置
    INVOICE_TYPES = ['personal', 'company']
    INVOICE_STATUS = ['pending', 'issued', 'cancelled'] 
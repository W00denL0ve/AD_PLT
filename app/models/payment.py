from datetime import datetime
from app import db

class Payment(db.Model):
    __tablename__ = 'payments'
    
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    payment_method = db.Column(db.String(20))  # alipay, wechat, bank_transfer
    status = db.Column(db.String(20))  # pending, success, failed
    transaction_id = db.Column(db.String(64), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 外键
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def __repr__(self):
        return f'<Payment {self.id}>'

class Invoice(db.Model):
    __tablename__ = 'invoices'
    
    id = db.Column(db.Integer, primary_key=True)
    invoice_number = db.Column(db.String(32), unique=True)
    amount = db.Column(db.Float)
    invoice_type = db.Column(db.String(20))  # personal, company
    status = db.Column(db.String(20))  # pending, issued, cancelled
    tax_number = db.Column(db.String(32))
    company_name = db.Column(db.String(128))
    address = db.Column(db.String(256))
    phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 外键
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    payment_id = db.Column(db.Integer, db.ForeignKey('payments.id'))
    
    def __repr__(self):
        return f'<Invoice {self.invoice_number}>' 
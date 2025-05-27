from datetime import datetime
from app import db

class Advertisement(db.Model):
    __tablename__ = 'advertisements'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    description = db.Column(db.Text)
    ad_type = db.Column(db.String(20))  # banner, popup, video, native
    content_url = db.Column(db.String(256))
    target_url = db.Column(db.String(256))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    budget = db.Column(db.Float)
    status = db.Column(db.String(20))  # pending, approved, rejected, active, paused, completed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 外键
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    # 统计信息
    impressions = db.Column(db.Integer, default=0)
    clicks = db.Column(db.Integer, default=0)
    cost = db.Column(db.Float, default=0.0)
    
    def __repr__(self):
        return f'<Advertisement {self.title}>'

class AdImpression(db.Model):
    __tablename__ = 'ad_impressions'
    
    id = db.Column(db.Integer, primary_key=True)
    ad_id = db.Column(db.Integer, db.ForeignKey('advertisements.id'))
    ip_address = db.Column(db.String(45))
    user_agent = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<AdImpression {self.id}>'

class AdClick(db.Model):
    __tablename__ = 'ad_clicks'
    
    id = db.Column(db.Integer, primary_key=True)
    ad_id = db.Column(db.Integer, db.ForeignKey('advertisements.id'))
    impression_id = db.Column(db.Integer, db.ForeignKey('ad_impressions.id'))
    ip_address = db.Column(db.String(45))
    user_agent = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<AdClick {self.id}>' 
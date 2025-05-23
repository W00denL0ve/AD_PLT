from flask import Blueprint, jsonify, request
from app.models.advertisement import Advertisement, AdImpression, AdClick
from app import db
from datetime import datetime

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/ads')
def get_ads():
    ads = Advertisement.query.filter_by(status='active').all()
    return jsonify([{
        'id': ad.id,
        'title': ad.title,
        'ad_type': ad.ad_type,
        'content_url': ad.content_url,
        'target_url': ad.target_url
    } for ad in ads])

@bp.route('/ad/<int:id>/impression', methods=['POST'])
def record_impression(id):
    ad = Advertisement.query.get_or_404(id)
    
    impression = AdImpression(
        ad_id=ad.id,
        ip_address=request.remote_addr,
        user_agent=request.headers.get('User-Agent')
    )
    db.session.add(impression)
    
    ad.impressions += 1
    db.session.commit()
    
    return jsonify({'status': 'success'})

@bp.route('/ad/<int:id>/click', methods=['POST'])
def record_click(id):
    ad = Advertisement.query.get_or_404(id)
    impression_id = request.form.get('impression_id')
    
    click = AdClick(
        ad_id=ad.id,
        impression_id=impression_id,
        ip_address=request.remote_addr,
        user_agent=request.headers.get('User-Agent')
    )
    db.session.add(click)
    
    ad.clicks += 1
    db.session.commit()
    
    return jsonify({'status': 'success'})

@bp.route('/ad/<int:id>/stats')
def get_ad_stats(id):
    ad = Advertisement.query.get_or_404(id)
    return jsonify({
        'impressions': ad.impressions,
        'clicks': ad.clicks,
        'ctr': (ad.clicks / ad.impressions * 100) if ad.impressions > 0 else 0
    }) 
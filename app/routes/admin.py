from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models.advertisement import Advertisement
from app.models.payment import Payment, Invoice
from app.models.user import User
from app import db
from functools import wraps
from datetime import datetime

bp = Blueprint('admin', __name__, url_prefix='/admin')

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('需要管理员权限')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/')
@login_required
@admin_required
def index():
    pending_ads = Advertisement.query.filter_by(status='pending').count()
    users_count = User.query.count()
    pending_invoices = Invoice.query.filter_by(status='pending').count()
    today_income = Payment.query.filter(
        Payment.status == 'success',
        Payment.created_at >= datetime.utcnow().date()
    ).with_entities(db.func.sum(Payment.amount)).scalar() or 0
    
    recent_ads = Advertisement.query.order_by(Advertisement.created_at.desc()).limit(5).all()
    recent_payments = Payment.query.order_by(Payment.created_at.desc()).limit(5).all()
    
    return render_template('admin/index.html',
                         pending_ads_count=pending_ads,
                         users_count=users_count,
                         pending_invoices_count=pending_invoices,
                         today_income=today_income,
                         recent_ads=recent_ads,
                         recent_payments=recent_payments)

@bp.route('/ads')
@login_required
@admin_required
def ads():
    ads = Advertisement.query.order_by(Advertisement.created_at.desc()).all()
    return render_template('admin/ads.html', ads=ads)

@bp.route('/ad/<int:id>/review', methods=['POST'])
@login_required
@admin_required
def review_ad(id):
    ad = Advertisement.query.get_or_404(id)
    action = request.form.get('action')
    
    if action == 'approve':
        ad.status = 'active'
        flash('广告已审核通过')
    elif action == 'reject':
        ad.status = 'rejected'
        flash('广告已拒绝')
    
    db.session.commit()
    return redirect(url_for('admin.ads'))

@bp.route('/users')
@login_required
@admin_required
def users():
    users = User.query.all()
    return render_template('admin/users.html', users=users)

@bp.route('/payments')
@login_required
@admin_required
def payments():
    payments = Payment.query.all()
    return render_template('admin/payments.html', payments=payments)

@bp.route('/invoices')
@login_required
@admin_required
def invoices():
    invoices = Invoice.query.all()
    return render_template('admin/invoices.html', invoices=invoices)

@bp.route('/invoice/<int:id>/review', methods=['POST'])
@login_required
@admin_required
def review_invoice(id):
    invoice = Invoice.query.get_or_404(id)
    action = request.form.get('action')
    
    if action == 'approve':
        invoice.status = 'issued'
        flash('发票已开具')
    elif action == 'reject':
        invoice.status = 'cancelled'
        flash('发票申请已拒绝')
    
    db.session.commit()
    return redirect(url_for('admin.invoices')) 
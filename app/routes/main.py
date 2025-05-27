from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models.advertisement import Advertisement
from app.models.payment import Payment, Invoice
from app import db
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('main/index.html')

@bp.route('/dashboard')
@login_required
def dashboard():
    ads = Advertisement.query.filter_by(user_id=current_user.id).all()
    return render_template('main/dashboard.html', ads=ads)

@bp.route('/ad/create', methods=['GET', 'POST'])
@login_required
def create_ad():
    if request.method == 'POST':
        ad = Advertisement(
            title=request.form.get('title'),
            description=request.form.get('description'),
            ad_type=request.form.get('ad_type'),
            content_url=request.form.get('content_url'),
            target_url=request.form.get('target_url'),
            start_date=datetime.strptime(request.form.get('start_date'), '%Y-%m-%d'),
            end_date=datetime.strptime(request.form.get('end_date'), '%Y-%m-%d'),
            budget=float(request.form.get('budget')),
            status='pending',
            user_id=current_user.id
        )
        db.session.add(ad)
        db.session.commit()
        flash('广告创建成功，等待审核')
        return redirect(url_for('main.dashboard'))
    return render_template('main/create_ad.html')

@bp.route('/ad/<int:id>')
@login_required
def view_ad(id):
    ad = Advertisement.query.get_or_404(id)
    if ad.user_id != current_user.id and not current_user.is_admin:
        flash('无权访问此广告')
        return redirect(url_for('main.dashboard'))
    return render_template('main/view_ad.html', ad=ad)

@bp.route('/payment/create', methods=['GET', 'POST'])
@login_required
def create_payment():
    if request.method == 'POST':
        amount = float(request.form.get('amount'))
        payment_method = request.form.get('payment_method')
        
        payment = Payment(
            amount=amount,
            payment_method=payment_method,
            status='pending',
            transaction_id=f'TRX{datetime.utcnow().strftime("%Y%m%d%H%M%S")}',
            user_id=current_user.id
        )
        db.session.add(payment)
        db.session.commit()
        
        # 模拟支付过程
        payment.status = 'success'
        current_user.balance += amount
        db.session.commit()
        
        flash('充值成功')
        return redirect(url_for('main.payment_history'))
    return render_template('main/create_payment.html')

@bp.route('/payment/history')
@login_required
def payment_history():
    payments = Payment.query.filter_by(user_id=current_user.id).order_by(Payment.created_at.desc()).all()
    return render_template('main/payment_history.html', payments=payments)

@bp.route('/invoice/create/<int:payment_id>', methods=['GET', 'POST'])
@login_required
def create_invoice(payment_id):
    payment = Payment.query.get_or_404(payment_id)
    if payment.user_id != current_user.id:
        flash('无权访问此支付记录')
        return redirect(url_for('main.payment_history'))
    
    if request.method == 'POST':
        invoice = Invoice(
            invoice_number=f'INV{datetime.utcnow().strftime("%Y%m%d%H%M%S")}',
            amount=payment.amount,
            invoice_type=request.form.get('invoice_type'),
            status='pending',
            tax_number=request.form.get('tax_number'),
            company_name=request.form.get('company_name'),
            address=request.form.get('address'),
            phone=request.form.get('phone'),
            user_id=current_user.id,
            payment_id=payment.id
        )
        db.session.add(invoice)
        db.session.commit()
        
        flash('发票申请已提交')
        return redirect(url_for('main.invoice_history'))
    return render_template('main/create_invoice.html', payment=payment)

@bp.route('/invoice/history')
@login_required
def invoice_history():
    invoices = Invoice.query.filter_by(user_id=current_user.id).order_by(Invoice.created_at.desc()).all()
    return render_template('main/invoice_history.html', invoices=invoices)

@bp.route('/invoice/<int:id>/preview')
@login_required
def invoice_preview(id):
    invoice = Invoice.query.get_or_404(id)
    if invoice.user_id != current_user.id and not current_user.is_admin:
        flash('无权访问此发票')
        return redirect(url_for('main.invoice_history'))
    return render_template('main/invoice_preview.html', invoice=invoice)

@bp.route('/purchased-ads')
@login_required
def purchased_ads():
    # 获取当前用户的所有广告
    ads = Advertisement.query.filter_by(user_id=current_user.id).order_by(Advertisement.created_at.desc()).all()
    return render_template('main/purchased_ads.html', ads=ads)

@bp.route('/ad/<int:id>/stats')
@login_required
def ad_stats(id):
    ad = Advertisement.query.get_or_404(id)
    if ad.user_id != current_user.id and not current_user.is_admin:
        flash('无权访问此广告')
        return redirect(url_for('main.purchased_ads'))
    
    # 模拟统计数据
    stats = {
        'impressions': 1000,
        'clicks': 50,
        'ctr': 5.0,
        'spent': 500.00
    }
    
    # 模拟每日数据
    daily_stats = [
        {
            'date': '2024-01-01',
            'impressions': 100,
            'clicks': 5,
            'ctr': 5.0,
            'spent': 50.00
        },
        {
            'date': '2024-01-02',
            'impressions': 150,
            'clicks': 8,
            'ctr': 5.3,
            'spent': 75.00
        }
    ]
    
    # 图表数据
    dates = [record['date'] for record in daily_stats]
    impressions = [record['impressions'] for record in daily_stats]
    clicks = [record['clicks'] for record in daily_stats]
    
    return render_template('main/ad_stats.html', 
                         ad=ad, 
                         stats=stats, 
                         daily_stats=daily_stats,
                         dates=dates,
                         impressions=impressions,
                         clicks=clicks)

@bp.route('/api-docs')
def api_docs():
    return render_template('main/api_docs.html')

@bp.route('/ad/<int:id>/withdraw', methods=['POST'])
@login_required
def withdraw_ad(id):
    ad = Advertisement.query.get_or_404(id)
    if ad.user_id != current_user.id:
        flash('无权操作此广告')
        return redirect(url_for('main.purchased_ads'))
    
    if ad.status != 'pending':
        flash('只能撤回待审核的广告')
        return redirect(url_for('main.purchased_ads'))
    
    db.session.delete(ad)
    db.session.commit()
    flash('广告已成功撤回')
    return redirect(url_for('main.purchased_ads')) 
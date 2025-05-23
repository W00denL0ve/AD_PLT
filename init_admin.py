from app import create_app, db
from app.models.user import User

def init_admin():
    app = create_app()
    with app.app_context():
        # 检查是否已存在管理员账号
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            admin = User(
                username='admin',
                email='admin@example.com',
                company_name='系统管理',
                phone='13800000000',
                is_admin=True
            )
            admin.password = 'admin123'  # 设置初始密码
            db.session.add(admin)
            db.session.commit()
            print('管理员账号创建成功！')
            print('用户名: admin')
            print('密码: admin123')
        else:
            print('管理员账号已存在')

if __name__ == '__main__':
    init_admin() 
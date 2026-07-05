from app import app, db
from models import User
from werkzeug.security import generate_password_hash

def create_admin():
    with app.app_context():
        existing = User.query.filter_by(username='admin').first()
        if existing:
            print("Usuário admin já existe. Atualizando senha...")
            existing.password = generate_password_hash('123456')
            db.session.commit()
            print("Senha do admin atualizada para 123456")
        else:
            admin = User(username='admin', password=generate_password_hash('123456'))
            db.session.add(admin)
            db.session.commit()
            print("Usuário admin criado com sucesso!")

if __name__ == "__main__":
    create_admin()
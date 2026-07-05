import os
import shutil
from app import app, db


def reset_database():
    db_paths = [
        'guapimirim.db',
        'instance/guapimirim.db',
        os.path.join(app.instance_path, 'guapimirim.db')
    ]

    print("=" * 50)
    print("Resetando banco de dados...")
    print("=" * 50)

    for db_path in db_paths:
        if os.path.exists(db_path):
            try:
                os.remove(db_path)
                print(f"Arquivo removido: {db_path}")
            except Exception as e:
                print(f"Erro ao remover {db_path}: {e}")

    if os.path.exists('__pycache__'):
        shutil.rmtree('__pycache__')
        print("Pasta __pycache__ removida")

    if os.path.exists('instance/__pycache__'):
        shutil.rmtree('instance/__pycache__')
        print("Pasta instance/__pycache__ removida")

    print("\n" + "=" * 50)
    print("Criando novo banco de dados...")
    print("=" * 50)

    with app.app_context():
        db.create_all()
        print("Tabelas criadas com sucesso!")

        from sqlalchemy import inspect
        inspector = inspect(db.engine)
        columns = [col['name'] for col in inspector.get_columns('point')]
        print(f"Colunas criadas: {len(columns)}")

    print("\n" + "=" * 50)
    print("Banco de dados resetado com sucesso!")
    print("=" * 50)


if __name__ == "__main__":
    reset_database()
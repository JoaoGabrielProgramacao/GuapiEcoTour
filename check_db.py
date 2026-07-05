import os
from app import app, db
from sqlalchemy import inspect


def check_database():
    print("=" * 60)
    print("DIAGNÓSTICO DO BANCO DE DADOS")
    print("=" * 60)

    print("\n1. Configuração do banco:")
    print(f"   URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
    print(f"   Instance path: {app.instance_path}")

    print("\n2. Arquivos encontrados:")
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.db'):
                print(f"   - {os.path.join(root, file)}")

    print("\n3. Estrutura do banco de dados:")
    with app.app_context():
        try:
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            print(f"   Tabelas encontradas: {tables}")

            if 'point' in tables:
                columns = inspector.get_columns('point')
                print(f"\n   Colunas da tabela 'point':")
                for col in columns:
                    print(f"   - {col['name']}: {col['type']}")
            else:
                print("   Tabela 'point' não encontrada!")

        except Exception as e:
            print(f"   Erro ao inspecionar banco: {e}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    check_database()
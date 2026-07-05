from app import app, db
from sqlalchemy import text


def migrate():
    with app.app_context():
        conn = db.engine.connect()

        columns = [
            ('hours_en', 'VARCHAR(100)'),
            ('trail_diff_en', 'VARCHAR(50)'),
            ('best_season_en', 'VARCHAR(100)')
        ]

        print("Adicionando colunas de tradução...")
        for col_name, col_type in columns:
            try:
                conn.execute(text(f"ALTER TABLE point ADD COLUMN {col_name} {col_type}"))
                print(f"✓ Coluna {col_name} adicionada")
            except Exception as e:
                print(f"⊘ Coluna {col_name} já existe ou erro: {e}")

        conn.commit()
        conn.close()
        print("Migração concluída!")


if __name__ == "__main__":
    migrate()
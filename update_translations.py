from app import app, db
from models import Point

def update_translations():
    with app.app_context():
        pontos = Point.query.all()
        count = 0

        for p in pontos:
            atualizado = False

            # Tradução do horário
            if p.hours and not p.hours_en:
                if "08:00 - 17:00 (fecha às terças-feiras)" in p.hours:
                    p.hours_en = "08:00 - 17:00 (closed on Tuesdays)"
                    atualizado = True
                elif "08:00 - 18:00 (todos os dias)" in p.hours:
                    p.hours_en = "08:00 - 18:00 (every day)"
                    atualizado = True
                elif "24 horas (acesso livre)" in p.hours:
                    p.hours_en = "24 hours (free access)"
                    atualizado = True

            # Tradução da dificuldade
            if p.trail_diff and not p.trail_diff_en:
                if p.trail_diff == "Difícil":
                    p.trail_diff_en = "Hard"
                    atualizado = True
                elif p.trail_diff == "Fácil":
                    p.trail_diff_en = "Easy"
                    atualizado = True
                elif p.trail_diff == "Moderada":
                    p.trail_diff_en = "Moderate"
                    atualizado = True

            # Tradução da melhor época
            if p.best_season and not p.best_season_en:
                if "Abril" in p.best_season and "Setembro" in p.best_season:
                    p.best_season_en = "April to September (less rain, better visibility)"
                    atualizado = True
                elif "Ano todo" in p.best_season:
                    p.best_season_en = "All year round (fuller in summer)"
                    atualizado = True
                elif "Maio" in p.best_season and "Agosto" in p.best_season:
                    p.best_season_en = "May to August (clearest days)"
                    atualizado = True

            if atualizado:
                count += 1

        db.session.commit()
        print(f"✅ Campos em inglês atualizados para {count} ponto(s).")

        # Exibe os dados atualizados para conferência
        print("\n📋 Conferência dos dados atualizados:")
        for p in Point.query.all():
            print(f"\n📍 {p.name_pt}")
            print(f"   hours_en: {p.hours_en}")
            print(f"   trail_diff_en: {p.trail_diff_en}")
            print(f"   best_season_en: {p.best_season_en}")

if __name__ == "__main__":
    update_translations()
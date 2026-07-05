from app import app, db
from models import Point

def seed():
    with app.app_context():
        if Point.query.count() > 0:
            print("Pontos já cadastrados.")
            return

        pontos = [
            Point(
                name_pt="Parque Estadual dos Três Picos",
                name_en="Three Peaks State Park",
                lat=-22.4169,
                lng=-42.6092,
                summary_pt="Parque com trilhas desafiadoras e cachoeiras exuberantes",
                summary_en="Park with challenging trails and exuberant waterfalls",
                description_pt="O Parque Estadual dos Três Picos é uma das unidades de conservação mais importantes do estado do Rio de Janeiro. Com mais de 46 mil hectares, abriga o ponto mais alto da região serrana e oferece trilhas para todos os níveis de experiência.",
                description_en="Three Peaks State Park is one of the most important conservation units in Rio de Janeiro state. With over 46 thousand hectares, it houses the highest point in the mountain region and offers trails for all experience levels.",
                hours_pt="08:00 - 17:00 (fecha às terças-feiras)",
                hours_en="08:00 - 17:00 (closed on Tuesdays)",
                trail_diff_pt="Difícil",
                trail_diff_en="Hard",
                best_season_pt="Abril a Setembro (menos chuvas, melhor visibilidade)",
                best_season_en="April to September (less rain, better visibility)",
                history_pt="Criado em 2002, o parque tem como objetivo proteger os remanescentes de Mata Atlântica e as nascentes que abastecem a região. O nome faz referência aos três picos que formam a paisagem mais icônica da serra.",
                history_en="Created in 2002, the park aims to protect the Atlantic Forest remnants and the springs that supply the region. The name refers to the three peaks that form the most iconic landscape of the mountain range.",
                access_difficulty_pt="Médio",
                access_difficulty_en="Intermediate",
                location_details_pt="Entrada principal no km 42 da BR-116, Guapimirim. Acesso por estrada de terra nos últimos 5 km.",
                location_details_en="Main entrance at km 42 of BR-116, Guapimirim. Access via dirt road for the last 5 km.",
                environmental_tips_pt="Leve apenas água e lanches leves, não deixe lixo na trilha, mantenha-se nas trilhas demarcadas, leve repelente natural, respeite a fauna e flora local.",
                environmental_tips_en="Take only water and light snacks, don't leave trash on the trail, stay on marked trails, bring natural repellent, respect local fauna and flora.",
                contact_phone="(21) 2632-3029",
                contact_email="parque.trespicos@inea.rj.gov.br",
                image_url="/static/images/tres_picos.jpg",
                trail_time_min=90
            ),
            Point(
                name_pt="Cachoeira do Véu de Noiva",
                name_en="Bridal Veil Waterfall",
                lat=-22.5605,
                lng=-43.1175,
                summary_pt="Cachoeira famosa com fácil acesso e mirante",
                summary_en="Famous waterfall with easy access and viewpoint",
                description_pt="Com aproximadamente 30 metros de altura, a Cachoeira do Véu de Noiva é um dos cartões-postais de Guapimirim. Possui estrutura com quiosques, estacionamento e área para piquenique.",
                description_en="With approximately 30 meters high, Bridal Veil Waterfall is one of Guapimirim's postcards. It has infrastructure with kiosks, parking and picnic area.",
                hours_pt="08:00 - 18:00 (todos os dias)",
                hours_en="08:00 - 18:00 (every day)",
                trail_diff_pt="Fácil",
                trail_diff_en="Easy",
                best_season_pt="Ano todo (mais cheia no verão)",
                best_season_en="All year round (fuller in summer)",
                history_pt="A cachoeira recebeu este nome devido à sua forma que lembra um véu de noiva. É um dos pontos mais antigos de visitação da região, sendo frequentada por turistas desde a década de 1970.",
                history_en="The waterfall received this name because its shape resembles a bridal veil. It is one of the oldest tourist spots in the region, frequented by tourists since the 1970s.",
                access_difficulty_pt="Fácil",
                access_difficulty_en="Easy",
                location_details_pt="Estrada do Véu de Noiva, s/n - Guapimirim. Estacionamento gratuito no local.",
                location_details_en="Veil de Noiva Road, s/n - Guapimirim. Free parking on site.",
                environmental_tips_pt="Não use protetor solar antes de entrar na água, preserve a vegetação nativa, não alimente os animais silvestres, recolha seu lixo.",
                environmental_tips_en="Don't use sunscreen before entering the water, preserve native vegetation, don't feed wild animals, collect your trash.",
                contact_phone="(21) 2632-1458",
                contact_email="cachoeira.veunoiva@guapimirim.rj.gov.br",
                image_url="/static/images/veu_noiva.jpg",
                trail_time_min=30
            ),
            Point(
                name_pt="Mirante do Soberbo",
                name_en="Soberbo Viewpoint",
                lat=-22.462748,
                lng=-42.986924,
                summary_pt="Vista panorâmica impressionante da Baía de Guanabara",
                summary_en="Impressive panoramic view of Guanabara Bay",
                description_pt="Localizado na Serra do Mar, o Mirante do Soberbo oferece uma das vistas mais espetaculares do Rio de Janeiro. Em dias claros, é possível ver toda a Baía de Guanabara e o Pão de Açúcar.",
                description_en="Located in Serra do Mar, Soberbo Viewpoint offers one of the most spectacular views of Rio de Janeiro. On clear days, you can see all of Guanabara Bay and Sugarloaf Mountain.",
                hours_pt="24 horas (acesso livre)",
                hours_en="24 hours (free access)",
                trail_diff_pt="Fácil",
                trail_diff_en="Easy",
                best_season_pt="Maio a Agosto (dias mais claros)",
                best_season_en="May to August (clearest days)",
                history_pt="O mirante é um ponto tradicional de parada para quem sobe a serra. Foi inaugurado na década de 1950 e desde então é um dos locais mais fotografados da região.",
                history_en="The viewpoint is a traditional stop for those going up the mountain range. It was inaugurated in the 1950s and has since been one of the most photographed spots in the region.",
                access_difficulty_pt="Fácil",
                access_difficulty_en="Easy",
                location_details_pt="BR-116, km 88 - Guapimirim. Acesso direto pela estrada.",
                location_details_en="BR-116, km 88 - Guapimirim. Direct access from the road.",
                environmental_tips_pt="Não estacione em locais proibidos, respeite a sinalização, não deixe lixo, cuidado ao atravessar a estrada.",
                environmental_tips_en="Don't park in prohibited areas, respect signage, don't leave trash, be careful when crossing the road.",
                contact_phone="(21) 2632-1000",
                image_url="/static/images/soberbo.jpg",
                trail_time_min=15
            )
        ]

        db.session.add_all(pontos)
        db.session.commit()
        print(f"Seed concluído — pontos adicionados: {len(pontos)}")

if __name__ == "__main__":
    seed()
from flask import Flask, render_template, session, redirect, url_for, request, jsonify, flash
from models import db, Point, User, Favorite
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from dotenv import load_dotenv
import os
import requests

load_dotenv()

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=template_dir)
app.secret_key = os.urandom(24)

if 'RENDER' in os.environ:
    db_path = os.path.join('/tmp', 'guapimirim.db')
else:
    db_path = 'guapimirim.db'

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor, faça login para acessar esta página.'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/proxy-route", methods=['POST'])
def proxy_route():
    # A chave agora vem do .env, não do frontend
    api_key = os.getenv('ORS_API_KEY')

    data = request.get_json()
    start = data.get('start')
    end = data.get('end')

    if not api_key:
        return jsonify({'error': 'Chave da API não configurada no servidor.'}), 500

    if not start or not end:
        return jsonify({'error': 'Parâmetros obrigatórios: start, end'}), 400

    payload = {
        "coordinates": [start, end],
        "format": "geojson",
        "radiuses": [5000, 5000],
        "geometry": True
    }

    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(
            'https://api.openrouteservice.org/v2/directions/driving-car/geojson',
            json=payload,
            headers=headers
        )
        return jsonify(response.json()), response.status_code
    except Exception as e:
        print(f"[PROXY] Erro: {e}")
        return jsonify({'error': 'Erro ao conectar ao ORS'}), 500


@app.route("/clima")
def clima():
    lang = request.args.get('lang', 'pt')
    wttr_lang = 'pt' if lang == 'pt' else 'en'
    try:
        response = requests.get(f'https://wttr.in/Guapimirim?format=%C+%t+%w+%h&lang={wttr_lang}')
        clima_text = response.text.strip()
        return jsonify({'clima': clima_text})
    except:
        msg = 'Não disponível' if lang == 'pt' else 'Not available'
        return jsonify({'clima': msg})


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('home'))
        else:
            flash('Usuário ou senha inválidos', 'danger')
    return render_template('login.html')


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/")
@login_required
def home():
    points = Point.query.limit(6).all()
    return render_template('home.html', points=points)


@app.route("/mapa")
@login_required
def map():
    points = Point.query.all()
    points_serialized = [{
        'id': p.id,
        'name_pt': p.name_pt,
        'name_en': p.name_en,
        'lat': p.lat,
        'lng': p.lng,
        'summary_pt': p.summary_pt,
        'summary_en': p.summary_en,
        'trail_diff_pt': p.trail_diff_pt,
        'trail_diff_en': p.trail_diff_en,
        'image_url': p.image_url
    } for p in points]
    return render_template('map.html', points=points_serialized)


@app.route("/pontos")
@login_required
def points_list():
    points = Point.query.all()
    return render_template('points.html', points=points)


@app.route("/ponto/<int:point_id>")
@login_required
def point_detail(point_id):
    point = Point.query.get_or_404(point_id)
    return render_template('point_detail.html', point=point)


@app.route("/dicas-ambientais")
@login_required
def environmental_tips():
    return render_template('environmental_tips.html')


@app.route("/change-language/<lang>")
@login_required
def change_language(lang):
    if lang in ['pt', 'en']:
        session['lang'] = lang
    return redirect(request.referrer or url_for('home'))


@app.route("/api/points")
@login_required
def api_points():
    points = Point.query.all()
    return jsonify([{
        'id': p.id,
        'name_pt': p.name_pt,
        'name_en': p.name_en,
        'lat': p.lat,
        'lng': p.lng,
        'summary_pt': p.summary_pt,
        'summary_en': p.summary_en,
        'trail_diff_pt': p.trail_diff_pt,
        'trail_diff_en': p.trail_diff_en,
        'image_url': p.image_url
    } for p in points])


@app.route("/favorite/<int:point_id>", methods=['POST'])
@login_required
def toggle_favorite(point_id):
    fav = Favorite.query.filter_by(user_id=current_user.id, point_id=point_id).first()
    if fav:
        db.session.delete(fav)
        db.session.commit()
        return jsonify({'favorited': False})
    else:
        new_fav = Favorite(user_id=current_user.id, point_id=point_id)
        db.session.add(new_fav)
        db.session.commit()
        return jsonify({'favorited': True})


@app.route("/meus-favoritos")
@login_required
def my_favorites():
    points = [fav.point for fav in current_user.favorites]
    return render_template('points.html', points=points, favorites_page=True)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
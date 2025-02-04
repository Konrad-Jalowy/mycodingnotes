from flask import Flask, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
import hashlib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shortener.db'
db = SQLAlchemy(app)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)
    visits = db.Column(db.Integer, default=0)


with app.app_context():
    db.create_all()

def generate_short_code(url):
    return hashlib.md5(url.encode()).hexdigest()[:6]

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.json
    original_url = data.get('url')
    if not original_url:
        return jsonify({'error': 'No URL provided'}), 400

    existing_url = URL.query.filter_by(original_url=original_url).first()
    if existing_url:
        return jsonify({'short_url': request.host_url + existing_url.short_code})

    short_code = generate_short_code(original_url)
    new_url = URL(original_url=original_url, short_code=short_code)
    db.session.add(new_url)
    db.session.commit()

    return jsonify({'short_url': request.host_url + short_code})

@app.route('/<short_code>', methods=['GET'])
def redirect_to_original(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first()
    if url_entry:
        url_entry.visits += 1
        db.session.commit()
        return redirect(url_entry.original_url)
    return jsonify({'error': 'URL not found'}), 404

@app.route('/stats/<short_code>', methods=['GET'])
def get_url_stats(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first()
    if url_entry:
        return jsonify({'original_url': url_entry.original_url, 'visits': url_entry.visits})
    return jsonify({'error': 'URL not found'}), 404

if __name__ == '__main__':

    app.run(debug=True)

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sana_ozel_anahtar!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    
    return render_template('index.html')

@socketio.on('gonderilen_mesaj')
def handle_message(data):
    kullanici = (data.get('kullanici') or 'Anonim').strip() or 'Anonim'
    mesaj = (data.get('mesaj') or '').strip()
    zaman = datetime.now().isoformat(timespec='seconds')
    print(f"Alınan Mesaj: {kullanici}: {mesaj}")

    emit('yeni_mesaj', { 'kullanici': kullanici, 'mesaj': mesaj, 'zaman': zaman }, broadcast=True)

@app.route('/test')
def test_page():
    return render_template('test.html')

if __name__ == '__main__':
    
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)

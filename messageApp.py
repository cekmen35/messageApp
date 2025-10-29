from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sana_ozel_anahtar!'
socketio = SocketIO(app)

@app.route('/')
def index():
    # Bu, istemci arayüzümüzün olduğu HTML dosyasını çağırır.
    return render_template('index.html')

@socketio.on('gonderilen_mesaj')
def handle_message(data):
    print(f"Alınan Mesaj: {data['kullanici']}: {data['mesaj']}")
    # Tüm bağlı istemcilere mesajı yayınlar
    emit('yeni_mesaj', data, broadcast=True)

if __name__ == '__main__':
    # Uygulamayı başlat
    socketio.run(app, debug=True)
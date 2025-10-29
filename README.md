# Mesajlaşma Uygulaması

Gerçek zamanlı sohbet (Flask + Flask-SocketIO + Eventlet).

## Kurulum

```bash
python -m venv venv
# PowerShell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Çalıştırma

```bash
python app.py
```

- Uygulama: http://localhost:5000
- Test (iki istemci): http://localhost:5000/test

## Özellikler
- Kullanıcı adı (header alanı veya `?u=` parametresi)
- Zaman damgalı mesajlar
- Gerçek zamanlı yayın

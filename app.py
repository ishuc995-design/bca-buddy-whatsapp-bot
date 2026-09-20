from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# WhatsApp Token (Demo ke liye khali rakha hai)
WHATSAPP_TOKEN = "YOUR_TOKEN"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print(data)
    return "ok", 200

if __name__ == '__main__':
    app.run(debug=True)
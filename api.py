from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json
import requests

app = Flask(__name__)
CORS(app)


@app.route('/chat',  methods=['POST'])
def chat():
    data = request.get_json()
    sender = data['sender']
    message = data['message']
    api_url = 'http://localhost:5005/webhooks/rest/webhook'
    create_row_data = {'sender': sender,'message': message}
    print(create_row_data)
    r = requests.post(url=api_url, json=create_row_data)
    # print(r.status_code, r.reason, r.text)
    response_list = list(eval(r.text))
    response = response_list[0]['text'] 
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6666, debug=True, use_reloader=False)

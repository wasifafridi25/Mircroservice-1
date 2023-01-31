from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/zipcode', methods=['GET'])
def get_zipcode():
    state = request.args.get('state')
    city = request.args.get('city')
    url = f"https://www.zipwise.com/webservices/citysearch.php?key=jb49u2fszhvghy74&format=json&string={city}&state={state}"
    #url = f"https://www.zipwise.com/webservices/citysearch.php?key=jb49u2fszhvghy74&format=json&string={city}"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)
    
if __name__ == '__main__':
    app.run(debug=True, port=8000)

#address    
#http://127.0.0.1:8000/zipcode?city=Sunnyvale&state=CA    





    

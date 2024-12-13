import json

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def mitarbeiter():
    return json.dumps({"name": "John",
                       "alter": 45,
                       "gehalt": 4500,
                       "abteilung": "IT"})

## curl -X POST http://127.0.0.1:5000/user -H 'Content-Type: application/json' -d '{"login":"my_login","password":"my_password"}'
@app.route("/user", methods=['POST'])
def user():
    content_type = request.headers.get('Content-Type')
    print(content_type)
    with open('json_file.json', 'a') as file:
        json.dump(request.json, file)
    return jsonify(request.get_json(force=True))


app.run()


## Hallo




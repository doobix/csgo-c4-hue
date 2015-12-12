import json
import requests
from flask import Flask, session, request, current_app

app = Flask(__name__)

@app.route("/", methods=["POST"])
def main():
    f = open('bomb_status', 'w')
    json_data = json.loads(request.data)
    round_data = json_data.get('round', {})
    bomb_status = str(round_data.get('bomb', ''))
    f.write(bomb_status)
    f.close()
    print bomb_status
    return 'plant the c4!'

if __name__ == "__main__":
    app.run(port=8080, debug=True)

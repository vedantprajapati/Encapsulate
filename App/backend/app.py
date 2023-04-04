import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from api.ApiHandler import handle_command

app = Flask(__name__)
CORS(app)

# NOTE: This route is needed for the default EB health check route
@app.route('/')
def home():
    return "ok"

@app.route('/get_topics')
def get_topics():
    return {"topics": ["topic1", "other stuff", "next topic"]}

@app.route('/submit_question', methods=["POST"])
def submit_question():
    question = json.loads(request.data)["question"]
    return {"answer": f"You Q was {len(question)} chars long"}

@app.route('/api/commands/help')
def command_help():
    cmd = request.args.get('cmd')
    # Here you can do any processing of the command that you need to do
    # For example, you might want to sanitize the command to prevent injection attacks
    # You can also execute the command on the server, and return the output to the client
    # For now, let's just return a response with the command that was received
    print(f"helping! {cmd}")
    response = f'helping: {cmd}'
    return jsonify(response)

@app.route('/api/commands/maps')
def command_map():
    cmd = request.args.get('cmd')
    # Here you can do any processing of the command that you need to do
    # For example, you might want to sanitize the command to prevent injection attacks
    # You can also execute the command on the server, and return the output to the client
    # For now, let's just return a response with the command that was received
    print(f"mapping! {cmd}")
    response = f'mapping: {cmd}'
    return jsonify(response)


@app.route('/api/commands/ritu')
def command_special():
    # data = request.get_json()
    # print(data)
    # cmd = data.get('cmd')
    cmd = request.args.get('cmd')
    # Here you can do any processing of the command that you need to do
    # For example, you might want to sanitize the command to prevent injection attacks
    # You can also execute the command on the server, and return the output to the client
    # For now, let's just return a response with the command that was received
    print(f"Secret Command! I LOVE YOU RITU!")
    response = f'Secret Command! I LOVE YOU RITU!'
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=8080)


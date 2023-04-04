from flask import jsonify, request

def handle_command(command):
    # Here you can do any processing of the command that you need to do
    # For example, you might want to sanitize the command to prevent injection attacks
    # You can also execute the command on the server, and return the output to the client
    # For now, let's just return a response with the command that was received
    response = {'output': f'Received command: {command}'}
    return jsonify(response)
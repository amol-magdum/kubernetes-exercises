from flask import Flask, jsonify, request
import os

app = Flask(__name__)
todos = []  # In-memory storage for now

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    todo = request.json.get('text', '')
    if not todo or len(todo) > 140:
        return jsonify({"error": "Invalid todo text"}), 400
    todos.append(todo)
    return jsonify({"message": "Todo added", "todo": todo}), 201

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
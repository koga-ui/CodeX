from flask import Flask, request, jsonify
from dataclasses import dataclass, field
from typing import List, Dict

app = Flask(__name__)

# In-memory storage for demo purposes
materials: Dict[int, dict] = {}
questions: Dict[int, dict] = {}
test_history: List[dict] = []

@app.route('/materials', methods=['POST'])
def create_material():
    data = request.json
    material_id = len(materials) + 1
    materials[material_id] = data
    return jsonify({'id': material_id}), 201

@app.route('/materials', methods=['GET'])
def list_materials():
    return jsonify(materials)

@app.route('/questions', methods=['POST'])
def create_question():
    data = request.json
    question_id = len(questions) + 1
    questions[question_id] = data
    return jsonify({'id': question_id}), 201

@app.route('/generate-test', methods=['POST'])
def generate_test():
    data = request.json
    # stub: just echo requested parameters
    test = {
        'materials': data.get('materials'),
        'range': data.get('range'),
        'count': data.get('count'),
    }
    test_history.append(test)
    return jsonify({'test': test})

@app.route('/history', methods=['GET'])
def history():
    return jsonify(test_history)

if __name__ == '__main__':
    app.run(debug=True)

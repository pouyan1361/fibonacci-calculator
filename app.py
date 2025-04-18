from flask import Flask, render_template, request, jsonify
from fibonacci import get_fibonacci_sequence

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        number = int(request.form['number'])
        if number < 0:
            return jsonify({'error': 'Please enter a non-negative number'})
        
        sequence = get_fibonacci_sequence(number)
        formatted_sequence = [f"F({i}) = {num}" for i, num in enumerate(sequence)]
        
        return jsonify({
            'sequence': sequence,
            'formatted_sequence': formatted_sequence
        })
    except ValueError:
        return jsonify({'error': 'Please enter a valid integer'})

if __name__ == '__main__':
    app.run(debug=True) 
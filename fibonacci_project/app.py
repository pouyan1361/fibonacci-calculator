from flask import Flask, render_template, request, jsonify
from fibonacci import get_fibonacci_sequence
from math_operations import factorial
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Try to get number from form data first
        number = request.form.get('number')
        if number is None:
            # If not in form data, try to get from JSON
            data = request.get_json()
            number = data.get('number') if data else None
        
        if number is None:
            return jsonify({'error': 'No number provided'})
            
        number = int(number)
        if number < 0:
            return jsonify({'error': 'Please enter a non-negative number'})
        
        # Calculate Fibonacci sequence
        app.logger.debug(f"Calculating Fibonacci sequence for n={number}")
        sequence = get_fibonacci_sequence(number)
        formatted_sequence = [f"F({i}) = {num}" for i, num in enumerate(sequence)]
        app.logger.debug(f"Fibonacci sequence: {sequence}")
        
        # Calculate factorial
        app.logger.debug(f"Calculating factorial for n={number}")
        fact = factorial(number)
        app.logger.debug(f"Factorial: {fact}")
        
        return jsonify({
            'sequence': sequence,
            'formatted_sequence': formatted_sequence,
            'factorial': fact
        })
    except ValueError as e:
        app.logger.error(f"ValueError: {str(e)}")
        return jsonify({'error': 'Please enter a valid integer'})
    except Exception as e:
        app.logger.error(f"Unexpected error: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred'})

if __name__ == '__main__':
    app.run(debug=True) 
from flask import Flask, request, jsonify, render_template
from calculator import DigitalYiJingCalculator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    number = data.get('number', '')
    # 呼叫分析邏輯
    results = DigitalYiJingCalculator.analyze_number(number)
    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True)
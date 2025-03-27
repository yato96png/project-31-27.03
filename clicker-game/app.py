from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Счетчик кликов
click_count = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/increment', methods=['POST'])
def increment():
    global click_count
    click_count += 1
    return jsonify({'click_count': click_count})

@app.route('/get_score', methods=['GET'])
def get_score():
    return jsonify({'click_count': click_count})

if __name__ == '__main__':
    app.run(debug=True)

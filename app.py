from flask import Flask, render_template ,jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    arr = [random.randint(10, 500) for _ in range(100)]  # 50 random numbers
    return render_template('index.html', arr=arr)

@app.route('/get_array')
def get_array():
    arr = [random.randint(10, 500) for _ in range(100)]  # 50 random numbers
    return jsonify(arr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 ,debug=True)
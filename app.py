from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    score = 0

    score += int(request.form['q1'])
    score += int(request.form['q2'])
    score += int(request.form['q3'])
    score += int(request.form['q4'])
    score += int(request.form['q5'])

    percentage = int((score / 25) * 100)

    if percentage < 50:
        result = "⚠️ Weak Immunity"
        advice = "Your immune system needs support."
    elif percentage < 75:
        result = "🙂 متوسط"
        advice = "You can improve your immunity."
    else:
        result = "💪 Strong Immunity"
        advice = "Keep your healthy habits!"

    return render_template("result.html", result=result, advice=advice, percentage=percentage)

if __name__ == '__main__':
    import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

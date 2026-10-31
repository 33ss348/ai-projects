from flask imort Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    units= int(request.form['units'])
    bill=units * 5 
     if units <= 100:
    message = f"Great your and energy saver!"
     elif units <= 200:
    message = f"Not bad, try to save a bit more."
     else:
    message = f"Time to switch of the lights ."

return render_template('result.html', bill=bill, message=message)
if __name__ == '__main__':
    app.run(debug=True)

<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Electricity Bill Calculator</title>
    </head>
    <body>
        <h1>Electricity Bill Calculator</h1>
        <form action="/calculate" method="post">
            <label for="units">Enter the number of units consumed:</label>
            <input type="number" id="units" name="units" placeholder="e.g.150" required>
            <button type="submit">Calculate </button>
        </form>
<div class="result">
<h2>Units used: {{ units }} kwh</h2>
<h2>Total Bill: ${{ bill }}</h2>
<p>Message: {{ message }}</p>
</div>
{% endif %}
    </body>
</html>
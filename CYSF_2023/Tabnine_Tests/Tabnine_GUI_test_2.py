## python tic tac toe game in flask

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tic_tac_toe = {
    'X': 'O',
    'O': 'X',
    'Draw': 'Draw'
}

@app.route('/tic-tac-toe', methods=['GET'])
def tic_tac_toe():
    return render_template('tic-tac-toe.html', board=tic_tac_toe)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tic-tac-toe', methods=['POST'])
def tic_tac_toe():
    if request.form['player1'] == 'X' and request.form['player2'] == 'O':
        return render_template('winner.html', winner='X')
    elif request.form['player1'] == 'O' and request.form['player2'] == 'X':
        return render_template('winner.html', winner='O')
    elif request.form['player1'] == 'X' and request.form['player2'] == 'X':
        return render_template('winner.html', winner='Draw')
    else:
        return render_template('winner.html', winner='Draw')

if __name__ == '__main__':
    app.run(debug=True)    
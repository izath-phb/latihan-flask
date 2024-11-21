from flask import Flask, render_template

app = Flask(__name__)

@app.route('/satu')
def getsatu():
    return render_template('satu.html')

@app.route('/matakuliah')
def getmatakuliah():
    ruang = ['D4.2', 'D4.3', 'D4.4']
    return render_template('matakuliah.html', ruang=ruang)

if __name__== '__main__':
    app.run(debug=True)


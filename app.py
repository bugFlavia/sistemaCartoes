from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    valorCompra = request.form['valorCompra']
    tipoCompra = request.form['tipoCompra']
    tipoPagamento = request.form['tipoPagamento']
    
    return render_template('process.html', valorCompra=valorCompra, tipoCompra=tipoCompra, tipoPagamento=tipoPagamento)

if __name__ == '__main__':
    app.run(debug=True)

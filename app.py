from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    valorCompra = float(request.form['valorCompra'])
    tipoCompra = request.form['tipoCompra']
    tipoPagamento = request.form['tipoPagamento']
    numeroParcelas = int(request.form.get('numeroParcelas', 1))

    # Cálculo do valor total com juros
    if tipoCompra == 'Parcelada':
        taxaJuros = 0.02  # 2% de juros por parcela
        valorTotalComJuros = valorCompra * (1 + taxaJuros) ** numeroParcelas
        valorMedioParcela = valorTotalComJuros / numeroParcelas
    else:
        valorTotalComJuros = valorCompra
        valorMedioParcela = valorCompra

    return render_template('process.html', 
                           valorCompra=valorCompra, 
                           tipoCompra=tipoCompra, 
                           tipoPagamento=tipoPagamento, 
                           valorTotalComJuros=valorTotalComJuros, 
                           numeroParcelas=numeroParcelas, 
                           valorMedioParcela=valorMedioParcela)

if __name__ == '__main__':
    app.run(debug=True)

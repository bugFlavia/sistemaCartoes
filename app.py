from flask import Flask, render_template, request

app = Flask(__name__)

def valorJuros(valor_compra, taxa_juros, numero_parcelas):
    valor_final = valor_compra * (1 + taxa_juros) ** numero_parcelas
    return valor_final

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    valorCompra = float(request.form['valorCompra'])
    tipoCompra = request.form['tipoCompra']
    tipoPagamento = request.form['tipoPagamento']
    numeroParcelas = int(request.form.get('numeroParcelas', 1))

    valorDesconto = valorCompra  # Valor padrão antes de aplicar qualquer desconto
    valorTotalComJuros = valorCompra  # Valor padrão antes de aplicar qualquer juros
    valorMedioParcela = 0

    if tipoCompra == 'Normal':
        if tipoPagamento == 'Pix' or tipoPagamento == 'Dinheiro':
            valorDesconto = valorCompra * (1 - 0.10)
    else:
        if numeroParcelas == 2:
            valorTotalComJuros = valorJuros(valorCompra, 0.02, numeroParcelas)
        elif numeroParcelas == 3:
            valorTotalComJuros = valorJuros(valorCompra, 0.05, numeroParcelas)
        elif numeroParcelas == 4:
            valorTotalComJuros = valorJuros(valorCompra, 0.08, numeroParcelas)
        elif numeroParcelas == 5:
            valorTotalComJuros = valorJuros(valorCompra, 0.10, numeroParcelas)
        elif numeroParcelas == 6:
            valorTotalComJuros = valorJuros(valorCompra, 0.15, numeroParcelas)

        # Calcular valor médio da parcela
        valorMedioParcela = format((valorTotalComJuros / numeroParcelas), '.2f')
        valorTotalComJuros = format(valorTotalComJuros, '.2f')

    return render_template('process.html', 
                           valorCompra=valorCompra, 
                           tipoCompra=tipoCompra, 
                           tipoPagamento=tipoPagamento, 
                           valorTotalComJuros=valorTotalComJuros, 
                           numeroParcelas=numeroParcelas, 
                           valorMedioParcela=valorMedioParcela, 
                           valorDesconto=valorDesconto)

if __name__ == '__main__':
    app.run(debug=True)

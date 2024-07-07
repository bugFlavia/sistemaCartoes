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
    
    print(f"Valor da compra: {valorCompra}")
    print(f"Tipo de compra: {tipoCompra}")
    print(f"Tipo de pagamento: {tipoPagamento}")
    
    return f"""
    Valor da compra recebido: {valorCompra}<br>
    Tipo de compra recebido: {tipoCompra}<br>
    Tipo de pagamento recebido: {tipoPagamento}
    """

if __name__ == '__main__':
    app.run(debug=True)

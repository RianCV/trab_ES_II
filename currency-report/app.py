from flask import Flask, request, jsonify
from datetime import datetime


app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({'status': 'UP'})


@app.route('/quote')
def quote():
# parâmetros: from, to
    frm = request.args.get('from', 'USD')
    to = request.args.get('to', 'BRL')


    # MOCK: gera um preço mockado (fixo + fração baseada em minuto)
    base_map = {('USD','BRL'): 5.42, ('EUR','BRL'): 5.90}
    base = base_map.get((frm, to), 1.0)


    timestamp = datetime.utcnow().isoformat() + 'Z'
    price = round(base + (datetime.utcnow().minute % 10) * 0.01, 4)


    return jsonify({
    'from': frm,
    'to': to,
    'price': price,
    'timestamp': timestamp
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8100)

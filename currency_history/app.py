from flask import Flask, request, jsonify
from datetime import datetime, timedelta


app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({'status': 'UP'})


@app.route('/history')
def history():
    frm = request.args.get('from', 'USD')
    to = request.args.get('to', 'BRL')


    # MOCK: gera 6 pontos nos últimos 30 minutos
    now = datetime.utcnow()
    values = []
    base_map = {('USD','BRL'): 5.42, ('EUR','BRL'): 5.90}
    base = base_map.get((frm, to), 1.0)


    for i in range(6):
        ts = (now - timedelta(minutes=5*i)).isoformat() + 'Z'
        price = round(base + (i * 0.01), 4)
        values.append({'timestamp': ts, 'price': price})


    return jsonify({'from': frm, 'to': to, 'values': values})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8101)
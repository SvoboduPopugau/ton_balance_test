from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# https://tonapi.io/


@app.route('/api/balance', methods=['GET'])
def get_ton_balance():
    try:
        ton_address = request.args.get('address')
        print(ton_address)
        if not ton_address:
            return jsonify({'error': 'Address parameter is missing.'}), 400

        response = requests.get(f'https://tonapi.io/v2/blockchain/accounts/{ton_address}')
        if response.status_code == 200:
            data = response.json()
            balance = data['balance']
            return jsonify({'balance': balance}), 200
        else:
            return jsonify({'error': 'Failed to retrieve TON balance.'}), response.status_code
    except Exception as e:
        return jsonify({'error': f'Failed to get balance: {e}'}), 500

if __name__ == '__main__':
    app.run()

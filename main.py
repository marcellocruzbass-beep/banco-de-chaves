import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# LISTA DE CHAVES VÁLIDAS
CHAVES_VALIDAS = [
    "bdt2-rlg8-d3zg-h4b8-45dd-89zp-ygkj",
    "a1b2-c3d4-e5f6-g7h8-i9j0-k1l2-m3n4",
    "x9y8-z7w6-v5u4-t3s2-r1q0-p9o8-n7m6",
    "k5j4-h3g2-f1d0-s9a8-p7o6-i5u4-y3t2",
    "m1n2-b3v4-c5x6-z7l8-k9j0-h1g2-f3d4"
]

# Senha para que apenas o seu servidor de licenças consiga consultar este banco
SECRET_KEY = os.getenv('PLUGIN_SECRET_KEY', 'SenhaSegura2024!')

@app.route("/verify", methods=["POST"])
def verify():
    data = request.get_json()
    
    if data.get('auth_token') != SECRET_KEY:
        return jsonify({"success": False, "error": "Acesso negado"}), 403

    user_key = data.get('key')
    
    if user_key in CHAVES_VALIDAS:
        return jsonify({"success": True, "status": "active"}), 200
    else:
        return jsonify({"success": False, "status": "invalid"}), 403

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)

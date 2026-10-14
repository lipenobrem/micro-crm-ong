from app import create_app
from flask import Flask

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

from flask import Flask

app = Flask(__name__)
app.secret_key = "chave_super_secreta_ong" 



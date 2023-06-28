from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)

# Configurações do banco de dados MySQL
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'bgg_technologies'


mysql = MySQL(app)

# Rota inicial
@app.route('/')
def server_UP():
    return 'Server UP'

# Rota para exemplo de retorno JSON
@app.route('/api/exemplo', methods=['GET'])
def exemplo():
    data = {'mensagem': 'Exemplo de retorno JSON'}
    return jsonify(data)

# Rota para exemplo de parâmetros na URL
@app.route('/api/saudacao/<nome>', methods=['GET'])
def saudacao(nome):
    mensagem = f'Olá, {nome}!'
    return mensagem

# Rota para listar os produtos
@app.route('/api/products', methods=['GET'])
def get_products():
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM produtos')
    results = cursor.fetchall()

    products = []
    for row in results:
        user = {
            'cod': row[0],
            'nome': row[1],
            'preco': row[2]
        }
        products.append(user)

    cursor.close()
    conn.close()

    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)

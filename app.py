from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'nome': 'rafael',
     'habilidades': ['phyton', 'flask']
     },
    {
        'nome': 'eduardo',
        'habilidades': ['nodejs', 'javascript']
    }
]
#desenvolvedor pela id
@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':

        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'desenvolvedor de Id {} não existe' .format(id)
            response = {'satus': 'erro', 'mensagem': mensagem}


        except Exception:
            mensagem = 'erro desconhecido. procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}

        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'satus': 'sucesso', 'mensagem': 'registro excluido'})

#todos os desenvolvedores

@app.route('/dev', methods = ['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status': 'sucesso', 'mensagem': 'registro inserido'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)





if __name__ == '__main__':
    app.run(debug=True)
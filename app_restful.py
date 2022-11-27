import json

from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {   'id': 1,
        'nome': 'rafael',
     'habilidades': ['phyton', 'flask']
     },
    {
        'id': 2,
        'nome': 'eduardo',
        'habilidades': ['nodejs', 'javascript']
    }
]

class desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'desenvolvedor de Id {} não existe'.format(id)
            response = {'satus': 'erro', 'mensagem': mensagem}


        except Exception:
            mensagem = 'erro desconhecido. procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}

        return response
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'satus': 'sucesso', 'mensagem': 'registro excluido'}


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]




api.add_resource(desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/dev')

if __name__ == '__main__':
    app.run(debug=True)
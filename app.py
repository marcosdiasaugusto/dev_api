from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'id': 0, 'nome': 'Marcos',
     'habilidades':['Python','Flask','Django']},
    {'id':1, 'nome': 'Denise',
     'habilidades':['Python','Django']},
    {'id': 2,
        "habilidades": [
            "História",
            "Geografia",
            "Relações Internacionais"
        ],
        "nome": "Henrique"
    },
    {
        "habilidades": [
            "Segurança do Trabalho",
            "Seguros",
            "Relações Internacionais"
        ],
        "id": 3,
        "nome": "Emily"
    }
]

# devolve, altera e deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            # desenvolvedor = desenvolvedores[id]
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe!'.format(id)
            response = {'status':'erro','mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Contacte o administrador do API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso','mensagem':'Registro excluído com Sucesso!'})
        return

# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/', methods=['POST','GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)
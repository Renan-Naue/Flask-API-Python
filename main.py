from flask import Flask, request, Response

empregados =[ 
            {'nome' : 'Valentina', 'cargo' : 'analista', 'salario' : 5000},
            {'nome' : 'Ze', 'cargo' : 'policial', 'salario' : 5000}, 
            {'nome' : 'Joao', 'cargo' : 'policial', 'salario' : 12000 },
]

users = [
            {'username' : 'Renan', 'secret' : '123456'}

        ]


def check_user(username, secret):
    for user in users:
        if (user['username'] == username) and (user['secret'] == secret):
            return True

    return False

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Home page</h1>'


@app.route('/empregados')
def get_empregados():
    return {'empregados' : empregados}


@app.route('/empregados/<cargo>')
def get_empregados_cargo(cargo):
    out_empregados = []
    for empregado in empregados:
        if cargo == empregado['cargo'].lower():
            out_empregados.append(empregado)
    return {'empregados' : out_empregados}


@app.route('/empregados/<info>/<value>')
def get_empregados_info(info, value):
    out_empregados = []
    for empregado in empregados:
        if info in empregado.keys():
            value_empregado = empregado[info]

            if type(value_empregado) == str:
                if value == value_empregado.lower():
                    out_empregados.append(empregado)
            if type(value_empregado) == int:
                if int(value) == value_empregado:
                    out_empregados.append(empregado)
    
    return {'empregados' : out_empregados}


@app.route('/informations', methods=['POST'])
def get_empregados_post():
    username = request.form['username']
    secret = request.form['secret']

    
    if not check_user(username, secret):
        return Response('Unauthorized', status=401)

    info = request.form['info']
    value = request.form['value']
    
    out_empregados = []
    for empregado in empregados:
        if info in empregado.keys():
            value_empregado = empregado[info]

            if type(value_empregado) == str:
                if value == value_empregado.lower():
                    out_empregados.append(empregado)
            if type(value_empregado) == int:
                if int(value) == value_empregado:
                    out_empregados.append(empregado)
    
    return {'empregados' : out_empregados}


if __name__ == '__main__':
    app.run(debug=True)
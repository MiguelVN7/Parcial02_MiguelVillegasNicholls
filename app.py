"""
Microservicio Flask para cálculo de factorial y decir si es par o impar.
"""

from flask import Flask, jsonify

app = Flask(__name__)
app.json.sort_keys = False


@app.route('/factorial/<int:numero>', methods=['GET'])
def calcular_factorial(numero):  
    factorial = 1
    for i in range(2, numero + 1):
        factorial = i * factorial

    if numero % 2 == 0:
        paridad = "par"
    else:
        paridad = "impar"
    
    resultado = {
        "numero": numero,
        "factorial": factorial, 
        "paridad": paridad 
    }
    
    return jsonify(resultado)


@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "mensaje": "Microservicio para Parcial 2 de AS con calculo de Factorial y Paridad",
        "uso": "/factorial/numero",
        "ejemplo": "/factorial/5"
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

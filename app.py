"""
Microservicio Flask para cálculo de factorial y paridad.

Este microservicio recibe un número por URL y devuelve:
- El número recibido
- Su factorial
- Una etiqueta indicando si es "par" o "impar"
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/factorial/<int:numero>', methods=['GET'])
def calcular_factorial(numero):
    """
    Endpoint que recibe un número y devuelve información sobre él.
    
    Parámetros:
    - numero (int): Número entero recibido por URL
    
    Retorna:
    - JSON con: numero, factorial, paridad
    """
    # TODO: Implementar la lógica del cálculo del factorial
    # TODO: Implementar la lógica para determinar si es par o impar
    
    resultado = {
        "numero": numero,
        "factorial": None,  # Implementar cálculo
        "paridad": None     # Implementar validación par/impar
    }
    
    return jsonify(resultado)


@app.route('/', methods=['GET'])
def home():
    """Endpoint de bienvenida con instrucciones de uso."""
    return jsonify({
        "mensaje": "Microservicio de Factorial y Paridad",
        "uso": "/factorial/<numero>",
        "ejemplo": "/factorial/5"
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

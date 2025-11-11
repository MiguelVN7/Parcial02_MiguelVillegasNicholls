# Parcial 2 - Arquitectura de Software

Repositorio para la parte práctica del Parcial 2 de la materia Arquitectura de Software, por Miguel Villegas. Es un:

Microservicio con **Flask** que recibe un número por URL y devuelve una respuesta JSON con:

- El número recibido
- Su factorial
- Una etiqueta indicando si es "par" o "impar" (el número original)


## Configuración del Entorno

### 1. Clonar el repo
```
git clone git@github.com:MiguelVN7/Parcial02_MiguelVillegasNicholls.git
cd Parcial02_MiguelVillegasNicholls
```

### 2. Crear entorno virtual
```
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```
pip install -r requirements.txt
```

### 4. Ejecutar
```
python app.py
```

## Respuesta a Pregunta
Si el microservicio se debiera comunicar con otro encargado de almacenar el historial de cálculos en una base de datos externa, cambiaría su diseño para que, una vez se haya generado la respuesta al cliente, se envíe asíncronamente una 
solicitud (con un POST) al microservicio que contiene el historial con los datos del cálculo realizado. Así podría guardar
la información sin dañar el rendimiento ni aumentar el tiempo de respuesta del microservicio inicial. Además, se debería
definir un formate JSON para el intercambio de esta información. Estos dos microservicios serían completamente independientes
y desacoplados uno del otro permitiendo su comunicación solo a través de sus APIs. Por último, se debería incluir unn mecanismo básico que permita el reintento del envío en caso de que falle.


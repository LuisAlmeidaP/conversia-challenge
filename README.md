# CONVERSIA CHALLENGE

Proyecto Desarrollado con [FastApi] (https://fastapi.tiangolo.com/)

## Requisitos
- [Python 3.8+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)

## Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/LuisAlmeidaP/conversia-challenge.git
   cd conversia-challenge/

3. Instalar Dependencias
    #### Crear un Entorno Virtual
   ```
   python -m venv venv
   pip install -r requirements.txt

4. Variables de Entorno
    #### - Crear archivo `.ENV`
    #### - Asignar los Sigueintes Valores al `.ENV` 
    
| Variable             | Descripción                                                                                        |
|----------------------|----------------------------------------------------------------------------------------------------|
| `DATABASE_URL`       | Conexion a la Base de Datos (ejemplo : `postgresql://usuario:contraseña@localhost:5432/nombre_db`) |
| `TWILIO_ACCOUNT_SID` | SID de Twilio.                                                                                     |
| `TWILIO_AUTH_TOKEN`  | Token de autenticación de Twilio.                                                                  |
| `TWILIO_PHONE_NUMBER`| Número de teléfono de Twilio.                                                                      |

5. Levantar el Servicio de Docker
    ```
    docker-compose up --build

6. Levantar Servidor
    ```
    python .\src\app.py

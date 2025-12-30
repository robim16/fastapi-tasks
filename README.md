Fast Api Tasks

DESCRIPCIÓN

Esta es una aplicación de tareas desarrollada utilizando el framework fastapi, docker, el ORM SQLAlchemy y base de datos PostgreSQL. La aplicación permite realizar todas las operaciones del CRUD, validando la autenticación de los usuarios mediante token con JWT y hasheo de contraseñas.La 
app es susceptible de mejoras tales como el uso de arquitecturas limpias, clases para testing, microservicios, resiliencia, comunicacion asíncrona, entre otros.



ESTRUCTURA DEL PROYECTO

app/
├── api/
│   ├── auth.py
│   └── tasks.py
├── core/
│   ├── config.py
│   ├── security.py
│   └── dependencies.py
├── db/
│   ├── base.py
│   ├── session.py
    ├── seed.py
│   └── migrations/
├── models/
│   ├── user.py
│   └── task.py
├── schemas/
│   ├── auth.py
│   └── task.py
└── main.py


VARIABLES DE ENTORNO

Crear un archivo .env en la raíz del proyecto:

DB_HOST=localhost
DB_PORT=5432
DB_NAME=technical_test
DB_USER=postgres
DB_PASSWORD=postgres

SECRET_KEY=super-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=60
ALGORITHM=HS256


EJECUTAR LA APP 

1 Instalar las dependencias necesarias: pip install -r requirements.txt

2 Activar entorno virtual: source venv/bin/activate

3 Crear y levantar los servicios de postgresql: docker-compose up -d

4 Correr las migraciones: alembic upgrade head

5 Levantar la aplicación: uvicorn app.main:app --reload

6 Abrir la url http://localhost:8000/docs en el navegador o en postman hacer un post request a     http://127.0.0.1:8000/auth/login con un json así:

{
    "username": "admin",
    "password": "admin123"
}

7 Autenticarse mediante el endpoint de login y copiar el token 

8 agregar el token en postman o swagger

9 Listar y crear la primera tarea  (en postman http://127.0.0.1:8000/tasks GET y POST requests con un json así:
    {
    "title": "string",
    "description": "string"
    }
)


Ver sección endpoints.


USUARIO INICIAL

username: admin
password: admin123

El usuario inicial es insertado mediante un seed que es llamado al iniciar la app por primera vez;
los seed son ampliamente utilizados en diversos framework y permiten poblar la db en ambiente de desarrollo sin manipular las bases de datos directamente

Las rutas se protegen mediante bearer token.


ENDPOINTS:

Autenticación

POST /auth/login


Tasks:

crear task: POST /tasks
listar tasks: GET /tasks?page=1&page_size=10
obtener una task por id: GET /tasks/{task_id}
actualizar task: PUT /tasks/{task_id}
eliminar task: DELETE /tasks/{task_id}

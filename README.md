Fast Api Tasks

DESCRIPCIÓN

Esta es una aplicación de tareas desarrollada utilizando el framework fastapi, docker, el ORM SQLAlchemy y base de datos PostgreSQL. La aplicación permite realizar todas las operaciones del CRUD, validando la autenticación de los usuarios mediante token con JWT y hasheo de contraseñas.


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


EJECUTAR LA APP 

Instalar las dependencias necesarias: pip install -r requirements.txt
Activar entorno virtual: source venv/bin/activate
Crear y levantar los servicios de postgresql: docker-compose up -d
Correr las migraciones: alembic upgrade head
Levantar la aplicación: uvicorn app.main:app --reload
abrir la url http://localhost:8000/docs en el navegador



USUARIO INICIAL

username: admin
password: admin123


ENDPOINTS:

Autenticación

POST /auth/login


Tasks:

crear task: POST /tasks
listar tasks: GET /tasks?page=1&page_size=10
obtener una task por id: GET /tasks/{task_id}
actualizar task: PUT /tasks/{task_id}
eliminar task: DELETE /tasks/{task_id}

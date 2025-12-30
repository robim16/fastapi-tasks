from fastapi import FastAPI
from app.api import auth, task
from app.db.session import SessionLocal
from app.db.seed import seed_admin_user


app = FastAPI(title="FastAPI Tasks")

@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    try:
        seed_admin_user(db)
    finally:
        db.close()

app.include_router(auth.router)
app.include_router(task.router)

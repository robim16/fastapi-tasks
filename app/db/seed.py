from sqlalchemy.orm import Session

from app.models.user import User
from app.core.security import hash_password


def seed_admin_user(db: Session):
    admin = db.query(User).filter(
        User.username == "admin"
    ).first()

    if not admin:
        admin = User(
            username="admin",
            password_hash=hash_password("admin123"),
        )
        db.add(admin)
        db.commit()

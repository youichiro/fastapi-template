from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Datetime, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text

from .database import Base


class AdminAccount(Base):
    __tablename__ = "admin_accounts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    admin_name = Column(String(225), nullable=False, unique=True, index=True)
    admin_secret = Column(String(64), nullable=False, unique=True, index=True)
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    accounts = relationship("Account", back_populates="admin_accounts")


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    admin_account_id = Column(Integer, ForeignKey("admin_accounts.id"), nullable=False)
    external_user_id = db.Column(db.String(225), nullable=False, unique=True, index=True)
    school_id = db.Column(db.Integer, nullable=False, index=True)
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    admin_account = relationship("AdminAccount", back_populates="accounts")

    __table_args__ = (
        db.UniqueConstraint("admin_account_id", "external_user_id"),
    )



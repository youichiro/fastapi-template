from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, UniqueConstraint
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

    accounts = relationship("Account", back_populates="admin_account")


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    admin_account_id = Column(Integer, ForeignKey("admin_accounts.id"), nullable=False)
    external_user_id = Column(String(225), nullable=False, unique=True, index=True)
    school_id = Column(Integer, nullable=False, index=True)
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    admin_account = relationship("AdminAccount", back_populates="accounts")

    __table_args__ = (UniqueConstraint("admin_account_id", "external_user_id"),)


class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    section_code = Column(String(50), nullable=False)
    is_correct = Column(Boolean, nullable=False)
    answered_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from settings.database import Base


class User(Base):
    __tablename__ = "users"

    username = Column(String, unique=True)
    email = Column(String, null=True)
    is_active = Column(Boolean, default=True)
    blogs = relationship("Blog", back_populates="user")



class Blog(Base):
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="blogs")

    title = Column(String)
    description = Column(String)

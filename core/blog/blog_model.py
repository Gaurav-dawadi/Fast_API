from ..base_model import Base
from sqlalchemy import Column, ForeignKey, Integer, String
# from sqlalchemy.orm import declarative_base, relationship


class BlogModel(Base):
    __tablename__ = "blogs"
    title = Column(String, index=True)
    description = Column(String, index=True)
    # id = Column(Integer, primary_key=True, index=True)
    # owner_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    # owner = relationship("User", back_populates="blogs")
    def __repr__(self):
        return f"Blog(id={self.id!r}, title={self.title!r})"
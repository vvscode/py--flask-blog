import json
from sqlalchemy import Column, ForeignKey, Integer, Numeric, Table, Text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from app import db

Base = db.Model
metadata = Base.metadata

posts_to_tags = Table(
    "posts_to_tags",
    Base.metadata,
    Column("posts", Integer, ForeignKey("posts.post_id", ondelete="CASCADE")),
    Column("tags", Integer, ForeignKey("tags.tag_id", ondelete="CASCADE")),
)


class Tag(Base):
    __tablename__ = "tags"

    tag_id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)


class Post(Base):
    __tablename__ = "posts"

    post_id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    short = Column(Text)
    full = Column(Text, nullable=False)
    picture = Column(Text)
    tags = relationship("Tag", secondary=posts_to_tags, backref="posts")

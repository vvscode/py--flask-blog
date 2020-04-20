"""initial seed

Revision ID: 00000000002
Revises:
Create Date: 2020-04-20 15:00:45.144060

"""
import json
import os

from app import db
from data.models import Post, Tag

# revision identifiers, used by Alembic.
revision = "00000000002"
down_revision = "00000000001"
branch_labels = None
depends_on = None

basedir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(basedir, "00000000002_initial_state_seed__posts.json")) as file:
    posts = json.loads(file.read())


with open(os.path.join(basedir, "00000000002_initial_state_seed__tags.json")) as file:
    tags = json.loads(file.read())


def upgrade():
    # Tags
    tags_map = {}
    for tag_name in tags.keys():
        tag = Tag(name=tags[tag_name])
        db.session.add(tag)
        tags_map[tag_name] = tag

    db.session.commit()

    # Posts
    for post_item in posts:
        post = Post(
            title=post_item["title"],
            short=post_item["short"],
            full=post_item["full"],
            picture=post_item["picture"],
        )

        db.session.add(post)

        for tag in post_item["tags"]:
            post.tags.append(tags_map[tag])

    db.session.commit()


def downgrade():
    print(f"Migration #{revision} has no downgrade option")
    print("But you can add here removing data from columns")

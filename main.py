from flask import render_template, abort, request, redirect, url_for
from app import app
from data import models


@app.route("/")
def index():
    return render_template(
        "posts.j2", tags=models.Tag.query.all(), posts=models.Post.query.all()
    )


@app.route("/tags/<tag_id>/")
def tags(tag_id):
    tag = models.Tag.query.get(tag_id)
    return render_template(
        "posts.j2",
        title=tag.name,
        posts=models.Post.query.filter(
            models.Post.tags.any(models.Tag.tag_id == tag_id)
        ).all(),
    )


@app.route("/post/<post_id>/")
def post(post_id):
    post = models.Post.query.get(post_id)
    return render_template("post.j2", title=post.title, post=post,)


@app.errorhandler(404)
def page_not_found(error):
    return (
        render_template("404.j2", title="404"),
        404,
    )


if __name__ == "__main__":
    app.run()

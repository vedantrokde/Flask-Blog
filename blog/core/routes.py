from flask import Blueprint, request, render_template
from blog.models import Post

core = Blueprint("core", __name__)


@core.route("/")
@core.route("/home")
def home():
    page = request.args.get("page", 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=5, page=page)
    return render_template("home.html", posts=posts)


@core.route("/about")
def about():
    return render_template("about.html", title="About")

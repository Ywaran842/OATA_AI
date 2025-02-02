# /home/yokeshwaran/Desktop/flask/flaskr/main/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, g, flash, current_app, abort
from . import bp
from flaskr.Class.Session import SessionManager
from flaskr.auth.routes import login_required
from flaskr.Class.beforequest import gset
from flaskr.Class.userdata import userdata
from flaskr.wtf_Class.wtf_Main import Createpost, Updatepost



@bp.before_request
def before_request():
    userid = SessionManager.get_session('userid')
    g.userid = userid


@bp.route('/')
@login_required
def index():
    user = userdata(g.userid)
    posts = user.get_post()
    return render_template('home.html', post=posts)

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = Createpost()
    if request.method == 'POST':
        if not form.validate_on_submit():
            flash('Please enter valid credentials')
            return redirect(url_for('main.create'))
        title = form.title.data
        body = form.body.data
        img_file = form.img.data
        img  = img_file.read()
        user = userdata(g.userid)
        current_app.logger.info(f"User id: {g.userid} on create")
        user.set_post(title, body, img)
        return redirect(url_for('main.index'))
    return render_template('create.html', form=form)

@bp.route('/<string:id>/update', methods=['GET', 'POST'])
@login_required
def update(id):
    posts = userdata(g.userid).Get_post_by_id(id)
    if posts is None:
        flash('post not found')
        return(redirect(url_for('main.index')))
    form = Updatepost()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        img_file = form.img.data
        img = img_file.read()
        userdata(g.userid).update_post(title, body, img, id)
        return redirect(url_for('main.index'))
    return render_template('update.html', post=posts, form = form)

@bp.route('/<string:id>/delete', methods=['POST'])
@login_required
def Deletepost(id):
    post = userdata(g.userid)
    if not post.Deletepost(id):
        return redirect(url_for('main.index'))
    return redirect(url_for('main.index'))


   


@bp.route('<string:id>/like', methods=['POST'])
@login_required
def like(id):
    posts = userdata(g.userid)
    if posts.Like(id) is False:
        flash('post not found')
        return redirect(url_for('main.index'))
    return redirect(url_for('main.index'))






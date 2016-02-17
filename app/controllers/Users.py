from system.core.controller import *
from flask import Flask, session
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
flask_bcrypt = Bcrypt(app)
import re

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')

    def index(self):
        ideas = self.models['User'].get_ideas()
        comments = self.models['User'].get_comments()
        return self.load_view('index.html', ideas=ideas, comments=comments)

    def register(self):
        user_info = {
            "username" : request.form.get('username'),
            "password" : request.form.get('password'),
            "pw_confirm" : request.form.get('pw_confirm')
        }
        create_status = self.models['User'].register(user_info)
        if create_status['status'] == True:
            return redirect('/bright_ideas')
        else:
            for message in create_status['errors']:
                flash(message)
            return redirect('/main')

    def login(self):
        return self.load_view('login.html')

    def signin(self):
        login_info = {
            "username" : request.form.get('username'),
            "password" : request.form.get('password')
        }
        login_status = self.models['User'].signin(login_info)

        if login_status['status'] == True:
            return redirect('/bright_ideas')
        else:
            invalid = "Error: invalid username or password"
            flash(invalid)
            return redirect('/main')

    def logout(self):
        session.clear()
        return redirect('/main')

    def post(self):
        content = request.form.get('content')
        self.models['User'].post_idea(content)
        return redirect('/bright_ideas')

    def like(self, id):
        self.models['User'].like(id)
        return redirect('/bright_ideas')

    def comment(self, id):
        comment_info = {
            "idea_id" : id,
            "content" : request.form.get('content')
        }
        self.models['User'].comment(comment_info)
        return redirect('/bright_ideas')


    def users(self, id):
        user_info = self.models['User'].users(id)
        comment_count = self.models['User'].comment_count(id)
        return self.load_view('show_user.html', user_info=user_info, comment_count=comment_count)

    def show_idea(self, id):
        display_post = self.models['User'].display_post(id)
        all_likes = self.models['User'].show_idea(id)
        return self.load_view('show_idea.html', display_post=display_post[0], all_likes=all_likes)

    def update(self, id):
        display_post = self.models['User'].display_post(id)
        return self.load_view('edit_idea.html', display_post=display_post[0])

    def edit(self, id):
        info = {
            "content": request.form.get('content'),
            "id": id
        }
        self.models['User'].edit(info)
        return redirect('/bright_ideas')


    def delete(self, id):
        self.models['User'].delete_idea(id)
        return redirect('/bright_ideas')

    def delete_comment(self, id):
        self.models['User'].delete_comment(id)
        return redirect('/bright_ideas')

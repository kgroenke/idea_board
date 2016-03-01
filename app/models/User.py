from system.core.model import Model
from flask import Flask, session
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
flask_bcrypt = Bcrypt(app)
import re

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def register(self, user_info):
        password = user_info['password']

        errors = []

        check_username_query = "SELECT * FROM users WHERE username = '{}'".format(user_info['username'])
        usernames = self.db.query_db(check_username_query)

        if len(usernames) > 0:
            errors.append("That username already exists")
        if len(user_info['username']) < 2:
            errors.append('Username must be at least two characters')
        if len(user_info['password']) < 8:
            errors.append('Password must be at least 8 characters')
        if user_info['password'] != user_info['pw_confirm']:
            errors.append('Passwords must match')

        if errors:
            return {
            "status" : False,
            "errors" : errors
            }
            print errors['errors']

        else:
            pw_hash = self.bcrypt.generate_password_hash(password)
            registration_query = "INSERT INTO users (username, pw_hash, created_at, updated_at) VALUES ('{}', '{}', NOW(), NOW())".format(user_info['username'], pw_hash)
            self.db.query_db(registration_query)

            select_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            user = self.db.query_db(select_user_query)
            session['id'] = user[0]['id']

            session['username'] = user_info['username']
            session['id'] = user[0]['id']
            return{"status" : True}

    def signin(self, login_info):
        password = login_info['password']
        signin_query = "SELECT * FROM users WHERE username='{}' LIMIT 1".format(login_info['username'])

        user = self.db.query_db(signin_query)

        if user != []:
            if self.bcrypt.check_password_hash(user[0]['pw_hash'], password):
                session['username'] = user[0]['username']
                session['id'] = user[0]['id']
                return {"status" : True}
            else:
                return{"status" : False}

        else:
            return{"status" : False}

    def get_ideas(self):
        get_ideas_query = "SELECT ideas.id AS id, content, like_count, user_id, username FROM ideas JOIN users ON users.id = ideas.user_id ORDER BY like_count DESC"
        return self.db.query_db(get_ideas_query)

    def get_comments(self):
        get_comments_query = "SELECT comments.content, comments.idea_id, comments.user_id AS commenter_id, users.username AS commenter_name, comments.id FROM comments LEFT JOIN users ON users.id = comments.user_id"
        return self.db.query_db(get_comments_query)


    def post_idea(self, content):
        post_idea_query = "INSERT INTO ideas(content, like_count, user_id) VALUES($${}$$, 0, '{}')".format(content, session['id'])
        return self.db.query_db(post_idea_query)

    def like(self, id):
        like_query = "INSERT INTO likes(idea_id, liker_id) VALUES('{}', '{}')".format(id, session['id'])
        like = self.db.query_db(like_query)

        update_count_query = "UPDATE ideas SET like_count = like_count + 1 WHERE id ='{}'".format(id)
        self.db.query_db(update_count_query)

        return like

    def users(self, id):
        user_info_query = "SELECT username, COUNT(ideas.id) AS idea_count, SUM(ideas.like_count) AS total_likes FROM users LEFT JOIN ideas ON users.id = ideas.user_id WHERE users.id = '{}' GROUP BY username".format(id)
        return self.db.query_db(user_info_query)

    def comment_count(self, id):
        comment_count_query = "SELECT COUNT(comments.content) AS comment_count FROM comments WHERE comments.user_id='{}'".format(id)
        return self.db.query_db(comment_count_query)


    def display_post(self, id):
        display_post_query = "SELECT username, content, ideas.id AS idea FROM ideas JOIN users ON ideas.user_id = users.id WHERE ideas.id = '{}'".format(id)
        return self.db.query_db(display_post_query)

    def show_idea(self, id):
        idea_likes_query = "SELECT username, users.id AS user_id FROM users LEFT JOIN likes ON users.id = likes.liker_id WHERE likes.idea_id = '{}' GROUP BY user_id".format(id)
        return self.db.query_db(idea_likes_query)

    def delete_idea(self, id):
        delete_likes_query = "DELETE FROM likes WHERE idea_id = '{}'".format(id)
        self.db.query_db(delete_likes_query)

        delete_comments_query = "DELETE FROM comments WHERE idea_id = '{}'".format(id)
        self.db.query_db(delete_comments_query)

        delete_idea_query = "DELETE FROM ideas WHERE id = '{}'".format(id)
        return self.db.query_db(delete_idea_query)

    def delete_comment(self, id):
        delete_comment_query = "DELETE FROM comments WHERE id = '{}'".format(id)
        self.db.query_db(delete_comment_query)

    def comment(self, comment_info):
        create_comment_query = "INSERT INTO comments(content, created_at, updated_at,  idea_id, user_id) VALUES('{}', NOW(), NOW(), '{}', '{}')".format(comment_info['content'], comment_info['idea_id'], session['id'])
        return self.db.query_db(create_comment_query)

    def edit(self, info):
        update_query = "UPDATE ideas SET content = '{}' WHERE id = '{}'".format(info['content'], info['id'])
        return self.db.query_db(update_query)

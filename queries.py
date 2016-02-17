Create idea:
"INSERT INTO ideas(content, like_count, user_id) VALUES('{}', 0, '{}')".format()

Like:
"INSERT INTO likes(created_at, update_at, idea_id, liker_id)
VALUES(NOW(), NOW(), '{}', '{}')".format()

Like Count:
"UPDATE ideas SET like_count = like_count + 1 WHERE id='{}'".format()


delete likes
DELETE FROM likes WHERE idea_id = 5
DELETE FROM ideas WHERE id = 5

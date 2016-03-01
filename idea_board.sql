DROP TABLE IF EXISTS likes;
DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS ideas;
DROP TABLE IF EXISTS users;


CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username TEXT,
  pw_hash TEXT,
  created_at TEXT,
  updated_at TEXT
);

CREATE TABLE ideas (
  id SERIAL PRIMARY KEY,
  content TEXT,
  like_count INTEGER,
  user_id INTEGER REFERENCES users(id),
  created_at TEXT,
  updated_at TEXT
);

CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  content TEXT,
  user_id INTEGER REFERENCES users(id),
  idea_id INTEGER REFERENCES ideas(id),
  created_at TEXT,
  updated_at TEXT
);

CREATE TABLE likes (
  id SERIAL PRIMARY KEY,
  idea_id INTEGER REFERENCES ideas(id),
  liker_id INTEGER REFERENCES users(id),
  created_at TEXT,
  updated_at TEXT
);

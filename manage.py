"""
    Base terminal command manager.

    Define terminal commands here to run actions
"""
from flask.ext.script import Manager, Server
from system.init import initialize_app
import subprocess
import os
# import psycopg2
# import urlparse
#
# urlparse.uses_netloc.append("postgres")
# url = urlparse.urlparse(os.environ["DATABASE_URL"])
#
# conn = psycopg2.connect(
#     database=url.path[1:],
#     user=url.username,
#     password=url.password,
#     host=url.hostname,
#     port=url.port
# )


manager = Manager(initialize_app())

port = int(os.environ.get("PORT", 5000))
server = Server(host="0.0.0.0", port=port)

manager.add_command('runserver', server)

if __name__ == "__main__":
    manager.run()

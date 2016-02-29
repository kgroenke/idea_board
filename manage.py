"""
    Base terminal command manager.

    Define terminal commands here to run actions
"""
from flask.ext.script import Manager, Server
from system.init import initialize_app
import subprocess
import os

manager = Manager(initialize_app())

port = int(os.environ.get("PORT", 5000))
server = Server(host="0.0.0.0", port=port)

manager.add_command('runserver', server)

if __name__ == "__main__":
    manager.run()

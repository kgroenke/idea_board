"""
    Database Specific Configuration File
"""
""" Put Generic Database Configurations here """

import os
import psycopg2
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

class DBConfig(object):
    """ DB_ON must be True to use the DB! """
    DB_ON = True
    DB_DRIVER = 'postgres'
    DB_ORM = False

""" Put Development Specific Configurations here """
class DevelopmentDBConfig(DBConfig):
    DB_USERNAME = url.username
    DB_PASSWORD = url.password
    DB_DATABASE_NAME = 'idea_board'
    DB_HOST = url.hostname
    DB_PORT = url.port
    """ unix_socket is used for connecting with MAMP. Take this out if you aren't using MAMP """
    # DB_OPTIONS = {
    #     'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock'
    # }

""" Put Staging Specific Configurations here """
class StagingDBConfig(DBConfig):
    DB_USERNAME = url.username
    DB_PASSWORD = url.password
    DB_DATABASE_NAME = 'idea_board'
    DB_HOST = url.hostname

""" Put Production Specific Configurations here """
class ProductionDBConfig(DBConfig):
    DB_USERNAME = url.username
    DB_PASSWORD = url.password
    DB_DATABASE_NAME = 'idea_board'
    DB_HOST = url.hostname

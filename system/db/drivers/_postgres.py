import psycopg2
import psycopg2.extras
import urlparse
import collections
import os

def _convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(_convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        print data
        return data
        # return type(data)(map(_convert, data))
    else:
        return data

class MySQLConnection(object):
    def __init__(self, config):
        urlparse.uses_netloc.append("postgres")
        url = urlparse.urlparse(os.environ["DATABASE_URL"])



        self.conn = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )

    def query_db(self, query, data=None):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        data = cursor.execute(query, data)
        if query[0:6].lower() != 'select':
            self.conn.commit()
            return
        else:
            result = list(cursor.fetchall())
            return _convert(result)

def connect(config):
    return MySQLConnection(config)

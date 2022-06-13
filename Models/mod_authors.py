from peewee import CharField , Model , PrimaryKeyField
from database_con.db_config import db

class Author(Model):

    author_id = PrimaryKeyField(unique= True)
    name = CharField()
    links = CharField()

    class Meta():
        database = db
        db_table = 'Author'
        order_by = 'author_id'
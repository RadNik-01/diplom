from peewee import ForeignKeyField , Model , PrimaryKeyField
from database_con.db_config import db
from Models.mod_article import Article
from Models.mod_authors import Author

class Auth_Art(Model):

    record_id = PrimaryKeyField(unique=True)
    author_id = ForeignKeyField(Author, backref="Auth_Art")
    art_id = ForeignKeyField(Article, backref="Auth_Art")

    class Meta():
        order_by = 'record_id'
        database = db
        db_table = 'Auth_Art'


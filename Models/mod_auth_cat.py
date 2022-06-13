from peewee import ForeignKeyField , Model , PrimaryKeyField
from database_con.db_config import db
from Models.mod_categories import Category
from Models.mod_authors import Author

class Auth_Cat(Model):

    record_id = PrimaryKeyField(unique= True)
    author_id = ForeignKeyField(Author, backref="Auth_Cat")
    cat_id = ForeignKeyField(Category, backref="Auth_Cat")

    class Meta():
        database = db
        db_table = 'Auth_Cat'
        order_by = 'record_id'
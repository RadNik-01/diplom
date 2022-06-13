from peewee import CharField , Model , PrimaryKeyField
from database_con.db_config import db

class Category(Model):

    cat_id = PrimaryKeyField(unique= True)
    cat_name = CharField()

    class Meta():
        database = db
        db_table = 'Category'
        order_by = 'cat_id'

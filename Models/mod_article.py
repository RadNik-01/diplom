from peewee import CharField , Model ,DateField , TextField , PrimaryKeyField
from database_con.db_config import db

class Article(Model):

    art_id = PrimaryKeyField(unique= True)
    title = CharField()
    authors = CharField()
    abstract = TextField()
    pub_date = DateField()
    categories = CharField()

    class Meta():
        database = db
        db_table = 'Article'
        order_by = 'pub_date'
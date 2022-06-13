from peewee import ForeignKeyField, Model, PrimaryKeyField
from database_con.db_config import db
from Models.mod_article import Article
from Models.mod_categories import Category

class Art_Cat(Model):

    record_id = PrimaryKeyField(unique= True)
    art_id = ForeignKeyField(Article, backref="Art_cat")
    cat_id = ForeignKeyField(Category, backref="Art_cat")

    class Meta():
        database = db
        db_table = 'Art_cat'
        order_by = 'record_id'
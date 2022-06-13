from Models.mod_auth_cat import Auth_Cat
from Models.mod_con_art_auth import Auth_Art
from Models.mod_article import Article
from Models.mod_authors import Author
from Models.mod_categories import Category
from Models.mod_art_cat import  Art_Cat
from database_con.db_config import db


def create_new_database():
    db.connect()
    db.create_tables([Article, Author, Category, Auth_Art, Art_Cat, Auth_Cat])
    db.commit()
    db.close()

def connect_to_database():
    db.connect()
    print('connected')

def commit_database():
    db.commit()
    print('changes was saved')

def disconect_database():
    print('exit')
    db.close()

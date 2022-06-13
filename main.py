import os
import shutil

from datetime import datetime


import op_arxiv
import op_scholar

from database_con.db_simple_op import *
from database_con.db_config import db_standart_path , db_record_path ,db_session_path


def db_checker():
        path = db_standart_path
        if (os.path.exists(path)):
            pass
        else:
            if (os.path.exists('db')):
                create_new_database()
            else:
                os.mkdir('db')
                create_new_database()

def record_saver(file_name):
    extension = ".db"
    if(len(file_name) < 3):
        record_time = datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
        record = "Record-"
        timer = str(record_time)
        new_record_path = db_record_path + record + timer + extension
    else:
        record = file_name
        new_record_path = db_record_path + record + extension
    file_oldname = os.path.join(db_standart_path)
    file_newname_newfile = os.path.join(new_record_path)
    shutil.copy(file_oldname, file_newname_newfile)

def session_saver():
    record_time = datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
    timer = str(record_time)
    extension = ".db"
    new_record_path = db_session_path + timer + extension
    file_oldname = os.path.join(db_standart_path)
    file_newname_newfile = os.path.join(new_record_path)
    shutil.copy(file_oldname, file_newname_newfile)

def searched_by_title_arx(user_parametr,user_max_res):
    parametr = user_parametr
    search_amount = user_max_res

    res_arx_count = op_arxiv.searched_by_title_func(parametr, search_amount)
    print(res_arx_count)
    commit_database()

def searched_by_title_sch(user_parametr,user_max_res):
    parametr = user_parametr
    search_amount = user_max_res

    res_sch_count = op_scholar.search_by_keyword(parametr, search_amount)
    print(res_sch_count)
    commit_database()

def searched_by_author_arx(user_parametr,user_max_res):

    parametr= user_parametr
    search_amount = user_max_res
    res_arx_count = op_arxiv.searcher_authors(parametr,search_amount)
    print(res_arx_count)
    commit_database()

def searched_by_author_sch(user_parametr,user_max_res):
    parametr = user_parametr
    op_scholar.author_searcher(parametr,user_max_res)
    #op_scholar.search_author(parametr)
    commit_database()

def searched_by_category_arx(user_parametr,user_max_res):

    parametr= user_parametr
    search_amount = user_max_res

    res_arx_count = op_arxiv.searched_by_category(parametr, search_amount)
    print(res_arx_count)
    commit_database()






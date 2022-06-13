import arxiv

from Models.mod_article import Article
from Models.mod_authors import Author
from Models.mod_categories import Category

from Models.mod_auth_cat import Auth_Cat
from Models.mod_art_cat import Art_Cat
from Models.mod_con_art_auth import Auth_Art
from database_con.db_config import db


def searcher(parametr,search_amount,search_category):
    res_count = 0
    platform = "Cornell University Library (arXiv) article: "
    searching = search_category + parametr
    search = arxiv.Search(
        query = searching,
        max_results = search_amount,
        sort_by=arxiv.SortCriterion.Relevance
    )
    for result in search.results():
        res_count += 1
        authors_list = []
        raw_title = result.title
        raw_year = result.published
        raw_year = raw_year.year
        raw_category = result.primary_category
        for author in result.authors:
            authors_list.append(str(author))
        raw_authors = ', '.join(authors_list)
        raw_abstract = result.summary

        art_title_check = None

        art_check = (Article.select(Article.title).where((Article.title == raw_title) & (Article.authors == raw_authors)))
        for r in art_check:
            art_title_check = r

        if (art_title_check == None):
            record_articles = Article.create(title=raw_title,
                                             authors=raw_authors,
                                             abstract= raw_abstract,
                                             pub_date=raw_year,
                                             categories=raw_category)
            record_articles.save()
            db.commit()

        for authors in authors_list:
            info = platform + result.entry_id

            author_check = None

            aut_check = (Author.select(Author.name).where(Author.name == authors))
            for r in aut_check:
                author_check = r

            if (author_check == None):

                record_author = Author.create(name=authors, links=info)
                record_author.save()

            cat_check = None
            cat_recheck = (Category.select(Category.cat_name).where(Category.cat_name == raw_category))

            for r in cat_recheck:
                cat_check = r

            if (cat_check == None):

                record_cat = Category.create(cat_name=raw_category)
                record_cat.save()

        for authors in authors_list:

            query_art_id_extr = (Article.select(Article.art_id).where(Article.title == raw_title))
            for id in query_art_id_extr:
                raw_art_id = id.art_id

            query_auth_id_extr = (Author.select(Author.author_id).where(Author.name == authors))

            for id in query_auth_id_extr:
                raw_auth_id = id.author_id

            query_auth_id_extr = (Category.select(Category.cat_id).where(Category.cat_name == raw_category))

            for id in query_auth_id_extr:
                raw_cat_id = id.cat_id

            aut_cat_check = None

            aut_cat = (Auth_Cat.select(Auth_Cat.record_id).where((Auth_Cat.author_id == raw_auth_id) & (Auth_Cat.cat_id == raw_cat_id)))
            for r in aut_cat:
                aut_cat_check = r

            if (aut_cat_check == None):
                record_Auth_cat = Auth_Cat.create(author_id=raw_auth_id, cat_id=raw_cat_id)
                record_Auth_cat.save()

            art_cat_check = None

            art_cat = (Art_Cat.select(Art_Cat.record_id).where((Art_Cat.art_id == raw_art_id) & (Art_Cat.cat_id == raw_cat_id)))
            for r in art_cat:
                art_cat_check = r

            if (art_cat_check == None):
                record_Art_cat = Art_Cat.create(art_id=raw_art_id, cat_id=raw_cat_id)
                record_Art_cat.save()

            auth_art_check = None

            auth_art = (Auth_Art.select(Auth_Art.record_id).where((Auth_Art.art_id == raw_art_id) & (Auth_Art.author_id == raw_auth_id)))

            for r in auth_art:
                auth_art_check = r

            if (auth_art_check == None):
                record_Auth_Art = Auth_Art.create(author_id=raw_auth_id, art_id=raw_art_id)
                record_Auth_Art.save()
    return(res_count)

def searched_by_title_func(parametr,search_amount):
    search_category = "ti:"
    res_count =searcher(parametr,search_amount,search_category)
    return (res_count)

def searched_by_category(parametr,search_amount):
    search_category = "cat:"
    res_count = searcher(parametr, search_amount, search_category)
    return (res_count)

def searcher_authors(parametr,search_amount):
    res_count = 0
    platform = "Cornell University Library (arXiv) article: "
    search_category = "au:"
    searching = search_category + parametr
    search = arxiv.Search(
        query = searching,
        max_results = search_amount,
        sort_by=arxiv.SortCriterion.Relevance
    )
    for result in search.results():
        res_count += 1
        authors_list = []
        raw_title = result.title
        raw_year = result.published
        raw_year = raw_year.year
        raw_category = result.primary_category
        for author in result.authors:
            authors_list.append(str(author))
        raw_authors = ', '.join(authors_list)
        raw_abstract = result.summary

        art_title_check = None

        art_check = (Article.select(Article.title).where((Article.title == raw_title) & (Article.authors == raw_authors)))
        for r in art_check:
            art_title_check = r

        if (art_title_check == None):
            record_articles = Article.create(title=raw_title,
                                             authors=raw_authors,
                                             abstract= raw_abstract,
                                             pub_date=raw_year,
                                             categories=raw_category)
            record_articles.save()



        for authors in authors_list:
            info = platform + result.entry_id

            author_check = None

            aut_check = (Author.select(Author.name).where(Author.name == authors))
            for r in aut_check:
                author_check = r

            if (author_check == None):

                record_author = Author.create(name=authors, links=info)
                record_author.save()

            cat_check = None
            aut_check = (Category.select(Category.cat_name).where(Category.cat_name == raw_category))

            for r in aut_check:
                cat_check = r

            if (cat_check == None):

                record_cat = Category.create(cat_name=raw_category)
                record_cat.save()




        for authors in authors_list:

            query_art_id_extr = (Article.select(Article.art_id).where(Article.title == raw_title))
            for id in query_art_id_extr:
                raw_art_id = id.art_id

            query_auth_id_extr = (Author.select(Author.author_id).where(Author.name == authors))

            for id in query_auth_id_extr:
                raw_auth_id = id.author_id

            query_auth_id_extr = (Category.select(Category.cat_id).where(Category.cat_name == raw_category))

            for id in query_auth_id_extr:
                raw_cat_id = id.cat_id


            aut_cat_check = None

            aut_cat = (Auth_Cat.select(Auth_Cat.record_id).where((Auth_Cat.author_id == raw_auth_id) & (Auth_Cat.cat_id == raw_cat_id)))
            for r in aut_cat:
                aut_cat_check = r

            if (aut_cat_check == None):
                record_Auth_cat = Auth_Cat.create(author_id=raw_auth_id, cat_id=raw_cat_id)
                record_Auth_cat.save()


            art_cat_check = None

            art_cat = (Art_Cat.select(Art_Cat.record_id).where((Art_Cat.art_id == raw_art_id) & (Art_Cat.cat_id == raw_cat_id)))
            for r in art_cat:
                art_cat_check = r

            if (art_cat_check == None):
                record_Art_cat = Art_Cat.create(art_id=raw_art_id, cat_id=raw_cat_id)
                record_Art_cat.save()



            auth_art_check = None

            auth_art = (Auth_Art.select(Auth_Art.record_id).where((Auth_Art.art_id == raw_art_id) & (Auth_Art.author_id == raw_auth_id)))

            for r in auth_art:
                auth_art_check = r

            if (auth_art_check == None):
                record_Auth_Art = Auth_Art.create(author_id=raw_auth_id, art_id=raw_art_id)
                record_Auth_Art.save()
    return (res_count)

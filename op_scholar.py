import scholarly
from scholarly import ProxyGenerator
from scholarly import scholarly

from Models.mod_authors import Author
from Models.mod_article import Article
from Models.mod_categories import Category

from Models.mod_auth_cat import Auth_Cat
from Models.mod_art_cat import Art_Cat
from Models.mod_con_art_auth import Auth_Art

from database_con.db_config import sch_key, db

pg = ProxyGenerator()
success = pg.ScraperAPI(str(sch_key))
scholarly.use_proxy(pg)

def search_by_keyword(parametr,search_amount):
    res_count = 0
    pub_Links_separ = "  "
    raw_cat = "Category unknown"
    search_query = scholarly.search_pubs(parametr)
    search_number = 0
    for res in search_query:
        res_count += 1
        search_number += 1
        if search_number == search_amount:
            break
        else:
            authors_list = []
            authors_id = []


            result_text = res['bib']
            raw_title = result_text['title']
            raw_abstract = result_text['abstract']
            raw_year = result_text['pub_year']
            raw_category = raw_cat

            result_author_id = res['author_id']
            result_author = result_text['author']
            for item in result_author:
                authors_list.append(item)

            for item in result_author_id:
                link = "no Author Account link"
                if (item !=("")):
                    lin = "Google Scholar Author Account link: https://scholar.google.com/citations?hl=uk&user="
                    link = lin + item
                    authors_id.append(link)
                else:
                    authors_id.append(link)
            i = 0
            while (i < len(authors_list)):
                author_data = authors_list[i]
                auth_acc_link = (authors_id[i])

                author_check = None

                aut_check = (Author.select(Author.name).where(Author.name == author_data))
                for r in aut_check:
                    author_check = r

                if (author_check == None):
                    links = auth_acc_link + pub_Links_separ
                    record_author = Author.create(name=author_data, links=links)
                    record_author.save()
                i += 1

            raw_authors = ', '.join(authors_list)

            art_title_check = None

            art_check = (Article.select(Article.title).where((Article.title == raw_title) & (Article.authors == raw_authors)))
            for r in art_check:
                art_title_check = r

            if (art_title_check == None):
                record_articles = Article.create(title=raw_title,
                                                 authors=raw_authors,
                                                 abstract=raw_abstract,
                                                 pub_date=raw_year,
                                                 categories=raw_category)
                record_articles.save()
                db.commit()

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

            aut_cat = (Auth_Cat.select(Auth_Cat.record_id).where(
                (Auth_Cat.author_id == raw_auth_id) & (Auth_Cat.cat_id == raw_cat_id)))
            for r in aut_cat:
                aut_cat_check = r

            if (aut_cat_check == None):
                record_Auth_cat = Auth_Cat.create(author_id=raw_auth_id, cat_id=raw_cat_id)
                record_Auth_cat.save()

            art_cat_check = None

            art_cat = (Art_Cat.select(Art_Cat.record_id).where(
                (Art_Cat.art_id == raw_art_id) & (Art_Cat.cat_id == raw_cat_id)))
            for r in art_cat:
                art_cat_check = r

            if (art_cat_check == None):
                record_Art_cat = Art_Cat.create(art_id=raw_art_id, cat_id=raw_cat_id)
                record_Art_cat.save()

            auth_art_check = None

            auth_art = (Auth_Art.select(Auth_Art.record_id).where(
                (Auth_Art.art_id == raw_art_id) & (Auth_Art.author_id == raw_auth_id)))

            for r in auth_art:
                auth_art_check = r

            if (auth_art_check == None):
                record_Auth_Art = Auth_Art.create(author_id=raw_auth_id, art_id=raw_art_id)
                record_Auth_Art.save()
    return (res_count)

def search_author(parameter):
    res_count = 0
    search_query = scholarly.search_author(parameter)
    for res in search_query:
        res_count += 1
        link = "Google Scholar Author Account link: https://scholar.google.com/citations?hl=uk&user="
        auth_id = res['scholar_id']
        links = link + auth_id
        names = res['name']
        interest_list = res['interests']

        author_check = None
        aut_check = (Author.select(Author.name).where(Author.name == names))
        for r in aut_check:
            author_check = r

        if (author_check == None):
            record_author = Author.create(name=names, links=links)
            record_author.save()
            for el in interest_list:
                cat_check = None
                aut_check = (Category.select(Category.cat_name).where(Category.cat_name == el))

                for r in aut_check:
                    cat_check = r
                if (cat_check == None):
                    record_cat = Category.create(cat_name=el)
                    record_cat.save()

                    query_auth_id_extr = (Author.select(Author.author_id).where(Author.name == names))

                    for id in query_auth_id_extr:
                        raw_auth_id = id.author_id

                    query_auth_id_extr = (Category.select(Category.cat_id).where(Category.cat_name == el))

                    for id in query_auth_id_extr:
                        raw_cat_id = id.cat_id

                    aut_cat_check = None

                    aut_cat = (Auth_Cat.select(Auth_Cat.record_id).where(
                        (Auth_Cat.author_id == raw_auth_id) & (Auth_Cat.cat_id == raw_cat_id)))
                    for r in aut_cat:
                        aut_cat_check = r

                    if (aut_cat_check == None):
                        record_Auth_cat = Auth_Cat.create(author_id=raw_auth_id, cat_id=raw_cat_id)
                        record_Auth_cat.save()

def author_searcher(parameter, max_res):
    res_count = 0
    search_query = scholarly.search_author(parameter)
    for res in search_query:
        res_count += 1
        if(res_count == max_res):
            break
        else:
            raw_category = "Category unknown"
            raw_authors = res["name"]
            link_id = res["scholar_id"]
            link_pre = "Google Scholar Author Account link: https://scholar.google.com/citations?hl=uk&user="
            link = link_pre + link_id
            filled_author = scholarly.fill(res, sections=["publications"])
            pubs = filled_author["publications"]

            author_check = None

            aut_check = (Author.select(Author.name).where(Author.name == raw_authors))
            for r in aut_check:
                author_check = r

            if (author_check == None):
                links = link
                record_author = Author.create(name=raw_authors, links=links)
                record_author.save()

            for p in pubs:
                r = p["bib"]
                raw_title = (r["title"])
                try:
                    raw_year = (r["pub_year"])
                except KeyError:
                    raw_year = "1111"

                art_title_check = None

                art_check = (
                    Article.select(Article.title).where((Article.title == raw_title) & (Article.authors == raw_authors)))
                for r in art_check:
                    art_title_check = r

                if (art_title_check == None):
                    record_articles = Article.create(title=raw_title,
                                                     authors=raw_authors,
                                                     pub_date=raw_year,
                                                     categories=raw_category)
                    record_articles.save()
                    db.commit()

                cat_check = None
                aut_check = (Category.select(Category.cat_name).where(Category.cat_name == raw_category))

                for r in aut_check:
                    cat_check = r

                if (cat_check == None):
                    record_cat = Category.create(cat_name=raw_category)
                    record_cat.save()

                query_art_id_extr = (Article.select(Article.art_id).where(Article.title == raw_title))
                for id in query_art_id_extr:
                    raw_art_id = id.art_id

                query_auth_id_extr = (Author.select(Author.author_id).where(Author.name == raw_authors))

                for id in query_auth_id_extr:
                    raw_auth_id = id.author_id

                query_auth_id_extr = (Category.select(Category.cat_id).where(Category.cat_name == raw_category))

                for id in query_auth_id_extr:
                    raw_cat_id = id.cat_id

                aut_cat_check = None

                aut_cat = (Auth_Cat.select(Auth_Cat.record_id).where(
                    (Auth_Cat.author_id == raw_auth_id) & (Auth_Cat.cat_id == raw_cat_id)))
                for r in aut_cat:
                    aut_cat_check = r

                if (aut_cat_check == None):
                    record_Auth_cat = Auth_Cat.create(author_id=raw_auth_id, cat_id=raw_cat_id)
                    record_Auth_cat.save()

                art_cat_check = None

                art_cat = (Art_Cat.select(Art_Cat.record_id).where(
                    (Art_Cat.art_id == raw_art_id) & (Art_Cat.cat_id == raw_cat_id)))
                for r in art_cat:
                    art_cat_check = r

                if (art_cat_check == None):
                    record_Art_cat = Art_Cat.create(art_id=raw_art_id, cat_id=raw_cat_id)
                    record_Art_cat.save()

                auth_art_check = None

                auth_art = (Auth_Art.select(Auth_Art.record_id).where(
                    (Auth_Art.art_id == raw_art_id) & (Auth_Art.author_id == raw_auth_id)))

                for r in auth_art:
                    auth_art_check = r

                if (auth_art_check == None):
                    record_Auth_Art = Auth_Art.create(author_id=raw_auth_id, art_id=raw_art_id)
                    record_Auth_Art.save()


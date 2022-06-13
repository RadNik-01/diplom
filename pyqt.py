import table_model
from main import *
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, qApp, QHeaderView, QInputDialog
import Menu


class Form(QtWidgets.QMainWindow, Menu.Ui_MainWindow):
    def __init__(self):
        db_checker()
        connect_to_database()
        super(Form, self).__init__()
        self.setupUi(self)
        self.Search_button.clicked.connect(self.inputdata)
        self.Save_session.clicked.connect(self.save_session)
        self.Save_record.clicked.connect(self.save_record)
        self.Refresh_info.clicked.connect(self.tabled_selector)
        self.tabled_articles()
        self.categories = {
'Astrophysics of Galaxies' : 'astro-ph.GA',
'Cosmology and Nongalactic Astrophysics': 'astro-ph.CO',
'Earth and Planetary Astrophysics': 'astro-ph.EP',
'High Energy Astrophysical Phenomena': 'astro-ph.HE',
'Instrumentation and Methods for Astrophysics': 'astro-ph.IM',
'Solar and Stellar Astrophysics':'astro-ph.SR' ,
'Disordered Systems and Neural Networks': 'cond-mat.dis-nn' ,
'Materials Science': 'cond-mat.mtrl-sci',
'Mesoscale and Nanoscale Physics' :'cond-mat.mes-hall' ,
'Other Condensed Matter': 'cond-mat.other' ,
'Quantum Gases': 'cond-mat.quant-gas' ,
'Soft Condensed Matter': 'cond-mat.soft',
'Statistical Mechanics': 'cond-mat.stat-mech',
'Strongly Correlated Electrons':'cond-mat.str-el',
'Superconductivity':'cond-mat.supr-con',
'General Relativity and Quantum Cosmology':'gr-qc',
'High Energy Physics - Experiment':'hep-ex' ,
'High Energy Physics - Lattice':'hep-lat',
'High Energy Physics - Phenomenology': 'hep-ph',
'High Energy Physics - Theory':'hep-th',
'Mathematical Physics':'math-ph',
'Adaptation and Self-Organizing Systems':'nlin.AO',
'Cellular Automata and Lattice Gases':'nlin.CG',
'Chaotic Dynamics': 'nlin.CD',
'Exactly Solvable and Integrable Systems': 'nlin.SI' ,
'Pattern Formation and Solitons': 'nlin.PS',
'Nuclear Experiment': 'nucl-ex',
'Nuclear Theory': 'nucl-th',
'Accelerator Physics': 'physics.acc-ph',
'Applied Physics': 'physics.app-ph',
'Atmospheric and Oceanic Physics':'physics.ao-ph' ,
'physics.atom-ph': 'Atomic Physics',
'Atomic and Molecular Clusters': 'physics.atm-clus',
'Biological Physics': 'physics.bio-ph' ,
'Chemical Physics': 'physics.chem-ph',
'Classical Physics': 'physics.class-ph',
'Computational Physics': 'physics.comp-ph',
'Data Analysis, Statistics and Probability':'physics.data-an' ,
'Fluid Dynamics': 'physics.flu-dyn',
'General Physics': 'physics.gen-ph',
'Geophysics':'physics.geo-ph',
'History and Philosophy of Physics':'physics.hist-ph' ,
'Instrumentation and Detectors':'physics.ins-det',
'Medical Physics':'physics.med-ph',
'Optics': 'physics.optics',
'Physics Education': 'physics.ed-ph' ,
'Physics and Society':'physics.soc-ph' ,
'Plasma Physics': 'physics.plasm-ph',
'Popular Physics':'physics.pop-ph' ,
'Space Physics': 'physics.space-ph',
'Quantum Physics': 'quant-ph' ,

'Algebraic Geometry': 'math.AG',
'Algebraic Topology': 'math.AT' ,
'Analysis of PDEs': 'math.AP' ,
'Category Theory': 'math.CT',
'Classical Analysis and ODEs':'math.CA' ,
'Combinatorics': 'math.CO',
'Commutative Algebra': 'math.AC' ,
'Complex Variables': 'math.CV',
'Differential Geometry': 'math.DG',
'Dynamical Systems': 'math.DS' ,
'Functional Analysis': 'math.FA',
'General Mathematics': 'math.GM',
'General Topology': 'math.GN' ,
'Geometric Topology': 'math.GT',
'Group Theory': 'math.GR',
'History and Overview': 'math.HO' ,
'Information Theory':'math.IT' ,
'K-Theory and Homology': 'math.KT' ,
'Logic': 'math.LO' ,
'Mathematical Physics': 'math.MP',
'Metric Geometry': 'math.MG',
'Number Theory': 'math.NT',
'Numerical Analysis': 'math.NA',
'Operator Algebras':'math.OA' ,
'Optimization and Control': 'math.OC',
'Probability': 'math.PR',
'Quantum Algebra': 'math.QA',
'Representation Theory':'math.RT' ,
'Rings and Algebras': 'math.RA',
'Spectral Theory':'math.SP' ,

'Artificial Intelligence': 'cs.AI',
'Computation and Language': 'cs.CL' ,
'Computational Complexity': 'cs.CC',
'Computational Engineering, Finance, and Science':'cs.CE',
'Computational Geometry': 'cs.CG' ,
'Computer Science and Game Theory': 'cs.GT',
'Computer Vision and Pattern Recognition': 'cs.CV',
'Computers and Society': 'cs.CY' ,
'Cryptography and Security': 'cs.CR',
'Data Structures and Algorithms': 'cs.DS' ,
'Databases': 'cs.DB',
'Digital Libraries': 'cs.DL',
'Discrete Mathematics': 'cs.DM',
'Distributed, Parallel, and Cluster Computing': 'cs.DC' ,
'Emerging Technologies': 'cs.ET',
'Formal Languages and Automata Theory': 'cs.FL' ,
'General Literature': 'cs.GL' ,
'Graphics': 'cs.GR' ,
'Hardware Architecture': 'cs.AR',
'Human-Computer Interaction': 'cs.HC' ,
'Information Retrieval':  'cs.IR',
'Information Theory': 'cs.IT' ,
'Learning': 'cs.LG',
'Logic in Computer Science': 'cs.LO' ,
'Mathematical Software': 'cs.MS' ,
'Multiagent Systems': 'cs.MA' ,
'Multimedia': 'cs.MM' ,
'Networking and Internet Architecture': 'cs.NI',
'Neural and Evolutionary Computing': 'cs.NE',
'Numerical Analysis': 'cs.NA',

'Biomolecules': 'q-bio.BM',
'Genomics': 'q-bio.GN',
'Molecular Networks': 'q-bio.MN' ,
'Subcellular Processes': 'q-bio.SC',
'Cell Behavior': 'q-bio.CB',
'Neurons and Cognition': 'q-bio.NC',
'Tissues and Organs':'q-bio.TO' ,
'Populations and Evolution': 'q-bio.PE' ,
'Quantitative Methods': 'q-bio.QM',
'Other': 'q-bio.OT',

'Pricing of Securities': 'q-fin.PR',
'Risk Management': 'q-fin.RM' ,
'Portfolio Management':'q-fin.PM',
'Trading and Microstructure': 'q-fin.TR',
'Mathematical Finance': 'q-fin.MF',
'Computational Finance':'q-fin.CP' ,
'Statistical Finance': 'q-fin.ST' ,
'General Finance': 'q-fin.GN' ,
'Economics': 'q-fin.EC' ,

'Applications': 'stat.AP',
'Computation': 'stat.CO',
'Machine Learning': 'stat.ML',
'Methodology': 'stat.ME' ,
'Other Statistics': 'stat.OT',
'Theory': 'stat.TH',
}
        self.Category_box.addItems(self.categories.keys())
        self.Search_by_box.currentTextChanged.connect(self.categ_ch)

    def inputdata(self):
        self.Save_record.setEnabled(False)
        self.Save_session.setEnabled(False)
        self.Search_button.setEnabled(False)
        try:
            if(self.Parametr_line.text() == ""):
                parameter = "No"
            else:
                parameter = self.Parametr_line.text()

            if (self.Category_box.currentText() == ""):
                category = "Nothing"
            else:
                category = self.categories[str(self.Category_box.currentText())]

            max_res = int(self.Max_results_box.value())
            search_by = self.Search_by_box.currentText()
            qApp.processEvents()

            if not self.CheckBox_Arxiv.isChecked() and not self.Check_box_goo_sch.isChecked():
                error = QMessageBox()
                error.setText("resourse wasnt picked at all")
                error.setStandardButtons(QMessageBox.Ok)
                error.exec()
            elif self.CheckBox_Arxiv.isChecked() and not self.Check_box_goo_sch.isChecked():
                if search_by == "Title":
                    if (parameter == "No") or (len(parameter) < 3):
                        error = QMessageBox()
                        error.setText("Parameter has no data")
                        error.setStandardButtons(QMessageBox.Ok)
                        error.exec()
                    else:
                        error = QMessageBox()
                        error.setText("Search has been finished")
                        error.setStandardButtons(QMessageBox.Ok)
                        searched_by_title_arx(parameter, max_res)
                        error.exec()
                elif search_by == "Category":
                    if (category == "Nothing"):
                        error = QMessageBox()
                        error.setText("Category wasnt picked")
                        error.setStandardButtons(QMessageBox.Ok)
                        error.exec()
                    else:
                        error = QMessageBox()
                        error.setText("Search has been finished")
                        error.setStandardButtons(QMessageBox.Ok)
                        searched_by_category_arx(category, max_res)
                        error.exec()
                elif search_by == "Author":
                    if (parameter == "No") or (len(parameter) < 3):
                        error = QMessageBox()
                        error.setText("Parameter has no data")
                        error.setStandardButtons(QMessageBox.Ok)
                        error.exec()
                    else:
                        error = QMessageBox()
                        error.setText("Search has been finished")
                        error.setStandardButtons(QMessageBox.Ok)
                        searched_by_author_arx(parameter, max_res)
                        error.exec()
                else:
                    error = QMessageBox()
                    error.setText("Search_by wasn`t picked")
                    error.setStandardButtons(QMessageBox.Ok)
                    error.exec()

            elif not self.CheckBox_Arxiv.isChecked() and self.Check_box_goo_sch.isChecked():
                if search_by == "Title":
                    if (parameter == "No") or (len(parameter) < 3):
                        error = QMessageBox()
                        error.setText("Parameter has no data")
                        error.setStandardButtons(QMessageBox.Ok)
                        error.exec()
                    else:
                        error = QMessageBox()
                        error.setText("Search has been finished")
                        error.setStandardButtons(QMessageBox.Ok)
                        searched_by_title_sch(parameter, max_res)
                        error.exec()

                elif search_by == "Author":
                    if (parameter == "No") or (len(parameter) < 3):
                        error = QMessageBox()
                        error.setText("Parameter has no data")
                        error.setStandardButtons(QMessageBox.Ok)
                        error.exec()
                    else:
                        error = QMessageBox()
                        error.setText("Search has been finished")
                        error.setStandardButtons(QMessageBox.Ok)
                        searched_by_author_sch(parameter, max_res)
                        error.exec()
                else:
                    error = QMessageBox()
                    error.setText("Search_by wasn`t picked")
                    error.setStandardButtons(QMessageBox.Ok)
                    error.exec()
            elif self.CheckBox_Arxiv.isChecked() and self.Check_box_goo_sch.isChecked():
                if search_by == "Title":
                    if (parameter == "No") or (len(parameter) < 3):
                        error = QMessageBox()
                        error.setText("Parameter has no data")
                        error.setStandardButtons(QMessageBox.Ok)
                        error.exec()
                    else:
                        error = QMessageBox()
                        error.setText("Search has been finished")
                        error.setStandardButtons(QMessageBox.Ok)
                        searched_by_title_arx(parameter, max_res)
                        searched_by_title_sch(parameter, max_res)
                        error.exec()
                elif search_by == "Author":
                    if (parameter == "No") or (len(parameter) < 3):
                        error = QMessageBox()
                        error.setText("Parameter has no data")
                        error.setStandardButtons(QMessageBox.Ok)
                        error.exec()
                    else:
                        error = QMessageBox()
                        error.setText("Search has been finished")
                        error.setStandardButtons(QMessageBox.Ok)
                        searched_by_author_sch(parameter, max_res)
                        searched_by_author_arx(parameter, max_res)
                        error.exec()
                elif search_by == "Category":
                    if (category == "Nothing"):
                        error = QMessageBox()
                        error.setText("Category wasnt picked")
                        error.setStandardButtons(QMessageBox.Ok)
                        error.exec()
                    else:
                        error = QMessageBox()
                        error.setText("Search has been finished")
                        error.setStandardButtons(QMessageBox.Ok)
                        searched_by_category_arx(category, max_res)
                        error.exec()
                else:
                    error = QMessageBox()
                    error.setText("Search_by wasn`t picked")
                    error.setStandardButtons(QMessageBox.Ok)
                    error.exec()
        except Exception as err:
            print(err)

        self.Save_session.setEnabled(True)
        self.Save_record.setEnabled(True)
        self.Search_button.setEnabled(True)

    def save_session(self):
        self.Save_record.setEnabled(False)
        self.Save_session.setEnabled(False)
        self.Search_button.setEnabled(False)
        session_saver()
        disconect_database()
        App.exit(0)

    def save_record(self):
        self.Save_record.setEnabled(False)
        self.Save_session.setEnabled(False)
        self.Search_button.setEnabled(False)
        text, ok = QInputDialog.getText(self,'Name your saving file', 'Name of your record')
        if ok:
            file_name = str(text)
            record_saver(file_name)
        self.Save_session.setEnabled(True)
        self.Save_record.setEnabled(True)
        self.Search_button.setEnabled(True)

    def tabled_selector(self):
        if(self.Combo_table_select.currentText() == "Articles"):
            self.tabled_articles()
        elif(self.Combo_table_select.currentText() == "Categories"):
            self.tabled_category()
        elif(self.Combo_table_select.currentText() == "Authors"):
            self.tabled_author()
        else:
            print("ERROR")

    def tabled_articles(self):
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        articles = Article.select().tuples()
        model = table_model.Article_TableModel(articles)
        self.tableView.setModel(model)

    def tabled_category(self):
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        category = Category.select().tuples()
        model = table_model.Category_TableModel(category)
        self.tableView.setModel(model)

    def tabled_author(self):
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        authors = Author.select().tuples()
        model = table_model.Authors_TableModel(authors)
        self.tableView.setModel(model)

    def categ_ch(self):
        if(self.Search_by_box.currentText() == "Title"):
            self.Label_Searching_parametr.show()
            self.Parametr_line.show()
            self.Label_category.hide()
            self.Category_box.hide()
            self.Check_box_goo_sch.show()

        elif(self.Search_by_box.currentText() == "Author"):
            self.Label_Searching_parametr.show()
            self.Parametr_line.show()
            self.Label_category.hide()
            self.Category_box.hide()
            self.Check_box_goo_sch.show()

        elif (self.Search_by_box.currentText() == "Category"):
            self.Category_box.show()
            self.Label_category.show()
            self.Label_Searching_parametr.hide()
            self.Parametr_line.hide()
            self.Check_box_goo_sch.hide()

        else:
            self.Label_Searching_parametr.show()
            self.Label_category.show()
            self.Label_Search_by.show()
            self.Check_box_goo_sch.show()
            self.Parametr_line.show()
            self.Category_box.show()
            self.Check_box_goo_sch.show()

App = QtWidgets.QApplication(sys.argv)
window = Form()
window.show()
App.exec()



















import fonctions_db


class Emprunt(object):
	def __init__(self, code_liv, cursor=None, stop=1, livre=None):
		if cursor == None:
			conn, cursor = fonctions_db.connect_db()
		if livre == None:
			livre = fonctions_db.execute_query(conn if conn else None, cursor,
			                                    f"""SELECT * FROM livre WHERE Code_Liv = '{code_liv}' """,
			                                    is_result=True)
		self.Code_Liv, self.Titre, self.Auteur, self.Genre, self.Prix = livre[0], livre[1], livre[2], livre[3], livre[4]

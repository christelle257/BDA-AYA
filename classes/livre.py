import fonctions_db


class Livre(object):
	def __init__(self, code_liv, cursor=None, stop=1, livre=None):
		if cursor == None:
			conn, cursor = fonctions_db.connect_db()
		if livre == None:
			livre = fonctions_db.execute_query(conn if conn else None, cursor,
			                                    f"""SELECT * FROM livre WHERE Code_Liv = '{code_liv}' """,
			                                    is_result=True)
		self.Code_Liv, self.Titre, self.Auteur, self.Genre, self.Prix = livre[0], livre[1], livre[2], livre[3], livre[4]

	@classmethod
	def create(cls, livre: tuple):
		conn, cursor = fonctions_db.connect_db()
		fonctions_db.execute_query(conn, cursor,
		                           f"""insert into livre (Code_Liv, Titre, Auteur, Genre, Prix) VALUES (%s ,%s, %s, %s, %s)""",
		                           livre)
		return cls(conn.insert_id(), cursor=cursor)

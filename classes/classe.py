import fonctions_db

class Classe(object):
	def __init__(self, code_cl, cursor=None, stop=1, classe=None, eleve=None):
		if cursor == None:
			conn, cursor = fonctions_db.connect_db()
		if classe == None:
			classe = fonctions_db.execute_query(conn if conn else None, cursor, f"""SELECT * FROM classe WHERE Code_Cl = '{code_cl}' """,is_result=True)
		self.Code_Cl, self.Intitule, self.Effectif = classe[0], classe[1], classe[2]

	@classmethod
	def create(cls, classe: tuple):
		conn, cursor = fonctions_db.connect_db()
		fonctions_db.execute_query(conn, cursor,
		                           f"""insert into classe (Code_Cl, Intitule, Effectif) VALUES (%s ,%s, %s)""",
		                           classe)
		return cls(conn.insert_id(), cursor=cursor)
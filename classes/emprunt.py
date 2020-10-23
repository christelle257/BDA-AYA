import fonctions_db


class Emprunt(object):
	def __init__(self, id_emprunt, cursor=None, stop=1, emprunt=None):
		if cursor == None:
			conn, cursor = fonctions_db.connect_db()
		if emprunt == None:
			emprunt = fonctions_db.execute_query(conn if conn else None, cursor,
			                                     f"""SELECT * FROM emprunt WHERE id = '{id_emprunt}' """,
			                                     is_result=True)
		self.id, self.Matricule, self.Code_Liv, self.Sortie, self.Retour = emprunt[0], emprunt[1], emprunt[2], emprunt[
			3], emprunt[4]

	@classmethod
	def create(cls, emprunt: tuple):
		conn, cursor = fonctions_db.connect_db()
		fonctions_db.execute_query(conn, cursor,
		                           f"""insert into emprunt (Matricule, Code_Liv, Sortie, Retour) VALUES (%s, %s, %s, %s)""", emprunt, close)
		return cls(conn.insert_id(), cursor=cursor)

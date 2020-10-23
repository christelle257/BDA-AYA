import fonctions_db
import classes

class Etudiant(object):
	def __init__(self, matricule, cursor=None, stop=1, etudiant=None,):
		if cursor is None:
			conn, cursor = fonctions_db.connect_db()
		if etudiant == None:
			etudiant = fonctions_db.execute_query(conn if conn else None, cursor,
			                                    f"""SELECT * FROM etudiant WHERE Matricule = '{matricule}' """,
			                                    is_result=True)
		self.Matricule, self.Nom, self.Prenoms, self.Sexe, self.classe = etudiant[0], etudiant[1], etudiant[2], etudiant[3], classes.classe.Classe(code_cl=etudiant[4])
		if stop == 1:
			fonctions_db.close_db(conn)

	@classmethod
	def create(cls, etudiant: tuple):
		conn, cursor = fonctions_db.connect_db()
		fonctions_db.execute_query(conn, cursor,
		                           f"""insert into etudiant (Matricule, Nom, Prenoms, Sexe, Code_Cl) VALUES (%s ,%s, %s, %s, %s)""",
		                           etudiant)
		return cls(conn.insert_id(), cursor=cursor)
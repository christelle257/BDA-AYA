from mysql import connector
from mysql.connector import Error
from mysql.connector import errorcode


def connect_db():
	"""Fonction permettant de se connecter à la base de donnée"""
	try:
		conn = connector.connect(
			host='localhost',
			user='root',
			password='',
			database='bda',
		)
		cursor = conn.cursor()
		return conn, cursor
	except connector.Error as error:
		try:
			conn = connector.connect(
				host='localhost',
				user='root',
				password='',
			)
			cursor = conn.cursor()
			cursor.execute("CREATE DATABASE IF NOT EXISTS bda;")
			conn.commit()
			conn.close()
			return connect_db()
		except connector.Error as error:
			print("probleme de connection {}".format(error))


def close_db(conn):
	"""Fonction permettant de fermer la base de donnée"""
	conn.commit()
	conn.close()


def execute_query(conn: None, cursor: None, query: str, values=None, is_excute_many=False, is_result=False,
                  is_result_many=False, close=True):
	myresult = None
	if not (conn and cursor):
		conn, cursor = connect_db()
	if not values:
		cursor.execute(query)
	elif not is_excute_many:
		cursor.excute(query, values)
	else:
		cursor.executemany(query, values)
	if is_result:
		if not is_result_many:
			myresult = cursor.fetchone()
		else:
			myresult = cursor.fetchall()
	if close:
		close_db(conn)
	else:
		conn.commit()
	if myresult:
		return myresult


def create_db(conn, cursor):
	execute_query(conn, cursor, """
	create table if not exists classe
		(
		    Code_Cl  varchar(6)  not null primary key ,
		    Intitule varchar(30) not null,
		    Effectif int         not null,
		    constraint classe_Code_Cl_uindex
		        unique (Code_Cl)
		);
	""")
	execute_query(conn, cursor, """
	create table if not exists livre
		(
		    Code_Liv varchar(15) not null,
		    Titre    varchar(40) not null,
		    Auteur   varchar(30) not null,
		    Genre    varchar(20) not null,
		    Prix     int         not null,
		    constraint LIVRE_Code_Liv_uindex
		        unique (Code_Liv)
		);
	""")
	execute_query(conn, cursor, """
		create table if not exists etudiant
		(
		    Matricule varchar(6)  not null primary key ,
		    Nom       varchar(20) not null,
		    Prenoms   varchar(50) not null,
		    Sexe      int(1)      not null,
		    Code_Cl   varchar(6)  not null,
		    constraint ETUDIANT_Matricule_uindex
		        unique (Matricule)
		);
		
		create index ETUDIANT_classe_Code_Cl_fk
		    on etudiant (Code_Cl);
		""")
	execute_query(conn, cursor, """
		create table if not exists emprunt
		(
		    Matricule varchar(6)  not null,
		    Code_Liv  varchar(15) not null,
		    Sortie    datetime    null,
		    Retour    datetime    null
		);
		
		create index emprunt_etudiant_Matricule_fk
		    on emprunt (Matricule);
		
		create index emprunt_livre_Code_Liv_fk
		    on emprunt (Code_Liv);
		""")
	close_db()
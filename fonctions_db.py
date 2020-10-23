from mysql import connector
from mysql.connector import Error
from mysql.connector import errorcode


def connect_db():
	"""Fonction permettant de se connecter à la base de donnée"""
	try:
		conn = connector.connect(
			host='localhost',
			user='root',
			password=''
		)
		cursor = conn.cursor()
		return conn, cursor
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



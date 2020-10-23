import fonctions_db

conn, cursor = fonctions_db.connect_db()
fonctions_db.create_db(conn, cursor)
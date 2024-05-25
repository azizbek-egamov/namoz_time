import sqlite3


def sql_connect():
    try:
        connection = sqlite3.connect("sqlite3.db")  # SQLite3 bazasiga bog'lanish
        connection.commit()
        return True
    except sqlite3.Error as e:
        print(e)
        return False


def sql_connection():
    connection = sqlite3.connect("sqlite3.db")  # SQLite3 bazasiga bog'lanish
    connection.commit()
    return connection


def user_(ab, ba, id):
    if sql_connect() == True:

        conn = sql_connection()
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {ab} WHERE {ba} = ?", (id,))

        res = cursor.fetchall()
        conn.commit()

        if not res:
            return False
        else:
            return True
    else:
        return False


def create_table():
    try:
        if sql_connect() == True:
            conn = sql_connection()
            cursor = conn.cursor()
            create_table = """ CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    uid BIGINT NOT NULL,
                    full_name TEXT NOT NULL,
                    username TEXT
                ); """
            cursor.execute(create_table)
            conn.commit()
            return True
        else:
            return False
    except:
        return False
create_table()


def add_information(uid, full_name, username):
    if sql_connect() == True:
        try:
            conn = sql_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO users (uid, full_name, username) VALUES (?, ?, ?)""",
                (uid, full_name, username),
            )
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
    else:
        return False


def select_info(id):
    if sql_connect() == True:
        conn = sql_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {id}")

        res = cursor.fetchall()
        conn.commit()
        l = list()
        if not res:
            return False
        else:
            for i in res:
                l.append(i)
            return l
    else:
        return False


def delete_table(da, ta, keys):
    if sql_connect() == True:
        try:
            conn = sql_connection()
            cursor = conn.cursor()
            cursor.execute(f"delete from {da} where {ta} = ?", (keys,))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
    else:
        return False


def drop_table(keys):
    if sql_connect() == True:
        try:
            conn = sql_connection()
            cursor = conn.cursor()
            cursor.execute(f"drop table {keys}")
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
    else:
        return False


def update_data(d1, d2, d3, key1, key2):

    if sql_connect() == True:
        try:
            conn = sql_connection()
            cursor = conn.cursor()

            cursor.execute(f"""UPDATE {d1} SET {d2} = '{key1}' WHERE {d3} = {key2};""")

            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
    else:
        return False


def table_info(ab, ba, id):
    if sql_connect() == True:

        conn = sql_connection()
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {ab} WHERE {ba} = ?", (id,))

        res = cursor.fetchall()
        conn.commit()

        if not res:
            return False
        else:
            return res
    else:
        return False

print(table_info("users", "uid", "5668945618"))
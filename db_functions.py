import pymysql
from config import host, user, password, db_name

# try:
#     connection = pymysql.connect(
#         host=host,
#         port=3306,
#         user=user,
#         password=password,
#         database=db_name,
#         cursorclass=pymysql.cursors.DictCursor
#     )
    # try:
        # with connection.cursor() as cursor:
        #     select_all_rows = "SELECT * FROM actor;"
        #     cursor.execute(select_all_rows)
        #     rows =  cursor.fetchall()
        #     for row in rows:
        #         print(row)

        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE `status` (id int AUTO_INCREMENT, user_id varchar(32), status varchar(32), coll_id varchar(32), pair_n int, PRIMARY KEY (id));"
        #     cursor.execute(create_table_query)
        #     print("Table created")

        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (user_id, coll_id) VALUES ('nb_1', 'bus_1');"
        #     cursor.execute(insert_query)
        #     connection.commit()

        # with connection.cursor() as cursor:
        #     update_query = "UPDATE `users` SET coll_id = 'car_2' WHERE user_id = 'nb_2';"
        #     cursor.execute(update_query)
        #     connection.commit()

        # with connection.cursor() as cursor:
        #     delete_query = "DELETE FROM `users` WHERE coll_id = 'bus_1';"
        #     cursor.execute(delete_query)
        #     connection.commit()

    #     with connection.cursor() as cursor:
    #         drop_table_query = "DROP TABLE `users`;"
    #         cursor.execute(drop_table_query)
            
    #     with connection.cursor() as cursor:
    #         select_all_rows = "SELECT * FROM users;"
    #         cursor.execute(select_all_rows)
    #         rows =  cursor.fetchall()
    #         for row in rows:
    #             print(row)
#     finally:
#         connection.close()
# except Exception as e:
#     print("Ops", e)



def receive_conn():
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor)
        return connection
    except Exception as e:
        print("Something is wrong")
        print(e)

def add_status(user_id, status="start", coll_id="None_1", pair_n=1):
    connection = receive_conn()
    try:
        with connection.cursor() as cursor:
            insert_query = f"INSERT INTO `status` (user_id, status, coll_id, pair_n) VALUES{(user_id, status, coll_id, pair_n)}"
            cursor.execute(insert_query)
            connection.commit()
    finally:
        connection.close()

def change_status(user_id, status=None, coll_id=None, pair_n=None): 
    connection = receive_conn()
    try:
        if status is not None:
            with connection.cursor() as cursor:
                update_query = f"UPDATE `status` SET status = '{status}' WHERE user_id = '{user_id}'"
                cursor.execute(update_query)
                connection.commit()
        if coll_id is not None:
            with connection.cursor() as cursor:
                update_query = f"UPDATE `status` SET coll_id = '{coll_id}' WHERE user_id = '{user_id}'"
                cursor.execute(update_query)
                connection.commit()

        if pair_n is not None:
            with connection.cursor() as cursor:
                update_query = f"UPDATE `status` SET pair_n = {pair_n} WHERE user_id = '{user_id}'"
                cursor.execute(update_query)
                connection.commit()
    finally:
        connection.close()

def delete_status(user_id):
    connection = receive_conn()
    try:
        with connection.cursor() as cursor:
            delete_query = f"DELETE FROM `status` WHERE user_id = '{user_id}'"
            cursor.execute(delete_query)
            connection.commit()
    finally:
        connection.close()


def add_coll_info(coll_id, user_id, name):
    connection = receive_conn()
    try:
        with connection.cursor() as cursor:
            insert_query = f"INSERT INTO `collection_info` (coll_id, user_id, name) VALUES {(coll_id, user_id, name)}"
            cursor.execute(insert_query)
            connection.commit()
    finally:
        connection.close()

def change_coll_info(coll_id, user_id=None, name=None): 
    connection = receive_conn()
    try:
        if user_id is not None:
            with connection.cursor() as cursor:
                update_query = f"UPDATE `collection_info` SET user_id = '{user_id}' WHERE coll_id = '{coll_id}'"
                cursor.execute(update_query)
                connection.commit()
        if name is not None:
            with connection.cursor() as cursor:
                update_query = f"UPDATE `status` SET name = '{name}' WHERE coll_id = '{coll_id}'"
                cursor.execute(update_query)
                connection.commit()
    finally:
        connection.close()

def delete_coll_info(coll_id):
    connection = receive_conn()
    try:
        with connection.cursor() as cursor:
            delete_query = f"DELETE FROM `collection_info` WHERE coll_id = '{coll_id}'"
            cursor.execute(delete_query)
            connection.commit()
    finally:
        connection.close()


def add_saved_coll(user_id, coll_id):
    connection = receive_conn()
    try:
        with connection.cursor() as cursor:
            insert_query = f"INSERT INTO `saved_collection` (user_id, coll_id) VALUES{(user_id, coll_id)}"
            cursor.execute(insert_query)
            connection.commit()
    finally:
        connection.close()

def change_saved_coll(user_id, coll_id): 
    connection = receive_conn()
    try:
         with connection.cursor() as cursor:
            update_query = f"UPDATE `saved_collection` SET coll_id = '{coll_id}' WHERE user_id = '{user_id}'"
            cursor.execute(update_query)
            connection.commit()
    finally:
        connection.close()

def delete_saved_coll(user_id, coll_id):
    connection = receive_conn()
    try:
        with connection.cursor() as cursor:
            delete_query = f"DELETE FROM `saved_collection` WHERE user_id = '{user_id}' AND coll_id = '{coll_id}'"
            cursor.execute(delete_query)
            connection.commit()
    finally:
        connection.close()


def add_coll_content(coll_id, pair_n, eng_word, rus_word):
    connection = receive_conn()
    try:
        with connection.cursor() as cursor:
            insert_query = f"INSERT INTO `collection_content` (coll_id, pair_n, eng_word, rus_word) VALUES{(coll_id, pair_n, eng_word, rus_word)}"
            cursor.execute(insert_query)
            connection.commit()
    finally:
        connection.close()

def change_coll_content(coll_id, pair_n = None, eng_word=None, rus_word=None): 
    connection = receive_conn()
    try:
        if pair_n is not None:
            with connection.cursor() as cursor:
                update_query = f"UPDATE `collection_content` SET pair_n = '{pair_n}' WHERE coll_id = '{coll_id}'"
                cursor.execute(update_query)
                connection.commit()
        if eng_word is not None:
            with connection.cursor() as cursor:
                update_query = f"UPDATE `collection_content` SET eng_word = '{eng_word}' WHERE coll_id = '{coll_id}'"
                cursor.execute(update_query)
                connection.commit()

        if pair_n is not None:
            with connection.cursor() as cursor:
                update_query = f"UPDATE `collection_content` SET rus_word = {rus_word} WHERE coll_id = '{coll_id}'"
                cursor.execute(update_query)
                connection.commit()
    finally:
        connection.close()

def delete_coll_content(coll_id):
    connection = receive_conn()
    try:
        with connection.cursor() as cursor:
            delete_query = f"DELETE FROM `collection_content` WHERE coll_id = '{coll_id}'"
            cursor.execute(delete_query)
            connection.commit()
    finally:
        connection.close()
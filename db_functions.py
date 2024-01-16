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

def add_user(db_user_id, db_status="start", db_coll_id="None_1", db_pair_n=1):
    connection = receive_conn()
    try:
        with connection.cursor() as cursor:
            insert_query = f"INSERT INTO `status` (user_id, status, coll_id, pair_n) VALUES{(db_user_id, db_status, db_coll_id, db_pair_n)}"
            cursor.execute(insert_query)
            connection.commit()
    finally:
        connection.close()

def change_status(db_user, db_status=None, db_coll_id=None, db_pair_n=None): 
    connection = receive_conn()
    try:
        if db_status is not None:
            with connection.cursor() as cursor:
                update_query = f"UPDATE `status` SET status = '{db_status}' WHERE user_id = '{db_user}'"
                cursor.execute(update_query)
                connection.commit()
        if db_coll_id is not None:
            with connection.cursor() as cursor:
                update_query = f"UPDATE `status` SET coll_id = '{db_coll_id}' WHERE user_id = '{db_user}'"
                cursor.execute(update_query)
                connection.commit()

        if db_pair_n is not None:
            with connection.cursor() as cursor:
                update_query = f"UPDATE `status` SET pair_n = {db_pair_n} WHERE user_id = '{db_user}'"
                cursor.execute(update_query)
                connection.commit()
    finally:
        connection.close()

def delete_user(db_user):
    connection = receive_conn()
    try:
        with connection.cursor() as cursor:
            delete_query = f"DELETE FROM `status` WHERE user_id = '{db_user}'"
            cursor.execute(delete_query)
            connection.commit()
    finally:
        connection.close()
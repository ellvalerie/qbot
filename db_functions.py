import pymysql
import os
from dotenv import load_dotenv, find_dotenv
from logger import db_logger


load_dotenv(find_dotenv())
host = os.getenv('HOST')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
db_name = os.getenv('DB_NAME')


def receive_conn():
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor)
        db_logger.info(f"Succesfully connected to the database {db_name}")
        return connection
    except Exception as e:
        db_logger.critical(f"Connection to the database {db_name} failed with error: {e}")

def add_status(user_id, status="start", coll_id="None_1", pair_n=1):
    connection = receive_conn()
    try:
        with connection.cursor() as cursor:
            insert_query = f"INSERT INTO `status` (user_id, status, coll_id, pair_n) VALUES{(user_id, status, coll_id, pair_n)}"
            cursor.execute(insert_query)
            connection.commit()
            db_logger.debug(f"Added status 'start' to {user_id} in {db_name}.status")
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
                db_logger.debug(f"Updated status to '{status}' to {user_id} in {db_name}.status")
        if coll_id is not None:
            with connection.cursor() as cursor:
                update_query = f"UPDATE `status` SET coll_id = '{coll_id}' WHERE user_id = '{user_id}'"
                cursor.execute(update_query)
                connection.commit()
                db_logger.debug(f"Updated coll_id to '{coll_id}' in {db_name}.status")

        if pair_n is not None:
            with connection.cursor() as cursor:
                update_query = f"UPDATE `status` SET pair_n = {pair_n} WHERE user_id = '{user_id}'"
                cursor.execute(update_query)
                connection.commit()
                db_logger.debug(f"Updated pair_n to {pair_n} in {db_name}.status")
    finally:
        connection.close()

def delete_status(user_id):
    connection = receive_conn()
    try:
        with connection.cursor() as cursor:
            delete_query = f"DELETE FROM `status` WHERE user_id = '{user_id}'"
            cursor.execute(delete_query)
            connection.commit()
            db_logger.debug(f"Deleted {user_id} in {db_name}.status")
    finally:
        connection.close()


add_status("omg")
change_status("omg", "editing", "coll_funny", 4)
delete_status("omg")

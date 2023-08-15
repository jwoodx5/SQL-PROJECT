import psycopg2
from dotenv import load_dotenv
import os
import streamlit as st

def get_connection():
    conn = psycopg2.connect(
    host = os.getenv('HOST'),
    database = os.getenv('DBNAME'),
    user = os.getenv('USER'),
    password = os.getenv('PASSWORD')
    )
    return conn


def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            cx_id SERIAL PRIMARY KEY,
            cx_first_name VARCHAR(50) NOT NULL,
            cx_last_name VARCHAR(50) NOT NULL,
            cx_email VARCHAR(100) NOT NULL,
            cx_phone_number VARCHAR(20) NOT NULL,
            cx_address VARCHAR(100) NOT NULL
        );
    """)
    conn.commit()

def check_duplicate_customer(email):
    conn = get_connection()
    cur = conn.cursor()
    select_query = "SELECT cx_id FROM customers WHERE cx_email = %s"
    values = (email,)
    
    try:
        cur.execute(select_query, values)
        existing_customer = cur.fetchone()
        return existing_customer
    except Exception as e:
        st.write("Error:", e)
        return None
    finally:
        cur.close()
        conn.close()


def create_address_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS customer_addresses (
            address_id SERIAL PRIMARY KEY,
            cx_id INT NOT NULL,
            address VARCHAR(100) NOT NULL,
            FOREIGN KEY (cx_id) REFERENCES customers (cx_id)
        );
    """)
    conn.commit()

def insert_address(cx_id, address):
    conn = get_connection()
    cur = conn.cursor()
    insert_query = "INSERT INTO customer_addresses (cx_id, address) VALUES (%s, %s)"
    values = (cx_id, address)

    try:
        cur.execute(insert_query, values)
        conn.commit()
        return True
    except Exception as e:
        st.write("Error:", e)
        return False
    finally:
        cur.close()
        conn.close()

def insert_data(fname, lname, email, phone, address):
    # Check if a customer with the same email already exists
    existing_customer = check_duplicate_customer(email)

    if existing_customer:
        cx_id = existing_customer[0]
    else:
        conn = get_connection()
        cur = conn.cursor()
        insert_query = "INSERT INTO customers (cx_first_name, cx_last_name, cx_email, cx_phone_number) VALUES (%s, %s, %s, %s) RETURNING cx_id"
        values = (fname, lname, email, phone)

        try:
            cur.execute(insert_query, values)
            cx_id = cur.fetchone()[0]
            conn.commit()
        except Exception as e:
            st.write("Error:", e)
            return False
        finally:
            cur.close()
            conn.close()

    # Insert the address for the customer
    result = insert_address(cx_id, address)
    return result

def get_addresses_by_customer(cx_id):
    conn = get_connection()
    cur = conn.cursor()
    select_query = "SELECT address FROM customer_addresses WHERE cx_id = %s"
    values = (cx_id,)

    try:
        cur.execute(select_query, values)
        addresses = cur.fetchall()
        return addresses
    except Exception as e:
        st.write("Error:", e)
        return []
    finally:
        cur.close()
        conn.close() 

    

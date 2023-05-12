import sqlite3
import re
conn = sqlite3.connect('customer.db')
cur = conn.cursor()

first_name = input("enter your first name ")
last_name = input("enter your last name ")
email = input ("enter your email name ")

cur.execute(f"""
INSERT INTO customer (
  first_name,
  last_name,
  email
)

VALUES (
    '{first_name}',
    '{last_name}',
    '{email}'
)
""")
conn.commit()

conn.close()


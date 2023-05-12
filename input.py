import sqlite3
import re
def get_name(inp_prompt: str, err_prompt: str) -> str:
        is_valid = re.compile(r"^[a-zA-Z]+$").match
        while True:
            name = input(inp_prompt).strip()
            if not is_valid(name):
                print(err_prompt)
                continue
            return name

def get_user() -> tuple[str, str]:
    first_name = get_name("First name: ", "Invalid first name")
    last_name = get_name("Last name: ", "Invalid last name")
    ID = get_name ("Enter ID: ", "invalid ID")
    return first_name, last_name, ID

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


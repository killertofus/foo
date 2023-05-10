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
    return first_name, last_name

print(get_user())

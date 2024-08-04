import re

user_db = []

create_user_record = lambda name, email: {"name": name, "email": email}
insert_user_record = lambda user: user_db.append(user)
fetch_all_user_records = lambda: user_db

def decode_smartscan_code(smartscan_code):
    decoded_data = smartscan_code.decode("utf-8") if isinstance(smartscan_code, bytes) else smartscan_code
    match = re.match(r'^(.*?),(.*?)$', decoded_data.strip())
    if not match:
        raise ValueError("Invalid SmartScan Code format. Expected 'name,email'")
    name, email = match.groups()
    return name, email

def RegisterUserFromSmartScan(smartscan_code):
    try:
        name, email = decode_smartscan_code(smartscan_code)
        new_user = create_user_record(name, email)
        insert_user_record(new_user)
        print("New user registered:", new_user)
        print("All registered users:", fetch_all_user_records())
    except Exception as e:
        print("Error registering user:", str(e))

def view_all_registered_users():
    print("All registered users:", fetch_all_user_records())

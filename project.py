import json
import requests
import time
import base64

url = "https://cae-bootstore.herokuapp.com/"
endpoint_login = "/login"
endpoint_user = "/user"
endpoint_book = "/book"
endpoint_question = "/question"

def create_question():
    question = input("Enter question : ")
    answer = input("Enter answer : ")
    new_question = {
        "question" : question,
        "answer" : answer
    }
    payload_json_create = json.dumps(new_question)
    response = requests.post(
        url + endpoint_question,
        data = payload_json_create
    )
    if response.ok:
        print("Successfully made question.")
    else:
        print("Idiot. You broke it.")

def edit_question():
    pass

def delete_question():
    pass

def view_questions():
    pass

def login_user(user_name, password):
    
    auth_string=user_name+':'+password
    
    headers = {
        'Authorization': "Basic "+base64.b64encode(auth_string.encode()).decode()
    }

    user_data=requests.get(
        url + endpoint_login,
        headers = headers
    )
    return user_data.json()

def register_user(payload):
    payload_json_string = json.dumps(payload)
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(
        url + endpoint_user,
        data = payload_json_string,
        headers = headers
    )
    return response.text


def login(email):
    password = input("Password: ")
    user=login_user(email, password)
    return user
    
user_info = {}
def register():
    print("Registration:")
    email=input("Email: ")
    first_name=input("First Name: ")
    last_name=input("Last Name: ")
    password=input("Password: ")

    user_info={
        "email":email,
        "first_name":first_name,
        "last_name":last_name,
        "password":password,
        "status":"user"
    }

    if email == "cdschmidt1103@gmail.com":
        user_info["status"] = "admin"

    return register_user(user_info)

def main():
    while True:
        print("Welcome to the Bookstore")
        email = input("Type your email to login or Type `register` to Register : ")
        if email == 'register':
            success_register = register()
            if success_register:
                print("You have successfully registered")
                continue
            else:
                print("There was an error please try again")
                time.sleep(2)
                continue
        elif email.lower() == "quit":
            print("Goodbye")
            break
        else:
            try:
                login(email)
            except:
                print("Invalid Username/Password Combo")
                time.sleep(2)
                continue

        if email == "cdschmidt1103@gmail.com":
            print("This is the admin.")
            print("""
options for your questions:
1. Create
2. Edit
3. Delete
4. View            
""")
            option = input("Choose an option : ")
            if option == "1":
                create_question()
            elif option == "2":
                edit_question()
            elif option == "3":
                delete_question()
            elif option == "4":
                view_questions()

        else:
            print("This is the user.")
            return

main()

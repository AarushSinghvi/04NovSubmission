# Initialize User database
user_database = {}
print("Welcome to HAP! Would You Like To Login or Sign Up?")

#Function for new user registration
def register_user():
    while True:
        username = input("Please Enter your Email Address to register with: ")
        if username in user_database:
            print("This Email Is Already Registered With HAP")
        elif username == "":
            print("Please Input A Valid Email Address")
        else:
            password = register_password()
            user_database[username] = password
            print("The Email", username, "Has Successfully been registered with HAP")
            break # Break the loop after a successful registration

#Function for Creating a Password
def register_password():
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#"
    while True:
        password = input("Enter a 6-Digit Password: ")
        if len(password) == 6 :
            return password
        else:
            print("The Password Must Be only 6-Characters Long")

#Function for User Login
def login_user():
    username = input("Please Enter Your Email Address: ")
    if username not in user_database:
        print("This Email Adress Is Not Associated With HAP")
    return False

username = str

password = input("Please Enter Your Password")
if user_database [username] != password:
    print("Incorrect Password, Try Again")
    return False
elif len(password) != 6:
    print("The password Must Be Only 6-Characters Long")
    return False

print("Welcome Back", username, "!")
return True 

#Main Function
def main():
    print("Welcome To HAP!")
    while True:
        action = input("Would you like to 'Login' or 'Sign Up'? ").lower()

        if action == 'sign up':
            register_user()

        elif action == 'login':
            if login_user():
                break  # Exit the loop if login is successful

        else:
            print("Invalid Option. Please choose 'Login' or 'Sign Up'.")

# Now ask if the user wants to search
    search = input("What Would You Like To Search Today? ")

        if search == "Database":
            # Implement Database Search Logic Here
            print("Searching Results...")

        elif search == "":
            print("Oops, Your search Does Not match Any Documents In Our Database.")
            # Implement Suggestions Logic Here
        else:
            print("Invalid search. Please try again.")

#Impliment Suggestions Logic Here

#Function For Bookmarking (to be implimented)

#Ask if the users want to continue searching

if __name__ == "__main__":
    main()
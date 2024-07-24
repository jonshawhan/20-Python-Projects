# Collect email from user
# split email using the @, example: joncbarnette@gmail.com
# first part as username: joncbarnette
# second part as domain: gmail.com
# split domain using the .

def main():
    print("Welcome to the email slicer!\n")

    email_input = input("Input your email address: \n")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("")
    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)
    print("\n--------------------\n")

while True:
    main()    
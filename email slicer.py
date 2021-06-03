def email_slicer():
    email = input("Enter your email: ")
    name = email[ : email.index("@")]
    site = email[ email.index("@")+1 : ]
    print(f"Hello {name} you are registered at {site} !")

email_slicer()

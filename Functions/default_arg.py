def greet (name ="anon"):
    if name != None:
        print(name)
    else:
        print(None)


greet("Chien")
greet()
greet(None)
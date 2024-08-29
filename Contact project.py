contacts={}
def new():
    x=input("Enter your name:")
    y=input("Enter your number:")
    contacts[x]=y
    print(contacts)
    
def change():
    x=input("what is the changed name?")
    y=input("Enter your changed number:")
    contacts[x]=y
    print("done!")

def delete():
    x=input("which name shoud be deleted?")
    del contacts[x]
    print("done!")
    print(contacts)
def show():
    print(contacts)
    
while True:
    h=input("what do you want to do?")
    if h=="out":
        print("Goodbye!")
        break
    elif h=="new":
        new()
    elif h=="change":
        change()
    elif h=="delete":
        delete()
    elif h=="show":
        show()
    else:
        print("Unvalid!")


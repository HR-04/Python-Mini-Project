from cryptography.fernet import fernet

def load_key():
    file=open("key.key","rb")
    key=file.read
    file.close()
    return key
    
key=load_key()
fer=fernet(key)

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user,pwd=data.split("|")
            print('user: ',user,'|pwd:',fer.decrypt(pwd.encode()).decode())
        
def add():
    name=input('Account name: ')
    password=input('Password: ')
    with open('password.txt','w') as f:
        f.write(name + "|"+ fer.encrypt(password.encode()).decode()+"\n")
    
while True:
    mode=input("would you like to add a new password or view the existing password or press q to quit (view / add / q ): ").lower()
    
    if mode == 'q':
        quit()
    
    if mode == view:
        view()
    elif mode == add:
        add()
    else:
        print("invalid mode")
        continue
    

""" Passcode program, by Andrew Li """

# all modules needed for secure databases
import bleach
import json
import hashlib
import os

# checks username
class password:

    def username(self):

        # input and clean username
        name = bleach.clean(input('Username: '))

        # creates json if none exists
        if (os.path.isfile('password.json') == False):
            # create json file
            with open('password.json', 'w') as passcode1:
                exists = True
                json.dump(exists, passcode1)
         
        # loads json file to check user
        with open('password.json', 'r') as fp:
            try: 
                json.load(name in fp)
                return (passcode(name))
            except:
                return createAccount(name)

        # if (user == )

# checks passcode with one in database
def passcode(user):

    # check user password 
    bar = bleach.clean(input('Password: '))

    with open('password.json', 'wr') as fp:
        json.dump({name: someHash}, fp)
    # if (bar == )

# creates new account
def createAccount(name):

    print('Welcome new user!\n')
    bar = bleach.clean(input('New password: '))

    if (len(bar) < 5):
        print('Length of password is too short')
        return 1

    zed = bleach.clean(input('Retype password: '))

    if (bar == zed):

        #insert some hash function
        someHash = hashlib.sha1( ('$2%' + bar + 's9!').encode('utf-8') ).hexdigest()

        with open('password.json', 'w') as fp:
            json.load(fp).append({name: someHash})

        print('Account created')

    else:

        print('Passwords do not match. Try again.')

# main calls entire system
def main():

    print('This is Foo Inc.\n Please enter your username')

    result = password().username()

# system calls name which triggers main
if __name__ == "__main__":
    main()

import csv
import os

import Account
import Input

states = ["azarbaijan sharghi", "azarbaijan gharbi", "ardebil", "esfahan", "alborz", "eilam", "booshehr",
          "tehran", "chaharmahal va bakhtiari", "khorasan jonobi", "khorasan razavi", "khorasan shomali",
          "khozestan", "zanjan", "semnan", "sistan va balochestan", "fars", "qazvin", "qom", "kordestan",
          "kerman", "kermanshah", "kohgiloye va boyerahmad", "golestan", "gilan", "lorestan", "mazandaran",
          "markazi", "hormozgan", "hamedan", "yazd"]

usernames = []
sujest = []


class User:

    def __init__(self, username, name, family, birthdate, state, gender, password):
        self.username = username
        self.name = name
        self.family = family
        self.birthdate = birthdate
        self.state = state
        self.gender = gender
        self.password = password

    def age(self):
        # ناقصه
        # userameرا به عنوان ورودی میگرفت که خب دیگه لازم نیست. چون سلف رو داریم و از آن میتونیم یوزرنیم رو برداریم
        pass


def get_usernames():
    # this def will save all usernames in a global list calld 'usernames'
    # we call it befor cheking usernames to update the list
    with open(Account.accounts) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            usernames.append(row['username'])
    return usernames


# کل این بخش کار نمیکنه
def FindFrend(username, state):
    with open(Account.accounts) as csv_file:
        counter = 1
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row["state"] == state:
                sujest.append(row['username'])
                print(f'{counter}--->{row["name"]} {row["family"]}')  # age: {row["age"]}')
                counter += 1
    while True:
        try:
            frendId = Input.freind_id()
            if os.path.exists("frend.csv"):
                with open("frend.csv", "a") as f:
                    f.write(f"{username},{sujest[frendId]}\n")
                break
            else:
                with open("frend.csv", "a") as f:
                    f.write("username,frend\n")
                    f.write(f"{username},{sujest[frendId]}\n")
                break
        except:
            print('adad na motabar ast,\ndobare talash konin')

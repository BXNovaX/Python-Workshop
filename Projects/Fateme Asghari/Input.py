import datetime
import os
import re

import jdatetime

import Account
import User

now = datetime.datetime.today()


def name():
    while True:
        name = input('lotfan name khod ra vared konid:\n')
        if len(name) > 30 or len(name) < 2:
            print('2 ta 30 character\n')
        elif not re.search("[a-z]", name):
            print('shamele horofe kochake englisi\n')
        elif re.search("[0-9]", name):
            print('bedone adad adad\n')
        elif re.search("[_@$]", name):
            print('bedone symbol\n')
        else:
            return name


def family():
    while True:
        family = input('name khanevadegi khod ra vared konid:\n')
        if len(family) > 30 or len(family) < 2:
            print('tedad characteer ha kam ya ziad ast\n')
        elif not re.search("[a-z]", family):
            print('shamele horofe kochake englisi\n')
        elif re.search("[0-9]", family):
            print('bedone adad adad\n')
        elif re.search("[_@$]", family):
            print('bedone symbol\n')
        else:
            return family


def birthday():
    while True:
        inputDate = input('tarikhe tavalode khod ra vared konid: YYYY/MM/DD: ')
        try:
            SHbirthday = inputDate.split('/')
            SHyear = SHbirthday[0]
            if len(SHyear) != 4:
                print('sal shamele 4 adad')
            SHmonth = SHbirthday[1]
            if len(SHmonth) != 2:
                print('mah shamele 2 adad')
            SHday = SHbirthday[2]
            if len(SHday) != 2:
                print('rooz shamele 2 adad')
            try:
                birthday = jdatetime.date(day=int(SHday), month=int(SHmonth), year=int(SHyear)).togregorian()
                if int(birthday.year) > int(now.year):
                    print('tarikh na motabar')
                else:
                    return inputDate
            except:
                print('tarikh na motabar\ndobarre emtehan konid')
        except:
            print('type vorodi na motabar')


def state():
    while True:
        inputState = input('lotfan ostane khod ra vared konid:\n1.moshahede liste ostan ha\n')
        if inputState == str(1):
            for state in User.states:
                print(state + "\n")
        elif inputState.lower() in User.states:
            return inputState
        else:
            print('vorodi na motabar\nlist ostan ha ra moshahede konid')


def gender():
    while True:
        gender = input("jensiat khod ra taiin konid:\n1.aqa\n2.khanom\n:")
        if gender == '1':
            gender = 'male'
            return gender
        elif gender == '2':
            gender = 'female'
            return gender
        else:
            print('vorodi na motabar\ndobare emtehan konid\n')


def username():
    try:
        usernames = User.get_usernames()
    except:
        None
    while True:
        username = input('username khod ra vared konid:\n')
        if (len(username) < 4) or (len(username) >= 40):
            print('4 ta 40 charracter\n')
        elif not re.search("[a-z]", username):
            print('shamele horofe kochake englisi\n')
        elif not re.search("[A-Z]", username):
            print('shamele horoofe bozorge englisi\n')
        elif re.search("\s", username):
            print('bedone fasele (space)\n')
        elif os.path.exists(
                Account.accounts):  # if this file dose not exist it means that we dont have eny member so its the first one!
            if username in usernames:
                print('name karbari tekrari\n')
            else:
                return username
        else:
            return username


def password():
    while True:
        password = input('password khod ra vared konid\n (A-Z,a-z,1-9,symbol)\n')
        if (len(password) <= 8) or (len(password) >= 16):
            print('8 ta 16 charracter\n')
        elif not re.search("[a-z]", password):
            print('shamele horofe kochake englisi\n')
        elif not re.search("[A-Z]", password):
            print('shamele horoofe bozorge englisi\n')
        elif not re.search("[0-9]", password):
            print('shamele adad')
        elif not re.search("[_@$]", password):
            print('shamele symbol\n')
        elif re.search("\s", password):
            print('bedone fasele (space)\n')
        else:
            while True:
                confirm = input('password khod ra taiid konid:\n')
                if confirm == password:
                    return password
                else:
                    print('motabeghat nadarea\nlotfan dobare emtehan konid\n')
                    break


def freind_id():
    while True:
        try:
            frendId = int(input('shomare farde morede nazar ra vared konid:\n'))
        except:
            print('faghat adad vared konid')
        if frendId - 1 > len(User.sujest) or frendId - 1 < 0:
            print('adad na motabar\n')
        else:
            return frendId

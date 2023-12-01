import csv
import os

import Input
import Menu
import User

accounts = 'Accounts.csv'


# ثبت نام کاربر مورد نظر که به عنوان ورودی به register داده شده
def register(user):
    # for unexpected comma in input
    # befor adding data to our csv file, we will replace comma with 'notthing' so we delete it
    # if we dont, it will be possible to enter comma in input and cuz we use csv (comma to separate values) it will make problems...
    username = user.username.replace(",", "")
    name = user.name.replace(",", "")
    family = user.family.replace(",", "")
    password = user.password.replace(",", "")
    # ---------------- until here --------------------
    # nad here we add our fixed data into csv file but befor doing that, we must chek if the file exist
    # else we have to crate a file and make our title row
    if os.path.exists(accounts):
        with open(accounts, "a") as f:
            f.write(f"{username},{user.gender},{name},{family},{user.birthdate},{user.state},{password}\n")
        print('account shoma sakhte shod\nlotfan dobare vared shavid\n\n')
        Menu.intro()
    else:
        with open(accounts, "w") as f:
            f.write('username,gender,name,family,birthday,state,password\n')  # this is our title row
            f.write(f"{username},{user.gender},{name},{family},{user.birthdate},{user.state},{password}\n")
        print('account shoma sakhte shod\nlotfan dobare vared shavid\n\n')
        Menu.intro()


# ورود
def enter_account(username, password):
    with open(accounts) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row["username"] == username and row["password"] == password:
                name = row["name"]
                print('\nshoma vared shodid :)\n')
                print(f"salam {name} ")
                Menu.user_menu(username)
                return
        print("username ya password eshtebah ast")


class Account:
    def __init__(self):
        self.user = User

    # ایجاد اکانت
    #میخواهیم با استفاده از اطلاعاتی که کاربر وارد میکنه براش اکانت بسازیم
    #پس اول دونه دونه اطلاعات رو از کاربر میگیریم و بعدش یه کاربر با اون مشخصات میسازیم
    #تا حالا فقط کاربر رو ایجاد کردیم و هنوز جایی ثبتش نکردیم
    #پس با متد register میریم توی فایل اکانتز ثبتش میکنیم
    def sign_up(self):
        name = Input.name()
        family = Input.family()
        birthdate = Input.birthday()
        state = Input.state()
        gender = Input.gender()
        username = Input.username()
        password = Input.password()
        self.user = User.User(username, name, family, birthdate, state, gender, password)
        register(self.user)

    # ورود به اکانت
    #کاربر میخواد وارد حسابش بشه
    #اگه هنوز هیچ اکانتی وجود نداره پس باید اکانت بسازیم
    # ولی اگه حساب کاربری وجود داره یوزرنیم رو میگیریم. اگه توی یوزرنیم هامون بود، پسورد رو میگیریم و بعدش با این دو تا داده وارد حسابش میشیم
    def sign_in(self):
        # this function called in intro function
        # if this file dose not exist it means that we dont have eny member so its the first one!
        if not os.path.exists(accounts):
            print('hanoz hich hesabe karbari vojod nadarad lotfan account khod ra besazid:\n')
            self.sign_up()
        else:
            while True:
                username = input('username khod ra vard konid:\n')
                usernames = User.get_usernames()
                if not username in usernames:
                    print('username vojod nadarad\nlotfan mojadadan emtehan konid\n')
                else:
                    password = input('password khod ra vared konid:\n')
                    enter_account(username, password)

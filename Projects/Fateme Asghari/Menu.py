import Account
import Input
import User

#اولین منو
def intro():
    account = Account.Account()
    print("salam\nbe 'doost' khosh omadid\n")
    while True:
        choice = (input('1.sakhte account\n2.vorod be account\n:'))
        if choice == '1':
            account.sign_up()
        elif choice == '2':
            account.sign_in()
        else:
            print('vorodi na motabar\n')


#  سلام!
#  این بخش منویی هست که بعد از داخل شدن کاربر به حسابش، صدا زده میشه
# باید منو بسازم و داخلش طبیعتا اصل برنامه جا داده میشه
# بخش های ارسال پیام و و...


#دومین منو
#که بعد از وارد شدن کاربر به اکانتش نمایش داده میشه
def user_menu(username):
    chois = input('1.doostyabi\n2.ersale payam\n3.moshahede payam ha\n')
    if chois == '1':
        # print("kar nemikone")
        state = Input.state()
        User.FindFrend(username, state)
    elif chois == '2':
        print("bakhshe doost yabi (ke be sorate 'function' neveshte shode) inja seda zade mishe")
    elif chois == '3':
        print("bakhshe moshahede payam (ke be sorate 'function' neveshte shode) inja seda zade mishe")
    else:
        print('vorodi na motabar\n')

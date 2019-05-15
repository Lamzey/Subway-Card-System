#Aribido Lamzey
#+2348131089608
#lamzey.m@gmail.com


print('Welcome to New York Subway Card System')

input('Please Any Key To Continue')

print('Please slot in your card and Enter you pin carefully')

card_pin = input()

if len(card_pin) != 4:
    print('Sorry, Incorrect pin, try again')

    card_pin = input()
if len(card_pin) != 4:
    print('Place your thumb on the mouse for automation!')
else:
    print('Progress by providing your bank account, Note: NUBAN must be 10 digits')

bankaccount = input()
if len(bankaccount) != 10:
    print('Sorry, Incorrect Bank Account, try again')
    bankaccount = input()
if len(bankaccount) != 10:
    print('Place your thumb on the sensor for automated derivation of bank details')
    
automation = input('Press The Enter Key')
automation = ['processing...', '10...', '20...', '30...', '40...', '50...', '60...', '70..', '80..', '90.', '100']
for a in automation:
    print(a)
print('Automation Successful')

print('How much would you like to recharge on your card?, You are adviced to recharge $30 dollars')

Recharge_Amount = input()
transaction = ['processing...', '10...', '20...', '30...', '40...', '50...', '60...', '70..', '80..', '90.', '100']
for t in transaction:
    print(t)
print('Recharge Successful')

print('Lists of stations')

stations = ['5th', 'Pelham Parkway', 'Bronx', 'Guns Hill']
for s in stations:
    print (s)

stations_select = input()

print('Lists of zones')
zones = ['zone 1', 'zone 2', 'zone 3']
for z in zones:
    print (z)

print('Kindly move on through the barrier, swipe your card and select your fare')

print('Below are the Fares for each journey, ' + ' Select a, b, or c.')
print('              Journey                 |       Fare    ')
print('(a)  Anywhere in Zone 1               |       $2.50   ')
print('(b)  Any one zone outside Zone 1      |       $2.00   ')
print('(c)  Any two zones including Zone 1   |       $3.00   ')
print('(d)  Any two zones excluding Zone 1   |       $2.25   ')
print('(e)  Any three zones                  |       $3.20   ')
print('(f)  All bus journey                  |       $1.80   ')

balance = 30
journey = input()
if journey == 'a':
    print('Balance:')
    print(30 - 2.50)
    print('Your fare has been deducted, please proceed to your train')
elif journey == 'b':
    print('Balance:')
    print(30 - 2.00)
    print('Your fare has been deducted, please proceed to your train')
elif journey == 'c':
    print('Balance:')
    print(30 - 3.00)
    print('Your fare has been deducted, please proceed to your train')
elif journey == 'd':
    print('Balance:')
    print(30 - 2.25)
    print('Your fare has been deducted, please proceed to your train')
elif journey == 'e':
    print('Balance:')
    print(30 - 3.20)
    print('Your fare has been deducted, please proceed to your train')
elif journey == 'f':
    print('Balance:')
    print(30 - 1.80)
    print('Your fare has been deducted, please proceed to your train')
else:
    print('You have not selected any fare')
    exit()


















      

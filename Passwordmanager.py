# PASSWORD MANAGER


PASSWORDS = {'email': '123email','luggage': '12345'}
import sys
import pyperclip
if len(sys.argv)<2:
    print('Usage : python password [account]-copy account password')
    sys.exit()
account=sys.argv[1]
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for "+ str(account)+" copied to clipboard.")
else:
    print("There is no account named "+ str(account))

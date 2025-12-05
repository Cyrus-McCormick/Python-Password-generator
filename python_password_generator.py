import random

#Is a list of posible characters to pull from
lower_letter = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
upper_letter = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
numbers = ('0','1','2','3','4','5','6','7','8','9')
special_characters = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', "'", '"', ',', '.', '/', '?', '~')

#finds the length of the password the user wands
pws_length = int(input('Enter how long you wnat your passowrd as a number: '))


build_password = []
password = ''
#creates the password
if(pws_length > 0):

    #looks to see if the user wants upper case letter
    want_upper = input('Do you want upper case characters? yes/no: ')
    if(want_upper == 'yes' or want_upper == 'Yes' or want_upper == 'Y' or want_upper == 'y'):
        get_upper=True
    elif(want_upper == 'no' or want_upper == 'No'or want_upper == 'N' or want_upper == 'n'):
        get_upper=False
    else:
        raise ValueError("Not a valid input for length to getnerate")
    
    #looks to see if the user wants numbers
    want_number = input('Do you want numbers? yes/no: ')
    if(want_number == 'yes' or want_number == 'Yes' or want_number == 'Y' or want_number == 'y'):
        get_number=True
    elif(want_number == 'no' or want_number == 'No' or want_number == 'N' or want_number == 'n'):
        get_number=False
    else:
        raise ValueError("Not a valid input for length to getnerate")

    #looks to see if the user wants special characters
    want_special = input('Do you want special case characters? yes/no: ')
    if(want_special == 'yes' or want_special == 'Yes' or want_special == 'Y' or want_special == 'y'):
        get_special=True
    elif(want_special == 'no' or want_special == 'No' or want_special == 'N' or want_special == 'n'):
        get_special=False
    else:
        raise ValueError("Not a valid input for length to getnerate")

    #gets each character in the password from lower and upper case letters, numbers, and specail characters
    while(len(build_password) != pws_length):
        new_charcater = random.randint(1,4)

        #adds a lower case character to the password
        if(new_charcater == 1):
            new_lower = random.randint(1,len(lower_letter)-1)
            build_password.append(lower_letter[new_lower])
            
        #adds a upper case character to the password
        elif(new_charcater == 2 and get_upper == True):
            new_upper = random.randint(1,len(upper_letter)-1)
            build_password.append(upper_letter[new_upper])
    
        #adds a number character to the password    
        elif(new_charcater == 3 and get_number == True):
            new_num = random.randint(1,len(numbers)-1)
            build_password.append(numbers[new_num])

        #adds a special character to the password  
        elif(new_charcater == 4 and get_special == True):
            new_special = random.randint(1,len(special_characters)-1)
            build_password.append(special_characters[new_special])
        
        
    
    for x in range(len(build_password)):
        password += build_password[x]

    print(password)
else:
    raise ValueError("Not a valid input for length to getnerate")
#Auther : Sandeep R
#Description : This python script will check password strengh based on the below condition
  #Password lengh should be more than 8 characters
  #Password must contain atleast 1 Upper case, Lower case alphabet, Digit or Special character.


def pass_digit(a):
     for i in a:
         num=i.isdigit() # isdigit() function will check whether character is digit or not. If the character is digit then it will return TRUE
         if num:
             break
     return(num)
    
# def pass_alpha(b):
#     for i in b:
#         alpha=i.isalpha()
#         if alpha:
#             break
#     return(alpha)
    
def pass_upper(c):
    for i in c:
        upper=i.isupper() #isupper() function will check whether character is Upper case alphabet  or not. If the character is Upper case alphabet then it will return TRUE
        if upper:
            break
    return(upper)

def pass_lower(d):
    for i in d:
        lower=i.islower() #islower() function will check whether character is Lower case alphabet  or not. If the character is Lower case alphabet then it will return TRUE
        if lower:
            break
    return(lower)

def pass_special(e):
    for i in e:
        special=not(i.isalnum()) #isalnum() function will check whether character is special character  or not. If the character is special character then it will return FALSE
        if special:
            break
    return(special)

def check_password_strength(result_upper,result_digit,result_special,result_lower):

    if result_digit and result_special and result_upper and result_lower:
        print("The password is matching with condition")

    # elif not(result_alpha):
    #     print("The password condition is not matching!!! we are missing alphabets letter ")
    #     exit(1)

    elif not(result_upper):
        print("The password condition is not matching!!! we are missing alphabets which are in uppercase")
        exit(1)

    elif not(result_lower):
        print("The password condition is not matching!!! we are missing alphabets which are in lowercase")
        exit(1)

    elif not(result_digit):
        print("The password condition is not matching!!! we are missing digits here ")
        exit(1)

    elif not(result_special): 
        print("The password condition is not matching!!! we are missing special characters")
        exit(1)

    else:
        print("Incorrect password!!!!!!!!!")
    

print("Enter the password")
a=input()
print(a)
pass_len=len(a) 
if pass_len<8: # This will check the length of the password whether length is less than 8 characters.
    print("Password is too small!!!! It should have 8 characters")
    exit(1)

result_digit=pass_digit(a) #This function call used to check the digit in the given password
#result_alpha=pass_alpha(a) #This function call used to check the alphabet in the given password
result_upper=pass_upper(a) #This function call used to check the upper case letter in the given password
result_special=pass_special(a) #This function call used to check the special characters in the given password
result_lower=pass_lower(a) #This function call used to check the lower case letter in the given password

check_password_strength(result_upper,result_digit,result_special,result_lower)

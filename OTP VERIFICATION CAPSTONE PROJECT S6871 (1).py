#!/usr/bin/env python
# coding: utf-8

# #                          OTP VERIFICATION SYSTEM

# ![otp.jpg](attachment:otp.jpg)

# ##### Problem Statement:

# You are tasked with developing an OTP (One-Time Password) verification system in Python. 
# The system should generate a 6-digit OTP and send it to the user's email address for verification. 
# Upon receiving the OTP, the user should enter it into the system for validation. 
# If the entered OTP matches the generated OTP, access should be granted; otherwise, access should be denied.

# ### Script :

# In[3]:


import random            # Provides functions to generate random numbers.
import smtplib           # Used to send mail to any Internet machine with an SMTP or ESMTP listener domain.

OTP = random.randint(100000,999999)      # Generating a randomm 6-digit OTP

# setting up server - This creates an SMTP server instance with the host address smtp.gmail.com and port number 587, which is commonly used for secure email transmission.

server = smtplib.SMTP('smtp.gmail.com',587)   

server.starttls()                   # Initiates a secure connection to the SMTP server using Transport Layer Security (TLS).

name = input("Enter your name: ")   #This prompts the user to input their name and stores it in the variable name.
global receiver_email
receiver_email = input("Enter ur email id:")  #This prompts the user to input their email address and stores it in the variable receiver_email.

def email_verification(receiver_email):        #  It prompts the user to re-enter the email address if it doesn't match the criteria.
    email_check1 = ["gmail","hotmail","yahoo","outlook"]
    email_check2 = [".com",".in",".org",".edu",".co.in"]
    count = 0

    for domain in email_check1:
        if domain in receiver_email:
            count+=1
    for site in email_check2:
        if site in receiver_email:
            count+=1

    if "@" not in receiver_email or count!=2:
        print("Invalid email id")
        new_receiver_email = input("Enter correct email id:")
        email_verification(new_receiver_email)
        return new_receiver_email
    return receiver_email

valid_receiver_email = email_verification(receiver_email)  # This calls the email_verification() function to validate the entered email address and stores the validated email address in the variable valid_receiver_email.
password = "wryp krww gwmz jyrw"
server.login("votp0317@gmail.com",password)     # logs in to the Gmail SMTP server using the provided email address and password.

body = "Dear "+name+","+"\n"+"\n"+"your OTP for project verification is "+str(OTP)+"."
subject = "OTP verification using python by Shabab"
message = f'subject:{subject}\n\n{body}'       # The body and subject variables are defined to compose the email message.

server.sendmail("votp0317@gmail.com",valid_receiver_email,message)  # Sends the email message to the validated receiver email address.


# The sending_otp(receiver_email) function sends a new OTP to the provided email address, verifies the received OTP, and prompts the user to enter the OTP. If the OTP is correct, it prints a success message; otherwise, it prompts to resend OTP.

def sending_otp(receiver_email):
    new_otp = random.randint(100000,999999)

    body = "Dear "+name+","+"\n"+"\n"+"your OTP is "+str(new_otp)+"."
    subject = "OTP verification using python by Shabab" 
    message = f'subject:{subject}\n\n{body}'
    server.sendmail("votp0317@gmail.com",receiver_email,message)
    print("OTP has been sent to"+receiver_email)
    received_OTP = int(input("Enter OTP:"))

    if received_OTP==new_otp:             # checks if the OTP entered by the user matches the initially generated OTP. If not, it provides options to resend OTP to the same email or enter a new email address for OTP verification.
        print("yeayy!! OTP verified")
    else:
        print("Oops!! Invalid OTP")
        print("Resending OTP.....")
        sending_otp(receiver_email)
    
print("OTP has been sent to "+valid_receiver_email)
received_OTP = int(input("Enter OTP: "))

if received_OTP==OTP:
    print("yeayy!! OTP verified")
else:
    print("Oops!! Invalid OTP")
    answer = input("Enter 'YES' to resend OTP on same email and 'NO' to enter a new email id:")
    YES = ['YES','yes','Yes']
    NO = ['NO','no','No']
    if answer in YES:
        sending_otp(valid_receiver_email)
    elif answer in NO:
        new_receiver_email = input("Enter new email id: ")
        email_verification(new_receiver_email)
        sending_otp(new_receiver_email)
    else:
        print("Invalid input")

server.quit()      # This terminates the SMTP session and closes the connection to the server.


# In[ ]:





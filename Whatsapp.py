import pywhatkit as pwk
phone_number=input('Enter mobile number with country code: ')
phone_number=('+91')+phone_number
# phone_number='+'+ phone_number
message=input('Enter the message: ')
pwk.sendwhatmsg_instantly(phone_number,message)
message="my name is tawfik shalash and this is my first program\n"

print(message)

#lets do some work on strings
print(message)
print(message.title()) #make the start of each word upper case
print((message.upper())) #print all chars with upper case
print((message.lower())) #print all chars with lower case
#\ all these function not change the string state to change string state
#you should use
message=message.lower()  #most used when we store data
#another one##########################################################
firstname="tawfik"
lastname="shalash"
full_name=f"{firstname} {lastname}"
print(f"hello, {full_name.title()}")

stringWithWhiteSpace=" python "
print(f"{stringWithWhiteSpace.rstrip()}")
print(f"{stringWithWhiteSpace.lstrip()}")

#to remove white space we use lstrinp() rstrip() strip()
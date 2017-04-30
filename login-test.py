
import requests,re,shutil,os,io,random,sys,subprocess

home_url = 'http://smartcard.stu.edu.cn/homeLogin.action'
user = '2015101015'
account = 69728
psw = '905409'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.5'
}

session = requests.Session()
res = session.get(home_url,headers=headers)

random_num = random.random() * 10000
captcha_url ='http://smartcard.stu.edu.cn/getCheckpic.action?rand='+str(random_num)
get_captcha = session.get(captcha_url).content

with open('captcha.png', 'wb') as f:
    f.write(get_captcha)
    f.close()

if sys.platform.find('darwin') >= 0:
    subprocess.call(['open', 'captcha.png'])
elif sys.platform.find('linux') >= 0:
    subprocess.call(['firefox', 'captcha.png'])
else:
    os.startfile('captcha.png')
os.system('firefox  captcha.png')
input_captcha = input('请输入验证码：')
input_captcha = str(input_captcha)

payload = {
    'imageField.x':30,
    'imageField.y':13,
    'loginType':2,
    'name':user,
    'passwd':psw,
    'rand':input_captcha,
    'userType':1
}

#登陆时实际发送表单所到之url
login_url = 'http://smartcard.stu.edu.cn/loginstudent.action'
res = session.post(login_url,headers=headers,data=payload, stream=True)


today = {
    'Submit':'+%C8%B7+%B6%A8+',
    'account':account,
    'inputObject':'all'
}

today_url = 'http://smartcard.stu.edu.cn/accounttodatTrjnObject.action'
res = session.post(today_url,headers=headers,data=today, stream=True)
html = res.content
# 保存网页
path = os.path.abspath(os.path.dirname(sys.argv[0])) #获取当前路径

with open(path+'/Today.html','wb') as f:
    f.write(html)



'''
loss = {
    'account':account,
    'passwd':psw
}

loss_url = 'http://smartcard.stu.edu.cn/accountDoLoss.action'
res = session.post(loss_url,headers=headers,data=loss, stream=True)
html = res.content
# 保存网页
with open('./loss.html','wb') as f:
    f.write(html)
'''

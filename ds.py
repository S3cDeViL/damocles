import requests
import time
import sys
import getpass

if sys.version > '3':
    pass
else:
    time.sleep(2)
    print("You Running At Python 2 \n [+] Run python3 Directory_Searcher.py [+]")
    exit()

Detect_user = getpass.getuser()
print("\nHello " + Detect_user)

def banner():
    banr = """
  ______             __    __      __                      __        ________  __  __           
 /      \           /  |  /  |    /  |                    /  |      /        |/  |/  |          
/$$$$$$  |  ______  $$/  _$$ |_   $$/   _______   ______  $$ |      $$$$$$$$/ $$/ $$ |  ______  
$$ |  $$/  /      \ /  |/ $$   |  /  | /       | /      \ $$ |      $$ |__    /  |$$ | /      \ 
$$ |      /$$$$$$  |$$ |$$$$$$/   $$ |/$$$$$$$/  $$$$$$  |$$ |      $$    |   $$ |$$ |/$$$$$$  |
$$ |   __ $$ |  $$/ $$ |  $$ | __ $$ |$$ |       /    $$ |$$ |      $$$$$/    $$ |$$ |$$    $$ |
$$ \__/  |$$ |      $$ |  $$ |/  |$$ |$$ \_____ /$$$$$$$ |$$ |      $$ |      $$ |$$ |$$$$$$$$/ 
$$    $$/ $$ |      $$ |  $$  $$/ $$ |$$       |$$    $$ |$$ |      $$ |      $$ |$$ |$$       |
 $$$$$$/  $$/       $$/    $$$$/  $$/  $$$$$$$/  $$$$$$$/ $$/       $$/       $$/ $$/  $$$$$$$/ 
                                                                                                
                                                            
                             #Coded by Shubham Gupta @s3cDevil \n                           """
    print(banr)
    time.sleep(2)
banner()


print("""
			Welcome To Critical File Finder Version : 1.0

	Choose A Number From Below : 

	[1]==> Tool Info And How it Works.

	[2]==> Enter The File Critical Finder (Default).

	[3]==> About The Tool.

	[4]==> Exit.
	""")

user_input = input("Choose A Choice >> ")
if user_input == "1":
    def tool_info():
        print(
            """Tool Based on Searching Common Files Using Dictionary To Find Critical Files On The Server \n Which Mean That Will Help The Bug Hunters To Find The Files More Quicker ! \n Use It At Your Own Risk \n @s3cDevil""")
        time.sleep(2)


    tool_info()

elif user_input == "2":
	def dirb():
		print("[+] Please Read README.MD First Necessary !  [+]")
		url_in = input("Enter The Site To Search  ==>")
		dir_dict = input("Enter Your Directory Dictionary List >>")
		dir_dicts = open(dir_dict, 'r').readlines()
		for items in dir_dicts:
			fu = items.strip()
			headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}
			url = url_in + "/" + fu
			request = requests.get(url, headers=headers)
			http = request.content
			if request.status_code >= 404 and b'404' or b'Not Found' in http:
				print("Not Found ==>  " + fu)
			else:
				print("File Has Been Found Successfully >> " + fu)
				fo = open('Critical_File_Found.txt', 'a')
				fo.write('\n')
				fo.write(url)
				fo.close()
	dirb()
elif user_input == "3":
    print("Copyright To s3cDeVil \n Use At Your Own Risk")
elif user_input == "4":
    exit()

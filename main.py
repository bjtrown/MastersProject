import pandas as pd
import subprocess
from bs4 import BeautifulSoup as BS
from netStat import netstat
from IPListFetch import fetchIP
from IPListFetch import fetchIP2
from IPListFetch import fetchIP3
from IPListFetch import ip2Geo



def menu():
    print("""\n Welcome to T-SNET by TJ
        [1] Scan your Device
        [2] Check IP's Safety
        [3] Locate IP's
        [0] Exit the Program""")

menu()
option = int(input("Enter a number: "))

while option != 0:
    if option == 1:

        netstat()

    elif option == 2:

        fetchIP()
        fetchIP2()
        fetchIP3()

    elif option == 3:
        ip2Geo()
    elif option == 0:
        #Exit function
        pass
    else:
        print("Invalid Option")
print("Thanks for using the program!")
print()
menu()
netstat()
fetchIP()
fetchIP2()
fetchIP3()
ip2Geo()











from bs4 import BeautifulSoup
import pandas as pd
import requests
import subprocess
apiKeyIP= "e262d60a4ff34a678726ccc01b154f4e"
apiKey = "a875be029c943e00620471a8cf1bd2abc6bde2e07040b9a6a03483b2fca3d3f500eedf3cd253a916"
data = pd.read_csv('scanOutput.csv')
ipList = data["Foreign IP Address"]

#Tests IP list against blocklist's list
def fetchIP():
    print("---Testing IPs against first IP list---\n")
    for ip in set(ipList):
        response = requests.get("https://api.blocklist.de/api.php?" + "ip=" + ip)
        response2 = requests.get("http://api.stopforumspam.org/api?" + "ip=" + ip)
        if response.status_code == 200 & response2.status_code == 200:
            if "attacks: 0<br />reports: 0<br />" in response.text:
                print(ip, "Does not seem to be dangerous.")
            elif "error" in response.text:
                print(ip, "has an error")
            else:
                print(ip, "was found to have: ", response.text)
        else:
            print(ip, "had a request error")


#fetchIP()

#Tests IP list against stopforumspam's list
def fetchIP2():
    print()
    print("---Testing IPs against Second IP list---\n")
    for ip in set(ipList):
        response2 = requests.get("http://api.stopforumspam.org/api?" + "ip=" + ip)
        if response2.status_code == 200:
            if "<appears>yes</appears>" in response2.text:
                print(ip, "was found to have: ", response2.text)

#fetchIP2()

#Tests IP list against abuseipdb's list
def fetchIP3():
    headers = {
        'Key': f"{apiKey}",
        'Accept': 'application/json',
    }



    for ip in set(ipList):
        params = (
        ('ipAddress', f"{ip}"),
        ('maxAgeInDays', '90'),
        ('confidenceMinimum', '25'),
        )
        response3 = requests.get('https://api.abuseipdb.com/api/v2/check', headers=headers, params=params)
        if response3.status_code == 200:
            add_to_file2 = ip + " Results: " + "\n" + response3.text + "\n"
            # print(response3.text)
            with open('AbuseIPDB Results.txt', 'a') as f:
                print(add_to_file2, file=f)
                f.close()
        else:
            print(ip, "Error: ", response3.status_code)
fetchIP3()

def ip2Geo():
    for ip in set(ipList):
            response3 = requests.get("https://api.ipgeolocation.io/ipgeo?apiKey=" + apiKeyIP + "&ip=" + ip, "&fields=country_name,state_prov,city,isp,organization" + "&output=xml")
            if response3.status_code == 200:
                add_to_file = ip + " Results: " + "\n" + response3.text + "\n"
                #print(ip, "information is:", response3.text)
                #print("")
                with open('ipGeoResults.txt', 'a') as f:
                    print(add_to_file, file=f)
                    f.close()
            else:
                print("status code was not 200")
                print("")
#ip2Geo()

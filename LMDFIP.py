import requests

#Script developed by Emmanuel Cano. This scripts gets the first 10 last malware domains related to an IP address.
#It is important to generate and paste your Umbrella Investigate Token into authorization field 
#In order to get more than 10 domains change the querystring limit variable
#More information can be found on https://docs.umbrella.com/investigate-api/docs/latest-malicious-domains-for-an-ip-1

ipaddress = input("What is the ip address to be analyzed? ")

url = "https://investigate.api.umbrella.com/ips/"+ ipaddress +"/latest_domains"

querystring = {"limit":"10"}

headers = {
    "accept": "application/json",
    "authorization": "Bearer YOUR_INVESTIGATE_TOKEN"
}

response = requests.request("GET", url, headers=headers,params=querystring)

print(response.text)

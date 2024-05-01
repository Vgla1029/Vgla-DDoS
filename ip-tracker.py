import requests

os.system("clear")


print(" __     __    _         _____               _      ___ ")
print(" \ \   / /_ _| | __ _  |_   _| __ __ _  ___| | __ |_ _|_ __ ")
print("  \ \ / / _` | |/ _` |   | || '__/ _` |/ __| |/ /  | || '_ \ ")
print("   \ V / (_| | | (_| |   | || | | (_| | (__|   <   | || |_) | ")
print("    \_/ \__, |_|\__,_|   |_||_|  \__,_|\___|_|\_\ |___| .__/ ")
print("        |___/                                         |_| ")
       
       
print(" ")
print("Vgla DDoS - Made By Vgla")
print("YouTube: https://www.youtube.com/@VglaRat")
print("GitHub: https://github.com/Vgla7")
print(" ")
ip = raw_input("Digite O Ip: ")
def ip_find():
	try:
		url = "http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query"
		mds = requests.get(url)
		data = mds.json()
		print("\n")
		
		print(f"[✓]IP : {data['query']}")
		print(f"[✓]Status : {data['status']}")
		print(f"[+]País : {data['country']}")
		print(f"[+]Região : {data['region']}")
		print(f"[+]Nome Da Região : {data['regionName']}")
		print(" ")
		print(f"[+]Cidads : {data['city']}")
		print(f"[+]Latitude : {data['lat']}")
		print(f"[+]Longitude : {data['lon']}")
		print(f"[+]Continente : {data['continent']}")
		print(f"[+]Codigo Do Continente : {data['continentCode']}")
		print(f"[+]Offset : {data['offset']}")
		print(f"[+]Currency : {data['currency']}")
		print(f"[+]Isp : {data['isp']}")
        print(" ")
		print(f"[+]Zipcode : {data['zip']}")
		print(f"[+]Org : {data['org']}")
		print(f"[+]TimeZone : {data['timezone']}")
		print(f"[+]As : {data['as']}")
		print(f"[+]AsName : {data['asname']}")
		print(f"[+]Reverse : {data['reverse']}")
		print(f"[+]Mobile? : {data['mobile']}")
		print(f"[+]Proxy? : {data['proxy']}")
		print(f"[+]Hosting : {data['hosting']}")
		
	except Exception as e:
		print (f"Error: {e}")
		
		
ip_find();

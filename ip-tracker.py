os.system("clear")


print(" __     __    _         _____               _      ___ ")
print(" \ \   / /_ _| | __ _  |_   _| __ __ _  ___| | __ |_ _|_ __ ")
print("  \ \ / / _` | |/ _` |   | || '__/ _` |/ __| |/ /  | || '_ \ ")
print("   \ V / (_| | | (_| |   | || | | (_| | (__|   <   | || |_) | ")
print("    \_/ \__, |_|\__,_|   |_||_|  \__,_|\___|_|\_\ |___| .__/ ")
print("        |___/                                         |_| ")
       
       
print
print "Vgla DDoS - Made By Vgla"
print "YouTube: https://www.youtube.com/@VglaRat"
print "GitHub: https://github.com/Vgla7"
print 
ip = raw_input("Digite O Ip: ")
def ip-find():
	try:
		response  = requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query")
		data = response.json()
		print("\n")
		
		print("[✓]IP : {data['query']}")
		print("[✓]Status : {data['status']}")
		print("[+]País : {data['country']}")
		print("[+]Região : {data['region']}")
		print("[+]Nome Da Região : {data['regionName']}")
		print
		print("[+]Cidads : {data['city']}")
		print("[+]Latitude : {data['lat']}")
		print("[+]Longitude : {data['lon']}")
		print("[+]Continente : {data['continent']}")
		print("[+]Codigo Do Continente : {data['continentCode']}")
		print("[+]Offset : {data['offset']}")
		print("[+]Currency : {data['currency']}")
		print("[+]Isp : {data['isp']}")
        print
		print("[+]Zipcode : {data['zip']}")
		print("[+]Org : {data['org']}")
		print("[+]TimeZone : {data['timezone']}")
		print("[+]As : {data['as']}")
		print("[+]AsName : {data['asname']}")
		print("[+]Reverse : {data['reverse']}")
		print("[+]Mobile? : {data['mobile']}")
		print("[+]Proxy? : {data['proxy']}")
		print("[+]Hosting : {data['hosting']}")
		
	except Exception as e:
		print (f"Error: {e}")
		
		
ip-find();

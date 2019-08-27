from requests import get

ip = get('https://api.ipify.org').text
print ip

f = open("externalip.txt", "a+")
storedIp = f.read()

if storedIp != ip:
	f.truncate(0)
	f.write(ip)

f.close()
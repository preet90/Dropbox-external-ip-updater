import dropbox
from requests import get

currentIp = get('https://api.ipify.org').text

dbx = dropbox.Dropbox('xxxxxxxxxx')

md, res = dbx.files_download('/externalip.txt')

savedIp = res.content

if savedIp != currentIp:
	dbx.files_upload(currentIp.encode(), '/externalip.txt', mode=dropbox.files.WriteMode.overwrite)
from  ftplib import FTP
from dateutil import parser
import pytz
from datetime import timedelta
host = '172.29.33.4'
port ='121'
usr = 'abhijeet'
passwd = '@b!j337'
ftps = FTP()
ftps.connect(host,port)
ftps.login(usr,passwd)
ftps.cwd('tech_charts/nse/his')
timestamp = ftps.voidcmd("MDTM nifty.csv")[4:].strip()
time = parser.parse(timestamp)
# time=time.replace(tzinfo=timezone.utc)
# print(pytz.utc.localize(time))
print(time)
print (time + timedelta(hours=5,minutes=30))
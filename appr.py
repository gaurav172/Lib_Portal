from datetime import datetime
from datetime import timedelta
import time


issue_date=datetime.now().strftime('%d/%m/%Y') 
return_date=(datetime.now() + timedelta(days=5) ).strftime('%d/%m/%Y')

from Home import *

def ApproveRequest(reqid):
	with sqlite3.connect('test.db') as conn:
		c=conn.cursor()
		c.execute("UPDATE REQUESTS SET STATUS='APPROVED',ISSUETIME=?,RETURNTIME=?,TME=? WHERE ID=?",(issue_date,return_date
,int(time.time()),reqid,))
		conn.commit()
		c.close()
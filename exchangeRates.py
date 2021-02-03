# Name : Shreya

import datetime
from datetime import date 
import urllib.request

def getLatestRates():
	""" Returns: a JSON string that is a response to a latest rates query.

	The Json string will have the attributes: rates, base and date (yyyy-mm-dd).
	"""
	url=urllib.request.urlopen("https://api.exchangeratesapi.io/latest")
	data=url.read()
	data=data.decode()
	return data

def changeBase(amount, currency, desiredCurrency, date):
	""" Outputs: a float value f.
		Only enter years in date after 2016 
	"""
	url=urllib.request.urlopen("https://api.exchangeratesapi.io/"+date+"?base="+currency)
	data=url.read()
	data=data.decode()
	data=data.replace('}','',1)

	lastdigitcur=data.index(desiredCurrency)
	till=data.index(",",lastdigitcur)
	num=float(data[(lastdigitcur+5):till])
	return num*amount
	


def printAscending(json):
	""" Output: the sorted order of the Rates 
		You don't have to return anything.
	
	Parameter:
	json: a json string to parse
	"""
	json=json.decode()
	json=json.replace('}','',1)

	no_of=json.count(',')-1
	col=[0]*no_of
	comm=[0]*no_of
	value=[0]*no_of
	
	col1st=json.index(':')+1
	col[0]=json.index(':',col1st)

	comm[0]=json.index(',')
	value[0]=float(json[col[0]+1:comm[0]])
	
	for i in range(no_of-1):
		
		col[i+1]=json.index(':',col[i]+1)
		comm[i+1]=json.index(',',comm[i]+1)
		value[i+1]=float(json[col[i+1]+1:comm[i+1]])


	col2=[0]*no_of
	comm2=[0]*no_of
	valuecurr=[0]*no_of

	col1st2=json.index(':')
	col2[0]=json.index('"',col1st2)
	comm2[0]=json.index('"',col2[0]+1)
	valuecurr[0]=json[col2[0]+1:comm2[0]]

	for i in range(no_of-1):
		col2[i+1]=json.index('"',comm2[i]+1)
		comm2[i+1]=json.index('"',col2[i+1]+1)
		valuecurr[i+1]=json[col2[i+1]+1:comm2[i+1]]


	valuenew=sorted(value)
	ind=[0]*no_of
	for i in range(no_of):
		ind[i]=value.index(valuenew[i])

	valuecurrnew=[0]*no_of
	for i in range(no_of):
		valuecurrnew[i]=valuecurr[ind[i]]

	for i in range(no_of):
		print("1 Euro= "+ str(valuenew[i])+' '+valuecurrnew[i])





def extremeFridays(startDate, endDate, currency):
	""" Output: on which friday was currency the strongest and on which was it the weakest.
		You don't have to return anything.
		Parameters: 
		stardDate and endDate: strings of the form yyyy-mm-dd. 
		exluding the trailing 0 in front of sinle digit month or day.
		currency: a string representing the currency those extremes you have to determine
	"""
	url=urllib.request.urlopen("https://api.exchangeratesapi.io/history?start_at="+startDate+"&end_at="+endDate)
	data=url.read()
	data=data.decode()

	no_dates=data.count('{')-2
	brac=data.index('{',2)
	datee=[0]*no_dates
	en=data.index(':')
	enn=data.index(':',en+1)
	datee[0]=data[(brac+2):(enn-1)]

	start=[0]*no_dates
	endd=[0]*no_dates
	start[0]=0

	for i in range(no_dates-1):
		start[i+1]=data.index('}',start[i]+1)+3
		endd[i+1]=data.index(':',start[i+1])-1
		datee[i+1]=data[start[i+1]:endd[i+1]]

	year=[0]*no_dates
	month=[0]*no_dates
	day=[0]*no_dates
	for i in range(no_dates):
		year[i]=int(datee[i][0:4])
		month[i]=int(datee[i][5:7])
		day[i]=int(datee[i][8:10])
	
	allday=[0]*no_dates
	countt=0
	for i in range(no_dates):
		dati=datetime.datetime(year[i],month[i],day[i])
		allday[i]=dati.weekday()
		if dati.weekday()==4:
			countt=countt+1
		else: pass


	friday_list=[0]*countt
	indd=[0]*countt

	indd[0]=allday.index(4)
	for i in range(countt-1):
		indd[i+1]=allday.index(4,indd[i]+1)
	
	for i in range(countt):
		friday_list[i]=datee[indd[i]]
	
	fri_index=[0]*countt
	curr_index=[0]*countt
	for i in range(countt):
		fri_index[i]=data.index(friday_list[i])
		curr_index[i]=data.index(currency,fri_index[i]+1)

	col3=[0]*countt
	comm3=[0]*countt
	curr_value=[0]*countt
	for i in range(countt):
		col3[i]=data.index(':',curr_index[i])
		comm3[i]=data.index(',',curr_index[i])
		curr_value[i]=data[col3[i]+1:comm3[i]]
		if '}' in curr_value[i]:
			curr_value[i]=curr_value[i].replace('}','')
			if '}'in curr_value[i]:
				curr_value[i]=curr_value[i].replace('}','')
				curr_value[i]=float(curr_value[i])
			else:
				curr_value[i]=float(curr_value[i])
		else:
			curr_value[i]=float(curr_value[i])
	curr_value_new=sorted(curr_value)	
	

	date_index=[0]*countt
	for i in range(countt):
		date_index[i]=curr_value.index(curr_value_new[i])

	print(currency+" was strongest on "+str(friday_list[date_index[0]])+". 1 Euro was equal to "+str(curr_value_new[0])+" "+currency)
	print(currency+" was weakest on "+str(friday_list[date_index[-1]])+". 1 Euro was equal to "+str(curr_value_new[-1])+" "+currency)
	


def findMissingDates(startDate, endDate):
	""" Output: the dates that are not present when you do a json query from startDate to endDate
		You don't have to return anything.

		Parameters: stardDate and endDate: strings of the form yyyy-mm-dd
	"""
	url=urllib.request.urlopen("https://api.exchangeratesapi.io/history?start_at="+startDate+"&end_at="+endDate)
	data=url.read()
	data=data.decode()
	

	st_date=date(int(startDate[:4]),int(startDate[5:7]),int(startDate[8:]))
	end_date=date(int(endDate[:4]),int(endDate[5:7]),int(endDate[8:]))
	
	between=end_date-st_date
	total_no_days=between.days+1
	tot_dates=[]
	for i in range(total_no_days):
		tot_dates.append(((st_date+datetime.timedelta(i)).isoformat()))

	no_dates=data.count('{')-2
	brac=data.index('{',2)
	datee=[0]*no_dates
	en=data.index(':')
	enn=data.index(':',en+1)
	datee[0]=data[(brac+2):(enn-1)]

	start=[0]*no_dates
	endd=[0]*no_dates
	start[0]=0

	for i in range(no_dates-1):
		start[i+1]=data.index('}',start[i]+1)+3
		endd[i+1]=data.index(':',start[i+1])-1
		datee[i+1]=data[start[i+1]:endd[i+1]]
	print("The following dates are not present: ")

	for i in range(len(tot_dates)):
		if tot_dates[i] not in datee:
			print(tot_dates[i])	

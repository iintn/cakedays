from datetime import datetime
import json


#Data storage
data = {}
#Line counter
counter = 0



with open("69M_reddit_accounts.csv") as f:
	#Itersting through each lind in the source file
	for line in f:
		
		#try catch so it doesn't fail when reading column titles
		try:
		
			#getting created_utc timestamp
			time = line.split(",")[2]
		
			#converting to month-day
			date = datetime.utcfromtimestamp(int(time)).strftime('%m-%d')
			
			#Adding date to data counter
			if date in data:
				data[date]+=1
			else:
				data[date]=1
				
		except:
			pass
		
		#Logging Progress
		counter+=1
		if counter % 100000 == 0:
			print ("Accounts processed:",counter)

#Saving data
with open("data.txt",'w') as f :
	f.write(json.dumps( data,indent=4, sort_keys=True))

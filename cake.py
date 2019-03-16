from PIL import Image,ImageDraw,ImageFont
import json

#Loading Data
with open("data.txt") as f:
	data = json.loads(f.read())

#February 29th's real count is 102,192. This bumps up the minimum value to show more variation in the colors. It is still the lowest value.
data["02-29"]=130000 


#Getting max and min values of the data
maxVal = max([data[x] for x in data])
minVal = min([data[x] for x in data])


#Initializing Font
font = ImageFont.truetype('fonts/helvetica bold.ttf', 64)

#Color Palettes
palette =[(253,237,134),(253,232,110),(249,208,99),(245,184,87),(240,160,75),(235,138,64),(231,114,53),(227,91,44),(199,78,41),(157,68,41),(117,60,44),(76,52,48)]
palette= [(253,235,115),(246,193,91),(237,148,69),(233 ,113 ,51),(230,103,49),(184,74,41),(138,64,43),(106,58,45)]

#Initializing information about months
monthDays = [31,29,31,30,31,30,31,31,30,31,30,31]
monthNames = ["January","February","March","April","May","June","July","August","September","October","November","December"]

#Turning Counts into a color
monthData = {}

#Iterating through each month
for a in range(1,13):
	
	monthData[str(a)] = {}
	
	#Iterating through each day
	for b in range(1,1+monthDays[a-1]):
		
		#Converting day/month ints into strings
		month = str(a)
		day = str(b)
		if len(month) == 1:
			month = "0"+month
		if len(day) ==1:
			day = "0"+day
		
		#Formatting the dates
		date = "{}-{}".format(month,day)
		
		#Getting the count between 0 and 1
		normaled = (abs(float(data[date])-minVal))/(1.1*maxVal-minVal)
		
		#Choosing a color
		bin = int(round((normaled)*(len(palette))))
		
		#assinging the color to the day in a dict
		monthData[str(a)][str(b)] = bin






#all of this stuff was originally supposed to   be in the monthDay loop, but because its the same for each month it doesnt need to be redone.
#I know that I'm not going to reuse this code for another project because I'll forget how it works and then rewrite it from scratch like I do every time. 
#So I'm just not gonna bother with making it transferable across different sizes or anything


#Initializing day box dimensions 
boxLen = 48
spacing = 32
numBoxes = 7
vertNumBoxes = monthDays[0] / numBoxes 
#Adds the extra row if remainder 
#Unnecessary because every month is not divisible by 7 consider removing 
if monthDays[0] % numBoxes != 0:
	vertNumBoxes+=1



#Calculating Width and Height for the month images
width = numBoxes*boxLen+(numBoxes-1)*spacing
height = vertNumBoxes*boxLen+(vertNumBoxes-1)*spacing


#Calculating spacing for full image
fullHorSpacing = spacing+2*boxLen
fullVertSpacing = 2*spacing+3*boxLen

#Calculating dimensions for full image
fullWidth = fullHorSpacing*5+width*4
fullHeight = fullVertSpacing*3+height*4

#Initializing full image
full = Image.new("RGB",(fullWidth,fullHeight),(255,255,255))
fullDraw = ImageDraw.Draw(full)

#Start coordinates for the day boxes
monthXCoord = fullHorSpacing
monthYCoord = fullVertSpacing*2


#Main method
for monthNum in range(len(monthDays)):
	
	#Creating image of the month
	monthImg = Image.new("RGBA",(width,height),(255,255,255,255))
	draw=ImageDraw.Draw(monthImg)
	
	#Starting y coordinate for day box and counter for day
	yCoord = 0
	dayCount = 1
	
	#How many columns 
	for y in range(vertNumBoxes):
	
		#Getting the number of days left 
		numBoxesInRow = monthDays[monthNum]-(y*numBoxes)
		#Makes sure you dont have to do more than necessary.
		if numBoxesInRow > numBoxes:
			numBoxesInRow = numBoxes
		
		
		#Centers the last row
		if y == vertNumBoxes-1:
			rowWidth = (numBoxesInRow*boxLen+(numBoxesInRow-1)*spacing)
			xCoord = (width-rowWidth)/2
		else:
			xCoord= 0
		
		
		#Putting the day boxes on the month image
		for x in range(numBoxesInRow):
			
			#getting the color for the day
			color = palette[monthData[str(monthNum+1)][str(dayCount)]]
			
			#putting the day on there
			draw.rectangle(((xCoord,yCoord),(xCoord+boxLen,yCoord+boxLen)),fill=color)
			
			#Incrementing x coordinate position and counter
			xCoord += boxLen+spacing
			dayCount+=1
		
		#Incrementing y coordinate position
		yCoord += boxLen+spacing
	
	#Pasting the month onto the full image
	full.paste(monthImg,(monthXCoord,monthYCoord))
	
	#Putting month names on the image
	fontsize = font.getsize(monthNames[monthNum])
	fullDraw.text(( monthXCoord,monthYCoord-int(fontsize[1]*1.4)),monthNames[monthNum],(0,0,0),font=font)
	
	#incrementing month coordinates
	monthXCoord += fullHorSpacing+width
	if (monthNum+1) % 4 == 0:
		monthYCoord += fullVertSpacing+height
		monthXCoord = fullHorSpacing
	



#Adding title to image
title = "Reddit's Most Common Cakeday"
font = ImageFont.truetype('fonts/helvetica.ttf', 92)
fontsize = font.getsize(title)
fullDraw.text(((full.size[0]-fontsize[0])/2,fullVertSpacing/2),title,fill=(0,0,0),font=font)



#Saving final result
full.save("cakedays.png")
#full.show()

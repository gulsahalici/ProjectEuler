days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
months=["January","February","March","April","May","June","July","August","September","October","November","December"]
dayCount=0
monthCount=0
firstSundays=0

for year in range(1901,2000):
    while monthCount!=12:
        counter=0
        limit=0
        if monthCount==3 or monthCount==5 or monthCount==8 or monthCount==10:
            limit=30
        else:
            if monthCount==1:
                if year%4==0:
                    if year%100==0:
                        if year%400==0:
                            limit=29
                        else:
                            limit=28
                    else:
                        limit=29
                else:
                    limit=28
            else:
                limit=31

        while counter!=limit and dayCount!=7:
            date=str(counter+1)+" "+str(months[monthCount])+" "+str(year)+" "+str(days[dayCount])
            #print(date)
            if dayCount==6 and counter==0:
                firstSundays+=1
        
            dayCount+=1
            counter+=1
            if dayCount==7:
                dayCount=0
        monthCount+=1
    monthCount=0

print(firstSundays)

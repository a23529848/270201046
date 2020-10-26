##Current Time

currentHour=6
currentMinute=52
easyPaceMinute=8
tempoMinute=6

##Distance

easyMiles=1+2
tempoMiles=3

#total Time (seconds)

runTime=easyPaceMinute*easyMiles*60 + tempoMinute*tempoMiles*60
##converts hour and minute to seconds
currentTime=currentHour*3600 + currentMinute*60
totalTime=currentTime+runTime
##converts from seconds to last time
totalHour=totalTime/3600
totalMinutes = (totalTime % 3600) / 60

newTime = int(totalHour),":",totalMinutes
##
print(newTime)



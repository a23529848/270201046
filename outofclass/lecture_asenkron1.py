theTime=float(input("Please Enter Current Time="))
theMinuteOfTime=theTime-int(theTime)

the_minute=theMinuteOfTime*100

the_Minute=int(the_minute)+1

print(the_Minute)

speedEasyPace=1/8
speedTempo=1/6

totalRunTime= 1/speedEasyPace + 3/speedTempo + 2/speedEasyPace ##minute

print(totalRunTime)

totalTime=totalRunTime+the_Minute

print(totalTime)

realTotalTime=int(totalTime)+1



HomeTime=((int(theTime)+1)+(realTotalTime%60)/100)-0.01

print(HomeTime)

x=input('Your name: \n')
y=input('Your lab grade: \n')
z=input('Your midterm grade: \n')
t=input('Your final grade: \n')
labgrade= float(y) * 0.25
midtermgrade = float(z) * 0.35
finalgrade = float(t) * 0.4
lastscore = labgrade + midtermgrade + finalgrade
print('Name: ' + str(x))
print('Lab: ' + str(labgrade))
print('Midterm: ' + str(midtermgrade))
print('Final: ' + str(finalgrade))
print('Last score: ' + str(lastscore))
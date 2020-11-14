from matplotlib import pyplot as plt

from functions import makeList

li = makeList('ProjectData\Data.nh.txt')
print(li)
if li[0] == ('1990', '0.412'):  #if statements to check specific data points
    print('Check 1: Passed')
else:
    print('Check 1 Failed')
if li[14] == ('2004', '0.604'):
    print('Check 2: Passed')
else:
    print('Check 2: Failed')
if li[29] == ('2019', '0.957'):
    print('Check 3: Passed')
else:
    print('Check 3: Failed')


from functions import plotList

plotList('Test', li, 'r', 'Year', 'Temperature')
plt.savefig('testplot.png')
plt.show()


from functions import correctFile  # Changed function ==> test needs adjustment

correctFile('ProjectData\\Data.monthly_nh.txt', 'Dt.mn.nh_c_test.txt')  #calls function on one of the data sets
f = open('Dt.mn.nh_c_test.txt', 'r')  #opens file
testline = f.readlines()  #places each line as an entry in the list
testlist = testline[0].split(',')  #takes a line of the larger list and creates a smaller list of the entries that were separated by commas
line1 = 1850 + 1/12  #the year and month are taken from the original uncorrected file and combined as they would be via the function
if testlist[0] == f'{line1:.2f}':  #if statements to test whether the values are what they should be
    print('Check 1 of CorrectFile: Passed')
else:
    print('Check 1 of CorrectFile: Failed')
line100 = 1858 + 4/12  #repeating test for line 100
testlist1 = testline[99].split(',')
if testlist1[0] == f'{line100:.2f}':
    print('Check 2 of CorrectFile: Passed')
else:
    print('Check 2 of CorrectFile: Failed')
line400 = 1883 + 4/12  #repeating test for line 400
testlist2 = testline[399].split(',')
if testlist2[0] == f'{line400:.2f}':
    print('Check 3 of CorrectFile: Passed')
else:
    print('Check 3 of CorrectFile: Failed')


from functions import makeAverageList
months = 6
Avgtestlist = makeAverageList('Data.monthly_nh_c.txt', 1, 2, months)
if len(Avgtestlist) == int(2037/months):  #if statement to test that the list produced is the length expected
    print('Length Check of AvgList: Passed')
else:
    print('Length Check of AvgList: Failed')
testAvg1 =(f'{(1850.08+1850.17+1850.25+1850.33+1850.42+1850.50)/6:.2f}', f'{(-0.844+-0.053+-0.699+-0.586+-0.420+-0.002)/6:.2f}')
if Avgtestlist[0] == testAvg1:  #^creates a tuple that should be the first entry in the list and uses an if statement to evaluate it
    print('Check of AvgList entry 1: Passed')
else:
    print('Check of AvgList entry 1: Failed')
testAvg2 = (f'{(1875.50+1875.08+1875.17+1875.25+1875.33+1875.42)/6:.2f}', f'{(-0.058+-0.916+-1.066+-0.882+-0.650+-0.123)/6:.2f}')
if Avgtestlist[50] == testAvg2:
    print('Check of AvgList entry 50: Passed')
else:
    print('Check of AvgList entry 50: Failed')
testAvg3 = (f'{(1900.50+1900.08+1900.17+1900.25+1900.33+1900.42)/6:.2f}', f'{(-0.002+-0.334+-0.364+-0.213+-0.179+-0.138)/6:.2f}')
if Avgtestlist[100] == testAvg3:
    print('Check of AvgList entry 100: Passed')
else:
    print('Check of AvgList entry 100: Failed')

months2 = 3
Avgtestlist2 = makeAverageList('Data.monthly_ns_c.txt', 1, 2, months2)
if len(Avgtestlist2) == int(2037/months2):
    print('Length Check of AvgList2: Passed')
else:
    print('Check of AvgList2: Failed')
testAvg4 = (f'{(1850.08+1850.17+1850.25)/3:.2f}', f'{(-0.7+-0.286+-0.732)/3:.2f}')
if Avgtestlist2[0] == testAvg4:
    print('Check of AvgList2 entry 1: Passed')
else:
    print('Check of AvgList2 entry 1: Failed')

months3 = 2
Avgtestlist3 = makeAverageList('Data.monthly_sh_c.txt', 1, 2, months3)
if len(Avgtestlist3) == int(2037/months3):
    print('Length Check of AvgList3: Passed')
else:
    print('Length Check of AvgList3: Failed')
testAvg5 = (f'{(1850.08+1850.17)/2:.2f}', f'{(-0.555+-0.522)/2:.2f}')
if Avgtestlist3[0] == testAvg5:
    print('Check of AvgList3 entry 1: Passed')
else:
    print('Check of AvgList3: Failed')

from functions import plotWithError

# To test plotWithError, a plot with error bands is made and specific points corresponding to values calculated earlier
# are plotted and should show along the curve if the plot is working correctly
testErrorlist1 = makeAverageList('Data.monthly_nh_c.txt', 1, 9, months)
testErrorlist2 = makeAverageList('Data.monthly_nh_c.txt', 1, 10, months)

plotWithError('TEST', 'Uncertainty', Avgtestlist, testErrorlist2, testErrorlist1, 'blue', 'skyblue', 'Year',
              'Temperature Anomaly')
plt.plot(float(testAvg1[0]), float(testAvg1[1]), 'r.')
plt.plot(float(testAvg2[0]), float(testAvg2[1]), 'r.')
plt.plot(float(testAvg3[0]), float(testAvg3[1]), 'r.')
plt.show()

# Same plot zoomed into the region with the specific plot points to confirm they are along the nominal curve
plotWithError('TEST', 'Uncertainty', Avgtestlist, testErrorlist2, testErrorlist1, 'blue', 'skyblue', 'Year',
              'Temperature Anomaly')
plt.plot(float(testAvg1[0]), float(testAvg1[1]), 'r.')
plt.plot(float(testAvg2[0]), float(testAvg2[1]), 'r.')
plt.plot(float(testAvg3[0]), float(testAvg3[1]), 'r.')
plt.axis([1850, 1920, -1, 1])
plt.show()


# Classes testing
from classes import Analysis

# No reason to create new corrected files

test_class = Analysis()
test_class.addFile('Data.monthly_nh_c.txt', 'Northern Hemisphere')
test_class.addFile('Data.monthly_sh_c.txt', 'Southern Hemisphere')
# PrintInfo() prints all input files, titles, data lists and uncertainties for that instance
test_class.printInfo()
if len(test_class.titles) == 2 and len(test_class.input_files) == 2:
    print('\n nh_sh has correct list lengths \n')

# Testing update lists using the same columns and granularity as used in makeAverageList() to compare results
columns = (1, 2, 9, 10, 11, 12)
test_class.updatelists(columns, 6, 1, 2037, 'Uncertainty 1', 'Uncertainty 2')
test_class.printInfo()

# The first entry of self.points should contain an averaged list over 6 months for the Northern Hemisphere data which
# means that it should have the same length as the list made in the previous test
if len(test_class.points[0]) == len(Avgtestlist):
    print('\ntest_class.points is the correct length')
else:
    print('\nincorrect length')

if test_class.points[0][0][0] == float(testAvg1[0]):
    print('\nCorrect average of first year value ')

# This loop will sum each value of the first two columns averaged by makeAverageList and updateLists and in theory they
# should be equal if the two are equivalent
year1 = 0
year2 = 0
temp1 = 0
temp2 = 0
for a, b in Avgtestlist:
    year1 = year1 + float(a)
    temp1 = temp1 + float(b)
for c, d, e, f, g, h in test_class.points[0]:
    year2 = year2 + float(c)
    temp2 = temp2 + float(d)

if year1 == year2 and temp1 == temp2:
    print('\nAll values are for temperature and year are equal')
else:
    print('\nValues are for temperature and year are not equal')

# Blue plot with 2 error bands, averaged over 6 months
test_class.plotWithErrors(1, 1, 2, 2)
plt.show()
# Green plot with 1 error band, averaged over 12 months
test_class.updatelists(columns, 12, 1, 2037, 'Uncertainty 1', 'Uncertainty 2')
test_class.plotWithErrors(1, 3, 1, 3)
plt.show()
# Red plot with no error bands, averaged over 12 months
test_class.plotWithErrors(2, 4, 0, 1)
plt.show()

# Swapping axes and changing colour to observe if changes happen correctly, should be a reflection in the line y=x
# Red scatter plot Northern vs Southern
test_class.scatterPlot(1, 2, 1, 2, 1)
plt.show()
# Blue scatter plot Southern vs Northern
test_class.scatterPlot(4, 3, 2, 1, 2)
plt.show()

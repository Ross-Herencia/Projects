from matplotlib import pyplot as plt
from functions import makeList
from functions import plotList
from functions import correctFile
from functions import makeAverageList
from functions import plotWithError
from classes import Analysis
from functions import correctFile2
# Part 1

data_list = makeList('ProjectData\\Data.nh.txt')
plotList('North hemisphere', data_list, 'slateblue', 'year', 'temperature anomalies')
plt.savefig('A3part1.png')
plt.show()

# Part 2

# Column 1 corrected/comma-separated monthly data files denoted with _c
correctFile('ProjectData\\Data.monthly_nh.txt', 'Data.monthly_nh_c.txt')
correctFile('ProjectData\\Data.monthly_ns.txt', 'Data.monthly_ns_c.txt')
correctFile('ProjectData\\Data.monthly_sh.txt', 'Data.monthly_sh_c.txt')
correctFile('ProjectData\\Data.monthly_tropical.txt', 'Data.monthly_tropical_c.txt')

# Nominal data comparison plot 48 month resolution
granularity = 48  # measured in months
nh = makeAverageList('Data.monthly_nh_c.txt', 1, 2, granularity)
ns = makeAverageList('Data.monthly_ns_c.txt', 1, 2, granularity)
sh = makeAverageList('Data.monthly_sh_c.txt', 1, 2, granularity)
tropical = makeAverageList('Data.monthly_tropical_c.txt', 1, 2, granularity)

plotList('Northern Hemisphere', nh, 'blue', 'Year', 'Temperature Anomaly')
plotList('Southern Hemisphere', sh, 'red','Year', 'Temperature Anomaly')
plotList('Tropics', tropical, 'orange', 'Year', 'Temperature Anomaly')
plotList('Global Average', ns, 'green', 'Year', 'Temperature Anomaly')
plt.savefig('A3part2a.png')
plt.show()

# Nominal data comparison plot 1 year resolution
granularity_1year = 12
nh_1y = makeAverageList('Data.monthly_nh_c.txt', 1, 2, granularity_1year)
ns_1y = makeAverageList('Data.monthly_ns_c.txt', 1, 2, granularity_1year)
sh_1y = makeAverageList('Data.monthly_sh_c.txt', 1, 2, granularity_1year)
tropical_1y = makeAverageList('Data.monthly_tropical_c.txt', 1, 2, granularity_1year)

plotList('Northern Hemisphere', nh_1y, 'blue', 'Year', 'Temperature Anomaly')
plotList('Southern Hemisphere', sh_1y, 'red','Year', 'Temperature Anomaly')
plotList('Tropics', tropical_1y, 'orange', 'Year', 'Temperature Anomaly')
plotList('Global Average', ns_1y, 'green', 'Year', 'Temperature Anomaly')
plt.savefig('A3part2b.png')
plt.show()


# Nominal data comparison plot 1 month resolution
granularity_1month = 1
nh_1m = makeAverageList('Data.monthly_nh_c.txt', 1, 2, granularity_1month)
ns_1m = makeAverageList('Data.monthly_ns_c.txt', 1, 2, granularity_1month)
sh_1m = makeAverageList('Data.monthly_sh_c.txt', 1, 2, granularity_1month)
tropical_1m = makeAverageList('Data.monthly_tropical_c.txt', 1, 2, granularity_1month)

plotList('Northern Hemisphere', nh_1m, 'blue', 'Year', 'Temperature Anomaly')
plotList('Southern Hemisphere', sh_1m, 'red','Year', 'Temperature Anomaly')
plotList('Tropics', tropical_1m, 'orange', 'Year', 'Temperature Anomaly')
plotList('Global Average', ns_1m, 'green', 'Year', 'Temperature Anomaly')
plt.savefig('A3part2c.png')
plt.show()


# Nominal data comparison plot 10 year resolution
granularity_10years = 120
nh_10y = makeAverageList('Data.monthly_nh_c.txt', 1, 2, granularity_10years)
ns_10y = makeAverageList('Data.monthly_ns_c.txt', 1, 2, granularity_10years)
sh_10y = makeAverageList('Data.monthly_sh_c.txt', 1, 2, granularity_10years)
tropical_10y = makeAverageList('Data.monthly_tropical_c.txt', 1, 2, granularity_10years)

plotList('Northern Hemisphere', nh_10y, 'blue', 'Year', 'Temperature Anomaly')
plotList('Southern Hemisphere', sh_10y, 'red','Year', 'Temperature Anomaly')
plotList('Tropics', tropical_10y, 'orange', 'Year', 'Temperature Anomaly')
plotList('Global Average', ns_10y, 'green', 'Year', 'Temperature Anomaly')
plt.savefig('A3part2d.png')
plt.show()

# Uncertainty lists for northern hemisphere (over 48 month average)
nh_error1 = makeAverageList('Data.monthly_nh_c.txt', 1, 9, granularity)
nh_error2 = makeAverageList('Data.monthly_nh_c.txt', 1, 10, granularity)
nh_error3 = makeAverageList('Data.monthly_nh_c.txt', 1, 11, granularity)
nh_error4 = makeAverageList('Data.monthly_nh_c.txt', 1, 12 , granularity)

# Uncertainty lists for global average (over 48 month average)
ns_error1 = makeAverageList('Data.monthly_ns_c.txt', 1, 9, granularity)
ns_error2 = makeAverageList('Data.monthly_ns_c.txt', 1, 10, granularity)
ns_error3 = makeAverageList('Data.monthly_ns_c.txt', 1, 11, granularity)
ns_error4 = makeAverageList('Data.monthly_ns_c.txt', 1, 12, granularity)

# Uncertainty lists for southern hemisphere (over 48 month average)
sh_error1 = makeAverageList('Data.monthly_sh_c.txt', 1, 9, granularity)
sh_error2 = makeAverageList('Data.monthly_sh_c.txt', 1, 10, granularity)
sh_error3 = makeAverageList('Data.monthly_sh_c.txt', 1, 11, granularity)
sh_error4 = makeAverageList('Data.monthly_sh_c.txt', 1, 12, granularity)

# Uncertainty lists for tropics (over 48 month average)
tropical_error1 = makeAverageList('Data.monthly_tropical_c.txt', 1, 9, granularity)
tropical_error2 = makeAverageList('Data.monthly_tropical_c.txt', 1, 10, granularity)
tropical_error3 = makeAverageList('Data.monthly_tropical_c.txt', 1, 11, granularity)
tropical_error4 = makeAverageList('Data.monthly_tropical_c.txt', 1, 12, granularity)

# Northern Hemisphere plot
plotWithError('Northern Hemisphere', 'Measurement/Sampling/Bias/Coverage', nh, nh_error3, nh_error4,
              'blue','paleturquoise', 'Year', 'Temperature Anomaly')
plotWithError('Northern Hemisphere','Measurement/sampling/Bias', nh, nh_error1, nh_error2, 'blue','skyblue',
              'Year', 'Temperature Anomaly')
plt.savefig('A3part2e.png')
plt.show()

# Southern Hemisphere plot
plotWithError('Southern Hemisphere', 'Measurement/Sampling/Bias/Coverage', sh, sh_error3, sh_error4,
              'blue', 'paleturquoise', 'Year', 'Temperature Anomaly')
plotWithError('Southern Hemisphere', 'Measurement/sampling/Bias', sh, sh_error1,sh_error2,'blue', 'skyblue',
              'Year', 'Temperature Anomaly')
plt.savefig('A3part2f.png')
plt.show()

# Tropical plot
plotWithError('Tropics', 'Measurement/Sampling/Bias/Coverage', tropical, tropical_error3, tropical_error4,
              'blue', 'paleturquoise', 'Year', 'Temperature Anomaly')
plotWithError('Tropics', 'Measurement/Sampling/Bias', tropical, tropical_error1, tropical_error2, 'blue',
              'skyblue', 'Year', 'Temperature Anomaly')
plt.savefig('A3part2g.png')
plt.show()

# Global Average plot
plotWithError('Global Average', 'Measurement/Sampling/Bias/Coverage', ns, ns_error3, ns_error4, 'blue',
              'paleturquoise', 'Year', 'Temperature Anomaly')
plotWithError('Global Average', 'Measurement/Sampling/Bias', ns, ns_error1, ns_error2, 'blue', 'skyblue', 'Year',
              'Temperature Anomaly')
plt.savefig('A3part2h.png')
plt.show()

# Part 3

# New instance of monthly data
nh_sh_tropical = Analysis()
nh_sh_tropical.addFile('Data.monthly_nh_c.txt', 'Northern Hemisphere')
nh_sh_tropical.addFile('Data.monthly_sh_c.txt', 'Southern Hemisphere')
nh_sh_tropical.addFile('Data.monthly_tropical_c.txt', 'Tropics')

#  Colour code: 1 = red, 2 = blue, 3 = green, 4 = black
#  Was originally referenced with a string like 'red', but changed it so I could plot with a loop more easily on the
#  land and sea data.

plotting_columns = (1, 2, 9, 10, 11, 12)
# 30 years / 2 month granularity
nh_sh_tropical.updatelists(plotting_columns, 2, 1677, 2037, 'Measurement/Sampling/Bias',
                           'Measurement/Sampling/Bias/Coverage')
# Individual plot of each region with error bands
nh_sh_tropical.plotWithErrors(1, 1, 2, 1)
plt.savefig('A3part3a.png')
plt.show()
nh_sh_tropical.plotWithErrors(2, 2, 2, 2)
plt.savefig('A3part3b.png')
plt.show()
nh_sh_tropical.plotWithErrors(3, 3, 2, 3)
plt.savefig('A3part3c.png')
plt.show()

# plot of 3 nominal curves with no error bands
nh_sh_tropical.plotWithErrors(1, 1, 0, 3)
nh_sh_tropical.plotWithErrors(2, 2, 0, 2)
nh_sh_tropical.plotWithErrors(3, 3, 0, 1)
plt.savefig('A3part3d.png')
plt.show()

# 10 years / 2 month granularity
nh_sh_tropical.updatelists(plotting_columns, 2, 1917, 2037, 'Measurement/Sampling/Bias',
                           'Measurement/Sampling/Bias/Coverage')
# Individual plot of each region with error bands
nh_sh_tropical.plotWithErrors(1, 4, 2, 1)
plt.savefig('A3part3e.png')
plt.show()
nh_sh_tropical.plotWithErrors(2, 5, 2, 2)
plt.savefig('A3part3f.png')
plt.show()
nh_sh_tropical.plotWithErrors(3, 6, 2, 3)
plt.savefig('A3part3g.png')
plt.show()

# PLot of 3 nominal curves without errors
nh_sh_tropical.plotWithErrors(1, 4, 0, 3)
nh_sh_tropical.plotWithErrors(2, 5, 0, 2)
nh_sh_tropical.plotWithErrors(3, 6, 0, 1)
plt.savefig('A3part3h.png')
plt.show()

# Scatter plots
# All data / 2 month granularity
nh_sh_tropical.updatelists(plotting_columns, 2, 1, 2037)
nh_sh_tropical.scatterPlot(7, 8, 1, 2, 1)
plt.savefig('A3part3i.png')
plt.show()
nh_sh_tropical.scatterPlot(8, 9, 2, 3, 2)
plt.savefig('A3part3j.png')
plt.show()
nh_sh_tropical.scatterPlot(7, 9, 1, 3, 3)
plt.savefig('A3part3k.png')
plt.show()

# All Data / 12 month granularity
nh_sh_tropical.updatelists(plotting_columns, 12, 1, 2037)
nh_sh_tropical.scatterPlot(10, 11, 1, 2, 1)
plt.savefig('A3part3l.png')
plt.show()
nh_sh_tropical.scatterPlot(11, 12, 2, 3, 2)
plt.savefig('A3part3m.png')
plt.show()
nh_sh_tropical.scatterPlot(10, 12, 1, 3, 3)
plt.savefig('A3part3n.png')
plt.show()


# Creating corrected files for land and sea data denoted by _c
# Column 14 has the yearly averaged values
correctFile2('ProjectData\\Data.land.nh.txt', 'Data.land.nh_c.txt')
correctFile2('ProjectData\\Data.land.ns.txt', 'Data.land.ns_c.txt')
correctFile2('ProjectData\\Data.land.sh.txt', 'Data.land.sh_c.txt')
correctFile2('ProjectData\\Data.sea.nh.txt', 'Data.sea.nh_c.txt')
correctFile2('ProjectData\\Data.sea.ns.txt', 'Data.sea.ns_c.txt')
correctFile2('ProjectData\\Data.sea.sh.txt', 'Data.sea.sh_c.txt')


# New instance of Analysis containing the corrected land and sea data files
land_sea = Analysis()
land_sea.addFile('Data.land.nh_c.txt', 'Land: Northern Hemisphere')
land_sea.addFile('Data.land.sh_c.txt', 'Land: Southern Hemisphere')
land_sea.addFile('Data.sea.nh_c.txt', 'Sea: Northern Hemisphere')
land_sea.addFile('Data.sea.sh_c.txt', 'Sea: Southern Hemisphere')
land_sea.addFile('Data.land.ns_c.txt', 'Land: Global Average')
land_sea.addFile('Data.sea.ns_c.txt', 'Sea: Global Average')

plot_columns = (1, 14, 2, 3, 4, 5)  # only the first 2 values will be used (plotting without errors)

# The document says to plot the four nominal data curves, which I have taken to mean excluding the global averages
# The loop uses two counters to keep track of data position (n) and title/colour code position (m)
# m is reset to 1 such that only four data lists are used for each plot corresponding to the four nominal curves
# Since there are 4 data sets and four colours, m can be used for both, but another variable could be introduced if not

land_sea.updatelists(plot_columns, 2, 1, 170)
land_sea.updatelists(plot_columns, 4, 1, 170)
land_sea.updatelists(plot_columns, 10, 1, 170)
n = 1
m = 1
for i in range(1, 19):
    if n < 5 and m <= 4:
        land_sea.plotWithErrors(m, n, 0, m)
        plt.savefig('A3part3o.png')
    if 11 > n >= 7 and m <= 4:
        land_sea.plotWithErrors(m, n, 0, m)
        plt.savefig('A3part3p.png')
    if 17 > n >= 13 and m <= 4:
        land_sea.plotWithErrors(m, n, 0, m)
        plt.savefig('A3part3q.png')
    n = n + 1
    m = m + 1
    if m == 7:
        plt.show()
        m = 1

# Bool introduced to allow the x and y titles to be overwritten using the instance titles
# Scatter comparing land and sea of Northern Hemisphere against land and sea of Southern Hemisphere (2 year average)
land_sea.x_title = 'Land Temperature Anomaly'
land_sea.y_title = 'Sea Temperature Anomaly'
land_sea.scatterPlot(1, 3, 1, 3, 1, True)
land_sea.scatterPlot(2, 4, 2, 4, 2, True)
plt.savefig('A3part3r.png')
plt.show()
# Scatter comparing global land and sea temperature anomalies (2 year average)
land_sea.scatterPlot(5, 6, 5, 6, 1)
plt.savefig('A3part3s.png')
plt.show()

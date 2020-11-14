from matplotlib import pyplot as plt


class Analysis:
    def __init__(self, x_title='Year', y_title='Temperature Anomaly'):
        self.x_title = x_title
        self.y_title = y_title
        self.input_files = []
        self.titles = []
        self.points = []
        self.uncertainty1 = []
        self.uncertainty2 = []
        # Nested dictionary of 4 primary colours with two lighter variants for error bands
        self.colour = {1: {1: 'crimson', 2: 'lightcoral', 3: 'mistyrose'},
                       2: {1: 'blue', 2: 'skyblue', 3: 'paleturquoise'},
                       3: {1: 'green', 2: 'mediumseagreen', 3: 'mediumspringgreen'},
                       4: {1: 'black', 2: 'grey', 3: 'lightgrey'}}

    def addFile(self, input_file, title):
        self.input_files.append(input_file)
        self.titles.append(title)

    def printInfo(self): # Prints the length followed by the contents of that instances lists
        print('\nFiles: ', len(self.input_files), self.input_files, '\n')
        print('Titles: ', len(self.titles), self.titles, '\n')
        print('Data lists: ', len(self.points), self.points, '\n')
        print('Uncertainties: \n','Uncertainty list 1 ', len(self.uncertainty1), self.uncertainty1, '\n',
              'Uncertainty list 2 ', len(self.uncertainty2), self.uncertainty2)

    def plotPoints(self, points):
        x = []
        y = []
        for a, b in self.points:
            x.append(float(f'{a:.3f}'))
            y.append(float(f'{b:.3f}'))
        plt.xlabel(self.x_title)
        plt.ylabel(self.y_title)
        plt.plot(x, y, color='blue')

    def updatelists(self, tuple6c, granularity=12, minrow=1, maxrow=100, uncertainty1='U1', uncertainty2='U2'):
        for a in self.input_files:
            file = open(a, 'r')
            data_list = file.readlines()
            n = 0
            points = []
            data = data_list[minrow-1:maxrow+1]  # Creating a new list containing entries between the min and max
            for b in range(int(len(data)/granularity)):
                value1 = 0
                value2 = 0
                value3 = 0
                value4 = 0
                value5 = 0
                value6 = 0
                for c in range(granularity):
                    row = data[n].split(',')
                    value1 = value1 + float(row[tuple6c[0]-1])  # Column values are summed for the amount of months
                    value2 = value2 + float(row[tuple6c[1]-1])  # specified in granularity
                    value3 = value3 + float(row[tuple6c[2]-1])
                    value4 = value4 + float(row[tuple6c[3]-1])
                    value5 = value5 + float(row[tuple6c[4]-1])
                    value6 = value6 + float(row[tuple6c[5]-1])
                    n = n + 1
                tuple6v = (float(f'{value1/granularity:.2f}'),float(f'{value2/granularity:.2f}'),
                           float(f'{value3/granularity:.2f}'),float(f'{value4/granularity:.2f}'),
                           float(f'{value5/granularity:.2f}'),float(f'{value6/granularity:.2f}'))
                points.append(tuple6v)  # Average is taken and data is tupled and append to an internal list for that
            self.points.append(points)  # file then to the instance list
            self.uncertainty1.append(uncertainty1)
            self.uncertainty2.append(uncertainty2)

    def plotWithErrors(self, title_position, data_position, errorbands, colourcode):
        points_x = []
        points_y = []
        error1_upper = []
        error1_lower = []
        error2_upper = []
        error2_lower = []
        for a,b,c,d,e,f in self.points[data_position-1]:  # Putting data into lists for plotting
            points_x.append(float(a))
            points_y.append(float(b))
            error1_lower.append(float(c))
            error1_upper.append(float(d))
            error2_lower.append(float(e))
            error2_upper.append(float(f))
        plt.xlabel(self.x_title)
        plt.ylabel(self.y_title)
        if errorbands == 2:  # Condition statement to check how many error bands are required
            plt.fill_between(points_x, error2_lower, error2_upper, color=self.colour[colourcode][3],
                             label=self.uncertainty2[data_position-1])
            plt.fill_between(points_x, error1_lower, error1_upper, color=self.colour[colourcode][2],
                             label=self.uncertainty1[data_position-1])
            plt.plot(points_x, points_y, self.colour[colourcode][1], label=self.titles[title_position - 1])
        elif errorbands == 1:
            plt.fill_between(points_x, error1_lower, error1_upper, color=self.colour[colourcode][2],
                             label=self.uncertainty1[data_position-1])
            plt.plot(points_x,points_y, self.colour[colourcode][1], label=self.titles[title_position - 1])
        elif errorbands == 0:
            plt.plot(points_x, points_y, self.colour[colourcode][1], label=self.titles[title_position - 1])
        plt.legend()

    def scatterPlot(self, data_position1, data_position2, title_position1, title_position2, colour=1, titles=False):
        points_x = []
        points_y = []
        for a, b, c, d, e, f in self.points[data_position1 - 1]:  # pulling out temperature data from the 6-tuple
            points_x.append(float(b))
        for g, h, i, j, k, l in self.points[data_position2 - 1]:
            points_y.append(float(h))
        if not titles:  # Check to see if axis title override is true or false
            plt.xlabel(self.titles[title_position1 - 1] + ' Temperature Anomaly')  # Uses file title from titles list
            plt.ylabel(self.titles[title_position2 - 1] + ' Temperature Anomaly')
            plt.plot(points_x, points_y, '.', color=self.colour[colour][1],
                     label=self.titles[title_position1 - 1] + ' / ' + self.titles[title_position2 - 1])
        else:
            plt.xlabel(self.x_title)  # Uses specific axis titles for that instance
            plt.ylabel(self.y_title)
            plt.plot(points_x, points_y, '.', color=self.colour[colour][1],
                     label=self.titles[title_position1 - 1] + ' / ' + self.titles[title_position2 - 1])
        plt.legend()

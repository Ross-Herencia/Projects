from matplotlib import pyplot as plt

# Part 1

def makeList(filename):
    f = open(filename, 'r')
    data_list = []
    file_length = len(f.readlines())
    f.seek(0)

    for i in range(file_length):
        line = f.readline()
        line_split = line.split()
        line_tuple = (line_split[0], line_split[1])
        data_list.append(line_tuple)

    return data_list


def plotList(plotname, data_list, colour, xtitle, ytitle):
    x = []
    y = []
    for i, j in data_list:
        x.append(float(i))
        y.append(float(j))

    plt.plot(x, y, colour, label=plotname)
    plt.legend()
    plt.xlabel(xtitle)
    plt.ylabel(ytitle)

# Part 2
# Note that columns and rows are always considered to start at 1 and so must be subtracted by 1 to index in lists

# Loops over the list of lines created from readlines() and splits at the empty space
# Writes a new file with comma-separated values and each rows values unchanged except for column 1


def correctFile(input_file, output_file):
    data = open(input_file, 'r')
    corrected_data = open(output_file, 'w')
    data_list = data.readlines()

    for i in range(len(data_list)):
        data_split = data_list[i].split()
        column1 = data_split[0].split('/')
        new_column1 = float(column1[0]) + float(column1[1])/12  # Changes column 1 into decimal format year.(month/12)
        corrected_data.write(f'{new_column1:.2f}' + ',')
        for j in data_split[1:12]:
            corrected_data.write(j + ',')
        corrected_data.write('\n')
    data.close()
    corrected_data.close()


# Uses the corrected data files to make lists of floats that can be used to plot. The lists are made up of averaged
# values of two desired columns, taken over a desired amount of months.

def makeAverageList(input_file, x_column=1, y_column=2, months=12):
    data = open(input_file, 'r')
    data_list = data.readlines()
    points = []
    n = 0  # n is used to track row number so that it does not average the same entry twice
    for i in range(int(len(data_list)/months)):  # int(lines/months) rounds down to nearest divisible number
        value1 = 0  # resets to 0 at the start of each new average
        value2 = 0
        for j in range(months):
            row = data_list[n].split(',')
            value1 = value1 + float(row[x_column-1])
            value2 = value2 + float(row[y_column-1])
            n = n + 1
        value1_2 = (f'{(value1/months):.2f}', f'{(value2/months):.2f}')
        points.append(value1_2)
    return points  # returns a list of 2-tuples


# Uses the lists made above to make plots with a coloured band of error

def plotWithError(name, uncertainty, points, points_upper, points_lower, colour_curve='blue', colour_band='aqua',
                  title_x='X', title_y='Y'):
    if len(points) == len(points_upper) == len(points_lower):
        points_x = []
        points_y = []
        points_upper_y = []
        points_lower_y = []
        for a, b in points:
            points_x.append(float(a))
            points_y.append(float(b))
        for c, d in points_upper:
            points_upper_y.append(float(d))  # Only interested in the y (error) component
        for e, f in points_lower:
            points_lower_y.append(float(f))
        plt.xlabel(title_x)
        plt.ylabel(title_y)
# This is the only order that returns a legend with the correct information
        plt.fill_between(points_x, points_lower_y, points_upper_y, color=colour_band, label=uncertainty)
        plt.legend()
        plt.plot(points_x, points_y, colour_curve, label=name)
    else:
        print('The length of each list is not equal')


# Part 3

# Used to correct land and sea data files
# Every other line is removed by creating a new list containing rows with even index values

def correctFile2(input_file,output_file):
    data = open(input_file, 'r')
    data_corrected = open(output_file, 'w')
    data_list = data.readlines()
    data_even = []
    n = 0
# Checks if the index is even appends the corresponding value to a new list and increases n by 1
# If odd, it just increases n by 1 because the data is not required
    for i in data_list:
        if n % 2 == 0:
            data_even.append(i)
        n = n + 1
    for j in data_even:
        entry_split = j.split()
        for k in entry_split:
            data_corrected.write(k + ',')  # Writes a new file with comma-separated data
        data_corrected.write('\n')



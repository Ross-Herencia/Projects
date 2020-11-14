from math import *
from matplotlib import pyplot as plt


def taucalc(input,output,plotname):
    f = open(input, 'r')
    f2 = open(output, 'w')
    time = []
    temp = []
    flines = f.readlines()
    for i in flines:
        fsplit = i.split()
        time.append(float(fsplit[0]))
        # 23.225 = 20.225 room temp + 3 systematic error
        temp.append(float(fsplit[1])-23.225)
    n = 1
    f2.write('Newton  Lorentz\n')
    resultsN = []
    resultsL = []
    number = []
    # time constant tau for newton's cooling law and lorentz's cooling law
    for j in range(39):
        tauN = (time[0] - time[n]) / (log((temp[n]/temp[0])))
        resultsN.append(float(f'{tauN/60:.2f}'))

        tauL = (time[0] - time[n]) / (4*(pow(temp[0], -0.25) - pow(temp[n], -0.25)))
        resultsL.append(float(f'{tauL/60:.2f}'))
        number.append(n)
        f2.write(f'{tauN/60:.2f}' + '   ' + f'{tauL/60:.2f}' + '\n')
        n = n + 1

    print('Newton:',resultsN)
    print('Lorentz:',resultsL)

    plt.plot(number,resultsN, 'b+', label='Newton')
    plt.plot(number, resultsL, 'ko', label='Lorentz')
    plt.title(plotname)
    plt.xlabel('Measurement number')
    plt.ylabel('Tau (min)')
    plt.legend()
    #plt.show()


taucalc('exp5bc.txt', 'exp5bctau.txt','Black Coffee')
plt.savefig('Black Coffee')
plt.show()
taucalc('exp5bw.txt', 'exp5bwtau.txt', 'Boiling Water')
plt.savefig('Boiling Water')
plt.show()
taucalc('exp5wc.txt', 'exp5wctau.txt', 'White Coffee')
plt.savefig('White Coffee')
plt.show()
taucalc('exp5bcw.txt', 'exp5bcwtau.txt', 'Black Coffee Water')
plt.savefig('Black Coffee with Water')
plt.show()
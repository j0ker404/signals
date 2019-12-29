import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from transfer_function import TF
"""
    Test transfer_function.py
"""
def bode_plot(num, den):
    # lets create the transfer function
    tf = signal.TransferFunction(num, den)
    w, mag, phase = tf.bode()
    # mag
    plt.figure()
    # plt.xlim(10^-2, 10^3)
    plt.semilogx(w, mag) 
    # phaseoften
    # plt.figure()
    # plt.xlim(10^-2, 10^4)
    # plt.semilogx(w, phase) 

    plt.show()


if __name__ == "__main__":
    # num  = []
    # den = []
    # print("Enter numerator coefficents in descending order: ")
    # print("Example input: 5 6 3 2.1")
    # data = ""
    # data = input()
    # while (data == ""):
    #     data = input()
    # val = data.split()
    # num = [float(x) for x in val]
    # # print([x for x in num])

    # print("Enter denomanator coefficents in descending order: ")
    # data  = ""
    # data = input()
    # while (data == ""):
    #     data = input()
    # val = data.split()
    # den = [float(x) for x in val]

    num = [100.0, 100.0]
    den = [1.0, 110.0, 1000.0]
    # print([x for x in den])
    tf = TF(num, den)
    # tf.set_num(num)
    # tf.set_den(den)

    # tf.plotMag()
    # tf.plotPhase()
    tf.plot_bode()
    # bode_plot(num, den)
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
import math


class TF:
    """
        Transfer Function
    """
    def __init__(self):
        """  
            Constructor 
            
        """
        super().__init__()
        self.__num = []
        self.__den = []
        self.__den.append(-1.0)

        self.__xmin = 10^-3
        self.__xmax = 10^4
        # self.__tf = signal.TransferFunction(self.__num, self.__den)
        self.__tf = None


    def __init__(self, num, den):
        """  
            Constructor for numerator and denominator
            
        """
        # self.__init__()
        self.__xmin = int(math.pow(10,-4))
        self.__xmax = int(math.pow(10,4))

        self.set_num(num)
        self.set_den(den)
        # self.__tf = signal.TransferFunction(self.__num, self.__den)
        self.__tf = None


    def __init__(self, zeros, poles, gain):
        """  
            Constructor for zeros, poles and gain

        """
        zpg = signal.ZerosPolesGain(zeros, poles, gain)
        tf = zpg.to_tf
        self.__num = tf.num
        self.__den = tf.den
        

    def __init__(self, num:list = [], den:list = [], zeros:list = [], poles:list = [], gain:float = 0):
        self.__xmin = int(math.pow(10,-4))
        self.__xmax = int(math.pow(10,5))
        if len(num) != 0 or len(den) != 0:
            self.set_num(num)
            self.set_den(den)
        elif len(zeros) != 0 or len(poles) != 0:
            zpg = signal.ZerosPolesGain(zeros, poles, gain)
            tf = zpg.to_tf()
            self.__num = tf.num
            self.__den = tf.den
        
    def get_xmax(self):
        """
            Get the max value for x-range
        """
        return self.__xmax
    

    def get_xmin(self):
        """
            Get the min value for x-range
        """
        return self.__xmin


    def set_xmax(self, max):
        """
            Set the max value for x-range
        """
        self.__xmax = max
    

    def set_xmin(self, min):
        """
            Set the min value for x-range
        """
        self.__xmin = min


    def set_num(self, num:list):
        """
            Set numerator for transfer function
        """
        self.__num = num.copy()

    def set_den(self, den:list):
        """
            Set denominator for transfer function
        """
        self.__den = den.copy()

    def get_num(self):
        """
            Get numerator for transfer function
        """
        return self.__num
        
    def get_den(self):
        """
            Get denominator for transfer function
        """
        return self.__den

    def get_values(self):
        """
            Returns frequencies, magnitudes and phase
            respectively
        """
        self.__tf = signal.TransferFunction(self.__num, self.__den)
        w=range(self.get_xmin(), self.get_xmax())
        return self.__tf.bode(w)

    def plotPhase(self):
        self.__tf = signal.TransferFunction(self.__num, self.__den)
        self.__w, self.__mag, self.__phase = self.get_values()
        plt.figure()
        plt.grid(True, which="both")
        plt.title("Phase")
        plt.xlabel("Frequency")
        plt.ylabel("Angle in degrees")
        plt.semilogx(self.__w, self.__mag)
        plt.show()

        

    def plotMag(self):
        self.__tf = signal.TransferFunction(self.__num, self.__den)
        self.__w, self.__mag, self.__phase = self.get_values()
        plt.figure()
        plt.grid(True, which="both")
        plt.title("Magnitute")
        plt.xlabel("Frequency")
        plt.ylabel("Amplitude")
        plt.semilogx(self.__w, self.__phase) 
        plt.show()

    

    
    def plot_bode(self):
        """
            Plot bode diagrams
        """
        self.__w, self.__mag, self.__phase = self.get_values()
        fig, (ax1, ax2) = plt.subplots(2, 1,constrained_layout=False)
        fig.suptitle('Bode plot', fontsize=16)
        ax1.grid(True, which="both")
        ax1.set_xlabel("Frequency")
        ax1.set_ylabel("Amplitude")
        ax1.semilogx(self.__w, self.__mag)
        
        ax2.grid(True, which="both")
        ax2.set_xlabel("Frequency")
        ax2.set_ylabel("Phase")
        ax2.semilogx(self.__w, self.__phase)

        plt.show()
        
        

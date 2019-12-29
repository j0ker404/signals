import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

class TF:
    """
        Transfer Function
    """
    def __init__(self):
        super().__init__()
        self.__num = []
        self.__den = []
        self.__nSet = False
        self.__dSet = False
        self.__den.append(-1.0)

        self.__w = 0.0
        self.__mag = 0.0
        self.__phase = 0.0
        self.__tf = signal.TransferFunction(self.__num, self.__den)

    def __init__(self, num, den):
        super().__init__()
        self.set_num(num)
        self.set_den(den)
        self.__tf = signal.TransferFunction(self.__num, self.__den)

    def set_num(self, num:list):
        """
            Set numerator for transfer function
        """
        self.__nSet = True
        self.__num = num.copy()

    def set_den(self, den:list):
        """
            Set denominator for transfer function
        """
        self.__dSet = True
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

    def plotPhase(self):
        self.__tf = signal.TransferFunction(self.__num, self.__den)
        self.__w, self.__mag, self.__phase = self.get_values()
        plt.figure()
        plt.title("Phase")
        plt.xlabel("Frequency")
        plt.ylabel("Angle in degrees")
        plt.semilogx(self.__w, self.__mag)
        plt.show()

        

    def plotMag(self):
        self.__tf = signal.TransferFunction(self.__num, self.__den)
        self.__w, self.__mag, self.__phase = self.get_values()
        plt.figure()
        plt.title("Magnitute")
        plt.xlabel("Frequency")
        plt.ylabel("Amplitude")
        plt.semilogx(self.__w, self.__phase) 
        plt.show()

    
    def get_values(self):
        """
            Returns frequencies, magnitudes and phase
            respectively
        """
        self.__tf = signal.TransferFunction(self.__num, self.__den)
        return self.__tf.bode()

    
    def plot_bode(self):
        """
            Plot bode diagrams
        """
        self.__w, self.__mag, self.__phase = self.get_values()
        fig, (ax1, ax2) = plt.subplots(2, 1,constrained_layout=True)
        fig.suptitle('Bode plot', fontsize=16)

        ax1.set_xlabel("Frequency")
        ax1.set_ylabel("Amplitude")
        ax1.semilogx(self.__w, self.__mag)
        
        ax2.set_xlabel("Frequency")
        ax2.set_ylabel("Phase")
        ax2.semilogx(self.__w, self.__phase)

        plt.show()
        
        

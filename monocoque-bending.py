
# coding: utf-8

# In[39]:

import numpy as np
import matplotlib.pyplot as plt


def semimonocoque():
        return 0


def monocoque():
        SFy = 1.25
        SFu = 1.5  # factor of safety, ultimate

        # material properties
        rho = 0.0975  # lb/in^3
        sigmay = 19000  # psi
        sigmau = 33000  # psi
    
        sigmastar = min(sigmay/SFy, sigmau/SFu)

        # airframe calculations
        length = 36  # length of monocoque section
        radius_mean = np.linspace(3,6)  # in
        thickness = np.linspace(0.125, .5, 4)

        for x in thickness:
            thick = x
            circumference = 2*np.pi*radius_mean
            mass = circumference * thick * length * rho  # mass of cylinder
            # moment of inertia of the cylinder
            inertia = mass * radius_mean**2
            y=length

            # calculating stresses
            #sigma = moment * y / I
            moment = sigmastar * inertia / y
            print(thick)
            plt.plot(radius_mean, moment)
            plt.show()
                
def main():
        print(monocoque())
        print(semimonocoque())


if __name__ == '__main__':
        main()


# In[ ]:




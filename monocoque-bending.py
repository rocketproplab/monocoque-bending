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
    radius_mean = 6  # in
    thickness = np.linspace(0.125, 0.5)  # in

    circumference = 2*np.pi*radius_mean
    mass = circumference * thickness * length * rho  # mass of cylinder
    # moment of inertia of the cylinder
    inertia = mass * radius_mean**2

    # calculating stresses
    sigma = moment * y / I
    moment = sigma * I / y
    sigma


def main():
    print(monocoque())
    print(semimonocoque())


if __name__ == '__main__':
    main()

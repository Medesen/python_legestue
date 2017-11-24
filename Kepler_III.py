#! /usr/bin/env python

# Calculates the period OR orbital separation of a binary obeying Kepler's 3rd law.
# Input: mass of orbital components (M1 & M2), AND orbital separation OR period of binary system.
# Output: period, given orbital separation OR orbital separation, given period.

# IMPORTS:
import numpy as np
import matplotlib.pyplot as plt
from optparse import OptionParser
import sys

# CONSTANTS:
G        = 6.6743e-8    # [cm^3/g/s^2]; gravitational constant.
#s_pr_yr  = 3.1558e7     # [s]; no. of seconds per year.
s_pr_day = 86400.       # [s]; no. of seconds per day.
cm_pr_AU = 1.49598e13   # [cm]; no. of cm per AU.
M_sun    = 1.99e33      # [g]; one solar mass.

# FUNCTIONS:
def Orbital_Separation(M, m, period):    # masses in [g] ; period in [s].
    orb_sep = ( period**2. * G * (M + m) / (4 * np.pi**2.) )**(1./3.)  # [cm]
    return orb_sep

def Period(M, m, orb_sep):
    Period = ( 4 * np.pi**2. * orb_sep**3. / (G * (M + m)) )**(1./2.)
    return Period

# MAIN PROGRAM:
parser = OptionParser()
parser.add_option("-P", "--binary_orbital_period", dest = "Period", help = "orbital period of binary system [days]", type = "float", default = 0.)
parser.add_option("-a", "--binary_separation", dest = "binary_separation", help = "binary separation [AU]", type = "float", default = 0.)
parser.add_option("-M", "--Mass_component_1", dest = "Mass_1", help = "mass [M_sun] of first binary component", type = "float", default = 0.)
parser.add_option("-m", "--Mass_component_2", dest = "Mass_2", help = "mass [M_sun] of second binary component", type = "float", default = 0.)
(options, args) = parser.parse_args()

M1 = options.Mass_1             # [M_sun]; mass of binary component no. 1.
M2 = options.Mass_2             # [M_sun]; mass of binary component no. 2.
P  = options.Period             # [yr]; orbital period of binary system.
a  = options.binary_separation  # [AU]; binary separation.

print ""
print "-----------------------------------------"

if (M1 == 0.):
    M1 = float(raw_input("Enter inital mass [M_sun] of first binary component (i.e. M_1,0): "))    
if (M2 == 0.):
    M2 = float(raw_input("Enter inital mass [M_sun] of second binary component (i.e. M_2,0): "))
print "M_1,0 =", M1, "M_sun = ", M1 * M_sun, "g."
print "M_2,0 =", M2, "M_sun = ", M2 * M_sun, "g."

if (a == 0. and P != 0.):
    a = Orbital_Separation(M1 * M_sun, M2 * M_sun, P * s_pr_day)     # input to funct: [M_sun] -> [g] & [days] -> [s]
    print "For P =", P, "yr the orbital separation is", a, "cm =", a / cm_pr_AU, "AU."
elif (P == 0. and a != 0.):
    P = Period(M1 * M_sun, M2 * M_sun, a * cm_pr_AU)
    print "For a =", a, "AU the binary period is", P, "s =", P / s_pr_day, "days"
else:
    print "ERROR: no input provided. Please enter either period (flag '-P' followed by period in [yr]) or orbital separation (flag '-a' followed by separation in [AU]"

print "-----------------------------------------"
print ""

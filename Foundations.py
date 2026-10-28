import aerosandbox as asb
import matplotlib.pyplot as plt
import numpy as np

#collect inputs from user

air_density = float(input('What is the air density?  '))
velocity = float(input("What is the Aircraft's velocity?"))
wing_area = float(input("WHat is the wing area? "))

#define airfoil

airfoil = asb.Airfoil("naca0015")

#Set angle of attack range

angleOfAttack = np.linspace(-5, 20, 51)
reynolds_num = 1000000
mach = 0

#Get lift and drag coefficients

aero_coefficients = airfoil.get_aero_from_neuralfoil(
    alpha = angleOfAttack,
    Re = reynolds_num,
    mach = mach
)

airfoil_cl = aero_coefficients["CL"]
airfoil_cd = aero_coefficients["CD"]

#Calculate lift and drag
airfoil_lift = airfoil_cl * (air_density * velocity * wing_area) / 2
airfoil_drag = airfoil_cd * (air_density * velocity * wing_area) / 2

#plot lift curve
plt.figure(1)
plt.plot(angleOfAttack,airfoil_cl)
plt.xlabel("Angle of attack [deg]")
plt.ylabel("Lift Coefficient, $C_L$")
plt.title("Lift coefficeient v. Angle of attack for NACA 0015")
plt.grid(True)


#plot drag curve
plt.figure(2)
plt.plot(angleOfAttack, airfoil_cd)
plt.xlabel("Angle of Attack [deg]")
plt.ylabel("Drag Coefficient, $C_D$" )
plt.title("Drag Coefficient v. Angle of Attack for NACA 0015")
plt.grid(True)


#plot cl/cd v AoA curve

cl_cd_ratio = airfoil_cl / airfoil_cd

plt.figure(3)
plt.plot(angleOfAttack, cl_cd_ratio)
plt.xlabel("Angle of Attack [deg]")
plt.ylabel("Cl to Cd ratio")
plt.title("Cl/Cd ratio v. Angle of Attack for NACA 0015")
plt.grid(True)

#plot lift and drag v angle of attack curve

plt.plot(angleOfAttack, cl_cd_ratio)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.set_title('Lift/Drag v AoA')

ax1.set_xlabel("Angle of Attack [deg]")
ax1.plot(angleOfAttack, airfoil_lift, color='red')
ax2.plot(angleOfAttack, airfoil_drag, color='blue')

ax1.set_ylabel('Lift', color='red')
ax2.set_ylabel('Drag', color='blue')

ax1.grid(True)
plt.show()


print(f'Lift (L): {airfoil_lift}')
print(f'Drag (D): {airfoil_drag}')



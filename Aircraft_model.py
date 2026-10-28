import aerosandbox as asb
import aerosandbox.aerodynamics.aero_3D as aero3d
import matplotlib.pyplot as plt
import aerosandbox.numpy as np
import copy

import functions as fn

airplane = asb.Airplane(
        name = 'Cessna172',
        xyz_ref = [0.81,0,0],
        wings = [
            asb.Wing(
                name = 'main wing',
                xyz_le = [0, 0, 0],
                symmetric = True,
                xsecs = [
                    asb.WingXSec(
                        xyz_le = [0, 0, 0],
                        chord = 1.0,
                        airfoil = asb.Airfoil('naca0015'),
                     
                    ),
                    asb.WingXSec(
                        xyz_le = [1.5, 5, 0],
                        chord = 0.75,
                        airfoil = asb.Airfoil('naca0015'),
                        
                    )
                ]
            ),
            asb.Wing(
                name = 'horizontal tail',
                xyz_le = [4, 0, 0],
                symmetric = True,
                xsecs = [
                    asb.WingXSec(
                        xyz_le = [0, 0, 0],
                        chord = 0.6,
                        airfoil = asb.Airfoil('naca0015'),
                        control_surfaces = [
                            asb.ControlSurface(
                                name = 'elevator',
                                deflection = 0,
                                hinge_point = 0.75,
                                trailing_edge = True,
                                symmetric = True
                            )

                        ]
                         
                    ),
                    asb.WingXSec(
                        xyz_le = [0.5, 1.2, 0],
                        chord = 0.6,
                        airfoil = asb.Airfoil('naca0015'),
                        control_surface = [
                            asb.ControlSurface(
                                name = 'elevator',
                                deflection = 0,
                                hinge_point = 0.75,
                                trailing_edge = True,
                                symmetric = True
                            )
                        ]# degrees where negative is downward motion
                         
                    )
                ]
            )
        ]
    )



if __name__ == "__main__":
    rho = float(input('What is the air density?  '))
    velocity = float(input("What is the Aircraft's velocity?"))
    wing_area = float(input("WHat is the wing area? "))
    mean_chord = float(input('What is the mean aerodynamic chord? '))
    wing_span = float(input('WHat is the wing span? '))
    #alpha = float(input('What is the angle of attack? '))
    mass = float(input('What is its mass? ')) 

    aero_center = mean_chord / 4
    dynamic_pressure = 0.5 * rho * velocity**2
    alpha = 1.32 #angle of attack for force trim @ 50 m/s
    dalpha = 0.5  
    deflection_delta = 1
    delta_pitchrate = 0.5

    alpha_list = np.linspace(0, 20, 25)

    #function used top set elevator deflection on airplane
    def set_elevator_deflection(airplane, ddeflection):
        for wing in airplane.wings:
            if wing.name == "horizontal tail":
                wing.set_control_surface_deflections({
                    "elevator": ddeflection
                })

    # for loop used to check if elevator is acutally being set
    for wing in airplane.wings:
        if wing.name == "horizontal tail":
            print("Tail control surfaces:", wing.get_control_surface_names())
            print("Elevator area (planform):", wing.control_surface_area(by_name="elevator"))
                 # degrees
       
    set_elevator_deflection(airplane, 100)

    results_posten = asb.AeroBuildup(
        airplane=airplane,
        op_point=asb.OperatingPoint(
            velocity=velocity,
            alpha=alpha,  # or a single alpha value
            beta=0,
            p=0,
            q=0,
            r=0,
        ),
    ).run()

    Cm_pos_list = []
    Cm_min_list = []
    

    # for alpha in alpha_list:
    #     results = fn.get_alpha_delta(airplane, alpha, dalpha, velocity)

    # Cm_pos_list.append(results['pos_delta'])
    # Cm_min_list.append(results['min_delta'])



    print ("Results:", results_posten['Cm'])
    print("Lift Coefficient:", results_posten['CL'])
    # print("Angle:", alpha_list)
    # print("Positive Cm:", Cm_pos_list)
    # print("Negative Cm:", Cm_min_list)
    

    #print("Angle:", alpha_list, "Positive:", Cm_pos, "Negative:", Cm_min)


    # ab = asb.AeroBuildup(
    #     airplane=airplane,
    #     op_point=asb.OperatingPoint(
    #         velocity=velocity,
    #         alpha=alpha_list,  # or a single alpha value
    #         beta=0,
    #         p=0,
    #         q=0,
    #         r=0,
    #     ),
    #     xyz_ref=[0,0,0],
    # )

    # aero = ab.run()

    
    


    # pitch_angle = 9

    #total moment given by the total aerodynamic pitching moment about the reference point of the aircraft plus the moment due to the lift force acting at the aerodynamic center of the wing

    # Cm_total = pitching_coefficient + Cm_alpha * dalpha + Cm_q * delta_pitchrate + Cm_delta_e * deflection_delta

    # total_moment = Cm_total * dynamic_pressure * mean_chord +  dynamic_pressure * aero_center * np.cos(np.radians(alpha_list))

    # idx_trim = np.argmin(np.abs(total_moment))
    # trim_alpha = alpha_list[idx_trim]

    #print("Trim angle of attack:", trim_alpha)
    #print(alpha_list)
    #print(total_moment)
        
    # print(dalpha_results)

    #print ("Total pitching moment:", total_moment)
    #airplane.draw_three_view()


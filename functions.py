## function for the positve delta in given variables
import aerosandbox as asb
import numpy as np
import Aircraft_model as am

def get_alpha_delta(airplane, alpha, delta, velo):
        alpha_posdelta = alpha + delta
        alpha_mindelta = alpha - delta

        
        airp_pos_output = asb.AeroBuildup(
                        airplane=airplane,
                        op_point=asb.OperatingPoint(
                               velocity = velo,
                               alpha = alpha_posdelta,
                               beta = 0,
                               p = 0,
                               q = 0,
                               r = 0,
                        )
                    ).run()
               
        airp_min_output = asb.AeroBuildup(
                        airplane=airplane,
                        op_point=asb.OperatingPoint(
                               velocity = velo,
                               alpha = alpha_mindelta,
                               beta = 0,
                               p = 0,
                               q = 0,
                               r = 0,
                        )
                    ).run()
        return { 
                "pos_delta": {
                        "Cm": airp_pos_output["Cm"],
                        'CL': airp_pos_output["CL"],

                }, 
                
                "min_delta": {
                        "Cm": airp_min_output["Cm"],
                        'CL': airp_min_output["CL"],

                }

              }


# results = get_alpha_delta(am.airplane, 5, 1, 50)
# print(results)

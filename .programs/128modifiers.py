

def generate_modifier(name, pairs):
    for i in range(1, 129):
        str = ""
        str += f"{name}_{i} = {{\n"
        for lhs,rhs in pairs:
            str += f"\t{lhs} = {round(i * rhs,3)}\n"
        str += f"}}\n\n"
        print(str)


generate_modifier("siege", [["siege_ability", 0.02 ]] )

generate_modifier("expansion", [ ["administrative_efficiency", 0.005 ], ["ae_impact", 0.005 ], ["core_creation", 0.005 ] ] )

generate_modifier("morale", [ ["land_morale", 0.01 ] ] )

generate_modifier("income", [ ["global_tax_income", 1 ] ] )

generate_modifier("army_size", [ ["land_forcelimit", 2 ], ["global_manpower", 1 ] ] )

generate_modifier("speed", [ ["movement_speed", 0.01 ] ] )

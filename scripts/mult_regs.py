# initialize carry and output
o = "\tset_variable = { which = carry value = 0 }\n"
for i in range(45):
    o = f"\tset_variable = {{ which = mor_{i} value = 0 }}\n"


# number of 0s at the end
for j in range(45)[::-1]:
    # only proceed if dr1_{j} is nonzero
    o += f"\tif = {{ limit = {{ check_variable = {{ which = dr1_{j} value = 1 }} }}\n"
    # Copy the registers dr0 series back into the temporary working area
    for i in range(45):
        o += f"\t\tset_variable = {{ which = twa_{i} which = dr0_{i} }}\n"

    # multipy temporary working area by dr1_{j}
    for i in range(45)[::-1]:
        
        o += f"""\t\tmultiply_variable = {{ which = twa_{i} which = dr1_{j} }}
\t\tchange_variable = {{ which = twa_{i} which = carry }}
\t\tif = {{
\t\t\tlimit = {{
\t\t\t\tcheck_variable = {{ which = twa_{i} value = 50 }}
\t\t\t}}
\t\t\tif = {{
\t\t\t\tlimit = {{
\t\t\t\t\tcheck_variable = {{ which = twa_{i} value = 70 }}
\t\t\t\t}}
\t\t\t\tif = {{
\t\t\t\t\tlimit = {{
\t\t\t\t\t\tcheck_variable = {{ which = twa_{i} value = 80 }}
\t\t\t\t\t}}
\t\t\t\t\tif = {{
\t\t\t\t\t\tlimit = {{
\t\t\t\t\t\t\tcheck_variable = {{ which = twa_{i} value = 90 }}
\t\t\t\t\t\t}}
\t\t\t\t\t\tset_variable = {{ which = carry value = 9 }}
\t\t\t\t\t\tsubtract_variable = {{ which = twa_{i} value = 90 }}
\t\t\t\t\t}}
\t\t\t\t\telse = {{
\t\t\t\t\t\tset_variable = {{ which = carry value = 8 }}
\t\t\t\t\t\tsubtract_variable = {{ which = twa_{i} value = 80 }}
\t\t\t\t\t}}
\t\t\t\t}}
\t\t\t\telse = {{
\t\t\t\t\tset_variable = {{ which = carry value = 7 }}
\t\t\t\t\tsubtract_variable = {{ which = twa_{i} value = 70 }}
\t\t\t\t}}
\t\t\t}}
\t\t\telse = {{
\t\t\t\tif = {{
\t\t\t\t\tlimit = {{
\t\t\t\t\t\tcheck_variable = {{ which = twa_{i} value = 60 }}
\t\t\t\t\t}}
\t\t\t\t\tset_variable = {{ which = carry value = 6 }}
\t\t\t\t\tsubtract_variable = {{ which = twa_{i} value = 60 }}
\t\t\t\t}}
\t\t\t\telse = {{
\t\t\t\t\tset_variable = {{ which = carry value = 5 }}
\t\t\t\t\tsubtract_variable = {{ which = twa_{i} value = 50 }}
\t\t\t\t}}
\t\t\t}}
\t\t}}
\t\telse = {{
\t\t\tif = {{
\t\t\t\tlimit = {{
\t\t\t\t\tcheck_variable = {{ which = twa_{i} value = 20 }}
\t\t\t\t}}
\t\t\t\tif = {{
\t\t\t\t\tlimit = {{
\t\t\t\t\t\tcheck_variable = {{ which = twa_{i} value = 30 }}
\t\t\t\t\t}}
\t\t\t\t\tif = {{
\t\t\t\t\t\tlimit = {{
\t\t\t\t\t\t\tcheck_variable = {{ which = twa_{i} value = 40 }}
\t\t\t\t\t\t}}
\t\t\t\t\t\tset_variable = {{ which = carry value = 4 }}
\t\t\t\t\tsubtract_variable = {{ which = twa_{i} value = 40 }}
\t\t\t\t\t}}
\t\t\t\t\telse = {{
\t\t\t\t\t\tset_variable = {{ which = carry value = 3 }}
\t\t\t\t\tsubtract_variable = {{ which = twa_{i} value = 30 }}
\t\t\t\t\t}}
\t\t\t\t}}
\t\t\t\telse = {{
\t\t\t\t\tset_variable = {{ which = carry value = 2 }}
\t\t\t\t\tsubtract_variable = {{ which = twa_{i} value = 20 }}
\t\t\t\t}}
\t\t\t}}
\t\t\telse = {{
\t\t\t\tif = {{
\t\t\t\t\tlimit = {{
\t\t\t\t\t\tcheck_variable = {{ which = twa_{i} value = 10 }}
\t\t\t\t\t}}
\t\t\t\t\tset_variable = {{ which = carry value = 1 }}
\t\t\t\t\tsubtract_variable = {{ which = twa_{i} value = 10 }}
\t\t\t\t}}
\t\t\t\telse = {{
\t\t\t\t\tset_variable = {{ which = carry value = 0 }}
\t\t\t\t}}
\t\t\t}}
\t\t}}\n"""
        # End inner for loop
    # Bitshift the value in TWA left the number of registers equal to j
    # Bitshift left to right
    a_j = 44 - j # antipode of j
    for k in range(45):
        if a_j == 0:
            break
        outpos = k - a_j
        # Just skip bitshifting if its negative
        if outpos < 0:
            continue
        o += f"\t\tset_variable = {{ which = twa_{outpos} which = twa_{k} }}\n"
    
    # Then fill in the last [44 - j] values with 0
    for k in range(a_j):
        o += f"\t\tset_variable = {{ which = twa_{44-k} value = 0 }}\n"
    
    # Add twa to mor
    o += "\t\tset_variable = { which = add_carry value = 0 }\n"
    for i in range(45)[::-1]:
        o += f"\t\tchange_variable = {{ which = mor_{i} which = twa_{i} }}\n"
        o += f"\t\tchange_variable = {{ which = mor_{i} which = add_carry }}\n"
        o += f"""\t\tif = {{
\t\t\tlimit = {{ check_variable = {{ which = mor_{i} value = 10 }} }}
\t\t\tsubtract_variable = {{ which = mor_{i} value = 10 }}
\t\t\tset_variable = {{ which = add_carry value = 1 }}
\t\t}} else = {{
\t\t\tset_variable = {{ which = add_carry value = 0 }}
\t\t}}\n"""
        
    # end the if that checks for 0
    o += f"\t}}\n\n"

# Bitshift mor series 3 to the right
for k in range(42)[::-1]:
    o += f"\tset_variable = {{ which = mor_{k + 3} which = mor_{k} }}\n"
o += f"\tset_variable = {{ which = mor_2 value = 0 }}\n"
o += f"\tset_variable = {{ which = mor_1 value = 0 }}\n"
o += f"\tset_variable = {{ which = mor_0 value = 0 }}\n"


# set dr0 series to mor
for i in range(45):
    o += f"\tset_variable = {{ which = dr0_{i} which = mor_{i} }}\n"

print(o)
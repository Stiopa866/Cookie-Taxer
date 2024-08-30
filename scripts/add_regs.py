o = "\tset_variable = { which = carry value = 0 }\n"

for i in range(45)[::-1]:
    o += f"\tchange_variable = {{ which = dr0_{i} which = dr1_{i} }}\n"
    o += f"\tchange_variable = {{ which = dr0_{i} which = carry }}\n"
    o += f"""\tif = {{
\t\tlimit = {{ check_variable = {{ which = dr0_{i} value = 10 }} }}
\t\tsubtract_variable = {{ which = dr0_{i} value = 10 }}
\t\tset_variable = {{ which = carry value = 1 }}
\t}} else = {{
\t\tset_variable = {{ which = carry value = 0 }}
\t}}\n\n"""

print(o)
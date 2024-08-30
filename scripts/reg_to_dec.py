r = 0
o = ""

for i in range(5):
    for j in range(9):
        # strip out last digit
        # assign to register
        # this goes in decreasing order
        st = f"""
    set_variable = {{ which = temp which = dr0_{r} }}
    multiply_variable = {{ which = temp value = {100000 / (10 ** j)} }}
    change_variable = {{ which = $ln$_{i} which = temp }}"""
        o += st
        r += 1

print(o)
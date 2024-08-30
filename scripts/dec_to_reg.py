r = 44
o = ""

for i in range(5)[::-1]:
    for j in range(9):
        # strip out last digit
        # assign to register
        # this goes in decreasing order
        st = f"""
    strip_last_digit_into_register = {{ var = fr{i} reg = dr0_{r} }}
    divide_variable = {{ which = fr{i} value = 10 }}"""
        o += st
        r -= 1

print(o)
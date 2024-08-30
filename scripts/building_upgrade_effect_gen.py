import codecs

# Globals
NAMESET = "cursor_cost"
BASE_COST = 15
FACTOR = 1.118
CHECK_VAR = "cursor_count"
MAX_BUILD_COUNT = 400

# Derived terms from globals
EXP_VAR = f"{NAMESET}_exp"
MTS_VAR = f"{NAMESET}_mantissa"
cloc_text_name = f"CLOC_{NAMESET.upper()}_EXP"

custom_loc = f"""defined_text = {{
    name = {cloc_text_name}
    random = no
    text = {{
        localisation_key = loc_duodecillion
        trigger = {{
            check_variable = {{ which = {EXP_VAR} value = 39 }}
        }}
    }}
    text = {{
        localisation_key = loc_undecillion
        trigger = {{
            check_variable = {{ which = {EXP_VAR} value = 36 }}
        }}
    }}
    text = {{
        localisation_key = loc_decillion
        trigger = {{
            check_variable = {{ which = {EXP_VAR} value = 33 }}
        }}
    }}
    text = {{
        localisation_key = loc_nonillion
        trigger = {{
            check_variable = {{ which = {EXP_VAR} value = 30 }}
        }}
    }}
    text = {{
        localisation_key = loc_octillion
        trigger = {{
            check_variable = {{ which = {EXP_VAR} value = 27 }}
        }}
    }}
    text = {{
        localisation_key = loc_septillion
        trigger = {{
            check_variable = {{ which = {EXP_VAR} value = 24 }}
        }}
    }}
    text = {{
        localisation_key = loc_sextillion
        trigger = {{
            check_variable = {{ which = {EXP_VAR} value = 21 }}
        }}
    }}
    text = {{
        localisation_key = loc_quintillion
        trigger = {{
            check_variable = {{ which = {EXP_VAR} value = 18 }}
        }}
    }}
    text = {{
        localisation_key = loc_quadrillion
        trigger = {{
            check_variable = {{ which = {EXP_VAR} value = 15 }}
        }}
    }}
    text = {{
        localisation_key = loc_trillion
        trigger = {{
            check_variable = {{ which = {EXP_VAR} value = 12 }}
        }}
    }}
    text = {{
        localisation_key = loc_billion
        trigger = {{
            check_variable = {{ which = {EXP_VAR} value = 9 }}
        }}
    }}
    text = {{
        localisation_key = loc_million
        trigger = {{
            check_variable = {{ which = {EXP_VAR} value = 6 }}
        }}
    }}
    text = {{
        localisation_key = loc_thousand
        trigger = {{
            check_variable = {{ which = {EXP_VAR} value = 3 }}
        }}
    }}
}}"""

def btree(lst, form):
	if not len(lst):
		return ''
	elif len(lst) == 1:
		return pyfl_to_vars((FACTOR ** lst[0]) * BASE_COST, NAMESET)
	else:
		return form % (lst[int(len(lst)/2)],
					   btree(lst[int(len(lst)/2):], form.replace('\n', '\n\t')),
					   btree(lst[:int(len(lst)/2)], form.replace('\n', '\n\t')))

def pyfl_to_vars(fl, nameset):
	vint = int(fl)
	fl4m = int(vint % 1000000)
	fl3d = int((vint / 1000000) % 1000)
	fl3m = int((vint / 1000000000) % 1000000)
	fl2d = int((vint / 1000000000000000) % 1000)
	fl2m = int((vint / 1000000000000000000) % 1000000)
	fl1d = int((vint / 1000000000000000000000000) % 1000)
	fl1m = int((vint / 1000000000000000000000000000) % 1000000)
	fl0d = int((vint / 1000000000000000000000000000000000) % 1000)
	fl0m = int((vint / 1000000000000000000000000000000000000) % 1000000)
	o = f"set_variable = {{ which = {nameset}_4 value = {fl4m}.000 }}    "
	o += f"set_variable = {{ which = {nameset}_3 value = {fl3m}.{fl3d} }}    "
	o += f"set_variable = {{ which = {nameset}_2 value = {fl2m}.{fl2d} }}    "
	o += f"set_variable = {{ which = {nameset}_1 value = {fl1m}.{fl1d} }}    "
	o += f"set_variable = {{ which = {nameset}_0 value = {fl0m}.{fl0d} }}    "
	return o
		
if __name__ == "__main__":

	cond = f'check_variable = {{ which = {CHECK_VAR} value = %s }}'
	form = 'if = {\n\t\tlimit = { %s }\n\t\t%s\n\t}\n\telse = {\n\t\t%s\n\t}' % (cond, '%s', '%s')

	with open(f'{NAMESET}_effects.txt', 'w') as f:
		outstr = f"get_{NAMESET} = {{\n\t" + btree([i for i in range(0, MAX_BUILD_COUNT + 1)], form)
		outstr += f"get_msd = {{ ln = {NAMESET} mantissa = {MTS_VAR} exponent = {EXP_VAR}}}"
		outstr += "\n}"
		f.write(outstr)
	
	with open(f'{NAMESET}_custom_loc.txt', 'w') as f:
		f.write(custom_loc)

	with codecs.open(f'{NAMESET}_l_english.yml', 'w', 'utf-8-sig') as f:
		f.write(f"l_english:\n {NAMESET}_tt: \"[{MTS_VAR}.GetValue] [Root.{cloc_text_name}]\"")
	


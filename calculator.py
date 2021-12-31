import os
import vecthree as v3


menu_options = [
"1. Add",
"2. Subtract",
"3. Scale",
"4. Get Magnitude",
"5. Normalize",
"6. Dot Product",
"7. Cross Product",
"8. Get Angle",
"9. Copy last result to clipboard",
"10. Quit"
]


functions = [v3.add,
v3.sub,
v3.scale,
v3.magnitude,
v3.normalize,
v3.dot,
v3.cross,
v3.get_angle
]


delim = ","


def print_options(n):
	global menu_options
	print("="*n)
	for m in menu_options:
		print(m)
	print("="*n)


def get_vector_input(n):
	nmap = {1:"First", 2:"Second"}
	if n == 0:
		return [input("Enter the vector\n")]
	return [input(f"Enter the {nmap[i]} vector\n") for i in range(1, n+1)]


def process_vector_as_string(x_str):
	global delim
	x_list = []
	for x in x_str.split(delim):
		x_list.append(float(x))
	return x_list


def process(n,m):
	global functions
	r = get_vector_input(m)
	xl = []
	for rr in r:
		xl_item = process_vector_as_string(rr)
		xl.append(xl_item)
	fn = functions[n-1]

	res = None
	if n == 3: # parameter for scale
		s_val = float(input("Enter amount to scale by:\n"))
		res = fn(*xl,s_val)
	else:
		res = fn(*xl)
	return res


def main():
	done = False
	result = None
	banner_size = 35
	while not done:
		print_options(banner_size)
		c = input("Select an option:\n")
		c_int = int(c)
		if c_int == 1: # add
			x = str(process(1,2))
			result = ",".join("".join(str(x)[1:-1]).split(", "))
			print("")
			print(result)
			print("")
		elif c_int == 2: # sub
			x = str(process(2,2))
			result = ",".join("".join(str(x)[1:-1]).split(", "))
			print("")
			print(result)
			print("")
		elif c_int == 3: # scale
			x = str(process(3,1))
			result = ",".join("".join(str(x)[1:-1]).split(", "))
			print("")
			print(result)
			print("")
		elif c_int == 4: # get magnitude
			x = str(process(4,0))
			print("")
			print(x)
			print("")
		elif c_int == 5: # normalize
			x = str(process(5,0))
			result = ",".join("".join(str(x)[1:-1]).split(", "))
			print("")
			print(result)
			print("")
		elif c_int == 6: # dot product
			x = str(process(6,2))
			print("")
			print(x)
			print("")
		elif c_int == 7: # cross product
			x = str(process(7,2))
			result = ",".join("".join(str(x)[1:-1]).split(", "))
			print("")
			print(result)
			print("")
		elif c_int == 8: # get angle
			x = str(process(8,2))
			print("")
			print(x)
			print("")
		elif c_int == 9: # copy result
			if result == None:
				os.system('echo "" | clip')
			else:
				cmd = f"echo {result} | clip"
				os.system(cmd)
		elif c_int == 10: # stop
			done = True
		else:
			raise Exception(f"Cannot recognize command'{c}'")
	print("Goodbye.")

if __name__ == "__main__":
	main()

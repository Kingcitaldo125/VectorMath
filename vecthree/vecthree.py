import math

def add(vec3one, vec3two):
	'''Return the sum of vec3one and vec3two'''
	if len(vec3one) != len(vec3two):
		return -1
	a = vec3one
	b = vec3two

	return [round(a[i] + b[i],4) for i in range(len(a))]

def sub(vec3one, vec3two):
	'''Return the difference between vec3one and vec3two(vec3one - vec3two)'''
	if len(vec3one) != len(vec3two):
		return -1
	a = vec3one
	b = vec3two

	return [round(a[i] - b[i],4) for i in range(len(a))]

def scale(vec3, val):
	'''Scale the vector, vec3, by the value val'''
	return [i*val for i in vec3]

def magnitude(vec3):
	'''Return the magnitude of a vector'''
	tot = 0
	for v in vec3:
		tot += v**2
	
	return round(math.sqrt(tot),4)

def normalize(vec3):
	'''Normalize, and return, a vector'''
	return [round(i/magnitude(vec3),4) for i in vec3]

def dot(vec3one, vec3two):
	'''Return the dot product of two vectors'''
	if len(vec3one) != len(vec3two):
		return -1
	h = 0
	for v in range(len(vec3one)):
		prod = vec3one[v] * vec3two[v]
		h += prod

	return round(h,4)

def cross(vec3one, vec3two):
	'''Return the cross product of two vector 3s'''
	if len(vec3one) != len(vec3two) or len(vec3one) != 3:
		return -1
	a = vec3one
	b = vec3two
	
	ax = a[0]
	ay = a[1]
	az = a[2]

	bx = b[0]
	by = b[1]
	bz = b[2]

	return [round((ay*bz) - (az*by), 4), round((az*bx) - (ax*bz), 4), round((ax*by) - (ay*bx), 4)]

def get_angle(vec3one, vec3two):
	'''Return the angle(degrees) between two vectors'''
	dotV = dot(vec3one, vec3two)
	magone = magnitude(vec3one)
	magtwo = magnitude(vec3two)
	ang = dotV/(magone * magtwo)
	ang = round(ang, 4)
	theta = math.acos(ang)
	
	NDot = round(magone * magtwo * math.cos(theta))
	#print("NDot",NDot)
	#print("dotV",dotV)
	assert(round(NDot) == round(dotV))

	return round(math.degrees(theta), 4)

if __name__ == "__main__":
	'''Entrypoint'''
	vec3one = [4.5774, 7.5774, 2.5774]
	vec3two = [1.12321, 3.12184, 8.49534]

	print(f"{vec3one} magnitude =", magnitude(vec3one))
	print(f"{vec3two} magnitude =", magnitude(vec3two))
	print(f"'{vec3one}' + '{vec3two}' =", add(vec3one, vec3two))
	print(f"'{vec3one}' - '{vec3two}' =", sub(vec3one, vec3two))
	print(f"{vec3one} normalized =", normalize(vec3one))
	print(f"{vec3two} normalized =", normalize(vec3two))
	print(f"'{vec3one}' dot '{vec3two}' =", dot(vec3one, vec3two))
	print(f"'{vec3one}' X '{vec3two}' =", cross(vec3one, vec3two))
	print(f"Angle between '{vec3one}' and '{vec3two}' (degrees)=", get_angle(vec3one, vec3two))

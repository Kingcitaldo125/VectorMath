import math

def add(vec3one, vec3two):
	if len(vec3one) != len(vec3two):
		return -1
	a = vec3one
	b = vec3two

	return [(a[i] + b[i]) for i in range(len(a))]

def sub(vec3one, vec3two):
	if len(vec3one) != len(vec3two):
		return -1
	a = vec3one
	b = vec3two

	return [(a[i] - b[i]) for i in range(len(a))]

def scale(vec3, val):
	return [i*val for i in vec3]

def magnitude(vec3):
	tot = 0
	for v in vec3:
		tot += v**2
	
	return round(math.sqrt(tot),4)

def normalize(vec3):
	return [round(i/magnitude(vec3),4) for i in vec3]

def dot(vec3one, vec3two):
	if len(vec3one) != len(vec3two):
		return -1
	h = 0
	for v in range(len(vec3one)):
		prod = vec3one[v] * vec3two[v]
		h += prod

	return round(h,4)

def cross(vec3one, vec3two):
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

	holdr = [round((ay*bz) - (az*by), 4), round((az*bx) - (ax*bz),4), round((ax*by) - (ay*bx),4)]
	
	return holdr

def get_angle(vec3one, vec3two):
	dotV = dot(vec3one, vec3two)
	magone = magnitude(vec3one)
	magtwo = magnitude(vec3two)
	theta = math.acos(dotV/(magone * magtwo))
	
	NDot = round(magone * magtwo * math.cos(theta))
	assert(NDot == dotV)

	return round(math.degrees(theta),4)

vec3one = [5, 4, 3]
vec3two = [3, -2, 7]
vec3three = [8, 4, 9]

#vec3one = [1,0,0]
#vec3two = [0,1,0]
#vec3three = [0,0,1]

print(f"{vec3one} magnitude =", magnitude(vec3one))
print(f"{vec3two} magnitude =", magnitude(vec3two))
print(f"'{vec3one}' + '{vec3two}' =", add(vec3one, vec3two))
print(f"'{vec3one}' - '{vec3two}' =", sub(vec3one, vec3two))
print(f"{vec3one} normalized =", normalize(vec3one))
print(f"{vec3one} normalized =", normalize(vec3two))
print(f"'{vec3one}' dot '{vec3two}' =", dot(vec3one, vec3two))
print(f"'{vec3one}' X '{vec3two}' =", cross(vec3one, vec3two))
print(f"Angle between '{vec3one}' and '{vec3two}' (degrees)=", get_angle(vec3one, vec3two))

#Upal Patel 
import re

def find_planet_names(content:str):
	pattern = re.compile("\"BodyName\":\"[-\w+\s\d+]+")
	planetResult = pattern.findall(content)
	if planetResult:
		for i in planetResult:
			if i[0] == i[-1]:
				i += 1
			print(i+'"')
	return len(planetResult)

import json
import sys

class Spell:
	def __init__(self, name, desc, page, range, components, ritual, duration, concentration, casting_time, level, school, character_class):
		self.name = name
		self.desc = desc
		self.page = page
		self.range = range
		self.components = componentes
		self.ritual = ritual
		self.duration = duration
		self.concentration = concentration
		self.casting_time = casting_time
		self.level = level
		self.school = school
		self.character_class = character_class

	def __init__(self, json):
		self.name = json['name']
		self.desc = json['desc']
		self.page = json['page']
		self.range = json['range']
		self.components = json['components']
		if json['ritual'] == 'yes': self.ritual = True
		else: self.ritual = False
		self.duration = json['duration']
		if json['concentration'] == 'yes': self.concentration = True
		else: self.concentration = False
		self.casting_time = json['casting_time']
		self.level = json['level']
		self.school = json['school']
		self.character_class = json['class']

	def __str__(self):
		return "Name:\t"+self.name+"\nDescription:\t"+self.desc+"\nPage:\t"+self.page+"\n\nRange:\t"+self.range+"\nComponents:\t"+self.components+"\nRitual:\t"+str(self.ritual)+"\nDuration:\t"+self.duration+"\nConcentration:\t"+str(self.concentration)+"\nCasting time:\t"+self.casting_time+"\nLevel:\t"+self.level+"\nSchool:\t"+self.school+"\nCharacter class:\t"+self.character_class

'''
	Converts file string into JSON.
	Throws exception if file contents
	aren't in JSON format.
'''
def loadJSON(filename):
	file = open(filename, "r")
	content = file.read()
	file.close()
	return json.loads(content)

'''
	Converts JSON array into spell array.
'''
def JSON2SpellArray(json):
	result = []
	# convert JSON spells to Spell class
	for row in json['spells']:
		result.append(Spell(row))
	return result

def print_spell(spell):
	print("Name:\t"+spell.name)
        print("Description:\t"+spell.desc)
        print("Page:\t"+spell.page)
        print("\nRange:\t\t"+spell.range)
        print("Components:\t"+spell.components)
        print("Ritual:\t\t"+str(spell.ritual))
        print("Duration:\t"+spell.duration)
        print("Concentration\t"+str(spell.concentration))
        print("Casting time:\t"+spell.casting_time)
        print("Level:\t\t"+spell.level)
        print("School:\t\t"+spell.school)
        print("Class:\t\t"+spell.character_class)


if __name__=='__main__':
	json = loadJSON('spells.json')
	spells = JSON2SpellArray(json)
	# interpret command
	if len(sys.argv) > 1:
		cmd = sys.argv[1]
		if cmd == 'see_all' or cmd == 'show_all':
			for spell in spells:
				print_spell(spell)
				print("\n__________________________________")
		elif cmd == "search_name" and sys.argv > 2:
			print("Searching for spell with name "+sys.argv[2])
			for spell in spells:
				if spell.name.lower().startswith(sys.argv[2].lower()):
					print_spell(spell)
	                                print("\n__________________________________")
			print("Finished searching!")
		elif cmd == "search_school" and sys.argv > 2:
			print("Searching for spell that belongs to school "+sys.argv[2])
                        for spell in spells:
                                if spell.school.lower().startswith(sys.argv[2].lower()):
                                        print_spell(spell)
                                	print("\n__________________________________")
                        print("Finished searching!")

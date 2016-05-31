import sys
import math
import time
import random

turn = 1

class Army:

	def __init__(self, name):
		self.name = name
		self.troop = 1
		self.morale = 100
		self.disc = 0
		self.location = ['none', 'none', 'none']
		self.weapons = 0
		self.food = 0
		
	def upkeep(self):
		if player.gold < self.troop:
			print("Your men are angry they haven't been paid in full")
			self.morale -= math.ceil(10*(player.gold / self.troop))
		elif player.gold >= self.troop:
			self.morale += 10
			if self.morale > 100:
				self.morale -= self.morale % 100
			player.gold -= self.troop
	
	def no_units(self):
		if self.troop == 0:
			print(self.name,  "has been killed to the last man")
			del self
			
	def see_army(self):
		print ("Morale = ", self.morale)
		print ("Soldiers = ", self.troop)
		print ("Discipline = ", self.disc)
		print ("Weapons = ", self.weapons)
		print ("Food = ", self.food)
		print("Location = ", self.location)
		input(';')
	
	def cons_food(self):
		for i in player.cities:
			if self.location[0] == i.name:
				if i.food * 10 >= self.troop:
					i.food -= math.ceil(self.troop * .10)
				elif i.food * 10 < self.troop:
					consumed = i.food + self.food
					i.food -= i.food
					if self.troop <= 10 * consumed:
						self.food -= math.ceil(self.troop * .10)
					elif self.troop > 10 * consumed:
						print("your soldiers of ", self.name, " are starving")
						self.morale -= math.floor(consumed*10/self.troop)
						self.food -= self.food
						self.troop -= math.ceil(self.troop * random.uniform(.1, .3))
			else:
				if self.troop <= 10 * self.food:
					self.food -= math.ceil(self.troop * .10)
				elif self.troop > 10 * self.food:
					print("Your soldiers of ", self.name, " are starving")
					self.morale -= math.floor(self.food*10/self.troop)
					self.food -= self.food
					self.troop -= math.ceil(self.troop * random.uniform(.1, .3))
					

	def move_army(self):
		while True:
			print("These are your cities: ")
			for c in player.cities:
				print(c.name)
			s = input("which city would you like to move to?: ")
			for i in player.cities:
				if i.name == s:
					if self.location[0] == i.name:
						print("Your army is already there!")
						input(':')
						break
					else:
						self.location[1] = i.name
						self.location[0] = 'enroute'
						print("Your army is enroute to", i.name)
						input(':')
			if s in ('n', 'no', 'N', 'NO'):
				break
	def army_travel(self):
		pass
	


class City:

	def __init__(self, name):
		self.name = name
		self.pop = 100
		self.food = 0
		self.weapons = 0
		self.happy = 100
		self.farms = 1
		self.wall = 0
		self.statue = 0
		self.smith = 0
		

	def employ_pop(self, const): # Improve the maths to be more fluid
		totalw = (self.farms * 70) + (self.statue * 10) + (self.smith * 30) + (self.wall * 5)
		needed_pop = totalw - self.pop
		pro_ef = self.pop/totalw
		
		if totalw < self.pop:
			print("There are ", (self.pop - totalw), " unemployed citizens in", self.name) # repeating same thing over and over, switch function to a different one
			input(':')
			return 1

		elif totalw == self.pop:
			return 1
			
		elif totalw > self.pop:
			print("There are not enough citizens in this city to handle all jobs")
			input(':')
			if const == self.farms:
				return pro_ef
			elif const == self.smith:
				return pro_ef
		
	def grow_pop(self):
		self.pop += math.ceil(self.pop * random.uniform(.1, .3))
	
	def prod_weapons(self):
		if self.smith == 0:
			return 0
		self.weapons += math.ceil(self.smith * 3 * self.employ_pop(self.smith))
		return self.weapons
	
	def prod_food(self):
		if self.farms == 0:
			return 0
		self.food += math.ceil(self.farms * 10 * self.employ_pop(self.farms))
		return self.food
	
	def riot_city(self, anger):
		totalb = (self.farms + self.statue + self.wall + self.smith)
		
		def max_destroy(percent):
			totald = percent * totalb
			return totald

		def numpercent(num): # Use this function for future buildings
			if num == 0:
				return 0
			else:
				return num / totalb
		
		def d_buildings(num, percent):
			destroyed_d = math.ceil(numpercent(num) * max_destroy(percent))
			return destroyed_d

		def fpercent():
			if self.farms == 0:
				return 0
			else:
				return self.farms / totalb
		def spercent():
			if self.statue == 0:
				return 0
			else:
				return self.statue / totalb
		def smithpercent():
			if self.statue == 0:
				return 0
			else:
				return self.smith / totalb
		
		d = anger + random.randint(1, 10)
		
		if d >= 10:	
			print("Rioters are out of control!!")
			input(":")
			print(math.ceil(fpercent() * max_destroy(.80)), "farms have been burned to the ground")
			self.farms -= math.ceil(fpercent() * max_destroy(.80))
			print(math.ceil(spercent() * max_destroy(.80)), "statues have been toppled by angry protesters")
			self.statue -= math.ceil(spercent() * max_destroy(.80))
			print(math.ceil(smithpercent() * max_destroy(.80)), "smitheries have been toppled by angry protesters")
			self.smith -= math.ceil(smithpercent() * max_destroy(.80))
			input(":")
			del d # possible bug, add 'del fpercent, spercent' if numbers messing up. Not sure if numbers get replaced in function... look into it.
			
		elif d in (9, 8, 7):
			print("Rioters are rampaging!")
			input(":")
			print(math.ceil(fpercent() * max_destroy(.50)), "farms have been burned")
			self.farms -= math.ceil(fpercent() * max_destroy(.50))
			print(math.ceil(spercent() * max_destroy(.50)), "statues of", player_name, "have been smashed to bits by angry peasants")
			self.statue -= math.ceil(spercent() * max_destroy(.50))
			print(math.ceil(smithpercent() * max_destroy(.5)), "smitheries have been annihilated by angry protesters")
			self.smith -= math.ceil(smithpercent() * max_destroy(.50))
			input(":")
			del d
			
		elif d in (6, 5, 4):
			print("Rioters are out and about but the guards have it under control!")
			input(":")
			print(math.ceil(fpercent() * max_destroy(.20)), "farms have been destroyed")
			self.farms -= math.ceil(fpercent() * max_destroy(.20))
			print(math.ceil(spercent() * max_destroy(.20)), "statues have been lost to fierce citizens")
			self.statue -= math.ceil(spercent() * max_destroy(.20))
			print(math.ceil(smithpercent() * max_destroy(.20)), "smitheries have been toppled by angry protesters")
			self.smith -= math.ceil(smithpercent() * max_destroy(.20))
			input(":")
			del d
			
		elif d in (3, 2, 1):
			print("Your royal guards have kept down the riots!")
			del d
	
	def check_morale(self):
		morale = self.happy
		if morale < 15:
			print("The workers of", self.name, "are disgusted with your rule! They are rampaging in the street!")
			self.riot_city(3)
		elif morale < 30:
			print("The workers of", self.name, "are angry with your rule! They are rioting!")
			self.riot_city(2)
		elif morale < 50:
			print("The plebiens of", self.name, "are discontent with your rule! They are protesting!")
			self.riot_city(1)
		elif morale < 90:
			print("The citizens of", self.name, "are content with your rule")
			input(":")
		elif morale >= 90:
			print("The citizens of", self.name, "love", player_name, "!")
			input(":")
			
	def cons_food(self):			#consume food
		if self.pop >= self.food * 10:
			print("Your people have starved. Your city of", self.name, "has lost", math.ceil(self.pop * .30), "people")
			input(':')
			self.pop -= math.ceil(self.pop * random.uniform(.10, .30))
			self.food -= self.food # removes all food
			self.happy -= math.ceil(self.happy * .40)
			if self.happy <= 25:
			 self.happy -= self.happy
			return self.pop, self.food
		elif self.pop <= self.food * 10:
			self.food -= math.ceil(self.pop * .10)
			self.happy += 10
			self.grow_pop()
			if self.happy > 100:
				self.happy -= self.happy % 100
			return self.food

	def inflation(self, cost):
		total = cost + self.pop * .02
		return math.ceil(total)


	def const_city(self):
		while True:
			print('\n' * 70)
			print("You have: ", player.gold, "gold")
			print("To build a wall type: wall\n\
			It will cost ", self.inflation(70), "to build a wall")
			print("To build a farm type: farm\n\
			It will cost ", self.inflation(50), "to build a farm." )
			print("To build a statue type: statue\n\
			It will cost ", self.inflation(200), "to build a statue")
			print("To build a smith type: smith\n\
			It will cost ", self.inflation(150), "to build a smith")
			b = input(':')
		
			if b in ("farm", "f"):
				if player.gold < self.inflation(50):
					print("You do not have enough gold")
					input(':')
				else:
					self.farms += 1
					player.gold -= self.inflation(50)
					print("You build another farm")
					input(':')
				
			elif b in ('wall', 'w'):
				if player.gold < self.inflation(70):
					print("You do not have enough gold")
					input(':')
				else:
					self.wall += 1
					player.gold -= self.inflation(70)
					print("You build another wall")
					input(':')
			elif b in ('statue', 's'):
				if player.gold < self.inflation(150):
					print("You do not have enough gold")
					input(':')
				else:
					self.statue += 1
					self.happy += 10
					player.gold -= self.inflation(200)
					print("You build another statue")
					input(':')
			elif b in ('smith', 'a', 'Smith'):
				if player.gold < self.inflation(200):
					print("You do not have enough gold")
					input(':')
				else:
					self.smith += 1
					player.gold -= self.inflation(150)
					print("You build another smithery")
					input(':')
			elif b in ('n', 'no', 'No'):
				break

	def see_city(self):
		print('\n' * 100)
		print('city name = ', self.name)
		print('population = ', self.pop)
		print('food = ', self.food)
		print('happiness = ', self.happy, '%')
		print('walls = ', self.wall)
		print('farms = ', self.farms)
		print('statues of', player_name, '=', self.statue)
		print('smiths = ', self.smith)
		print('weapons = ', self.weapons)
		input(':')

class Empire:

	def __init__(self, name):
		self.name = name
		self.cities = []
		self.gold = 2000
		self.army = []


	def first_city(self):
		while True:
			if len(self.cities) > 0:
				break

			elif len(self.cities) == 0:
				self.cities.append(City(input("Give your first city a name:")))
				for c in self.cities:
					print("You own", c.name)
			else:
				break
	def view_city(self):
		while True:
			if len(self.cities) == 0:
				print("you own no cities")
				break
			print('\n' * 50)
			print("These are your cities: ")
			for c in self.cities:
				print(c.name)
				
			s = input("which city would you like to view?: ")
			for i in self.cities:
				if i.name == s:
					i.see_city()
			if s in ('n', 'no', 'N', 'NO'):
				break
				
	def view_army(self):
		while True:
			if len(self.army) == 0:
				print("you own no armies")
				break
			print('\n' * 50)
			print("These are your armies: ")
			for c in self.army:
				print(c.name)
				
			s = input("which army would you like to view?: ")
			for i in self.army:
				if i.name == s:
					i.see_army()
			if s in ('n', 'no', 'N', 'NO'):
				break
	def move_army(self):
		while True:
			if len(self.army) == 0:
				print("you own no armies")
				break
			print('\n' * 50)
			print("These are your armies: ")
			for c in self.army:
				print(c.name)
				
			s = input("which army would you like to move?: ")
			for i in self.army:
				if i.name == s:
					i.move_army()
			if s in ('n', 'no', 'N', 'NO'):
				break
	def build_city(self):
		while True:
			if len(self.cities) == 0:
				print("you own no cities")
				break
			print('\n' * 50)
			print("These are your cities: ")
			for c in self.cities:
				print(c.name)
				
			s = input("which city would you like to build in?: ")
			print('To found a new city type: city')
			for i in self.cities:
				if i.name == s:
					i.const_city()
			if s in ('n', 'no', 'N', 'NO'):
				break
			elif s in ('city', 'c'):
				while True:
					self.cities.append(City(input("Give your city a name:")))
					for c in self.cities:
						print("You own", c.name)
					else:
						break
	def found_city(self):
		while True:
			print('\n' * 50)
			print("These are your cities: ")
			for c in self.cities:
				print(c.name)
			s = input("which city would you like to build from?: ")
			for i in self.cities:
				if i.name == s:
					if i.pop <= 100:
						print("This city does not have enough population")
						input(':')
					elif self.gold < 500:
						print("You don't have enough gold")
						input(':')
						break
					else:
						i.pop -= 100
						self.gold -= 500
						self.cities.append(City(input("Give your city a name:")))
						continue
			if s in ('n', 'no', 'N', 'NO'):
				break
		
		
	def col_tax(self):
		print("Collecting taxes...")
		#time.sleep(6)
		for i in self.cities:
			self.gold += math.ceil(i.pop * .3) # forgot the random, check this

	def view_empire(self): # func to view total gold, cities, food, and eventually armies
			print(self.name,"\n", "Your gold:\n", self.gold)
			print("\nCities: ")
			for c in self.cities:
				print(c.name)
			print("\nArmy: ")
			for a in self.army:
				print(a.name)
			input(':')

	def build_army(self):
		while True:
			print('\n' * 50)
			print("These are your cities: ")
			for c in self.cities:
				print(c.name)
			s = input("which city would you like to build an army from?: ")
			for i in self.cities:
				if i.name == s:
					if i.pop < 100:
						print("This city does not have enough population")
						input(':')
					elif self.gold < 200:
						print("You don't have enough gold")
						input(':')
						break
					else:
						i.pop -= 1
						self.gold -= 200
						self.army.append(Army(input("Give your army a name:")))
						for a in self.army:
							if a.location[0] == 'none':
								a.location[0] = i.name
						continue
			if s in ('n', 'no', 'N', 'NO'):
				break
	def transfer_res(self):
		while True:
			print('\n' * 100)
			print("These are your cities: ")
			for c in self.army:
				print(c.name)
			s = input("which army would you like to transfer resources to?: ")
			for i in self.army:
				if i.name == s:
					if i.pop < 100:
						print("This city does not have enough population")
						input(':')
					elif self.gold < 200:
						print("You don't have enough gold")
						input(':')
						break
					else:
						i.pop -= 1
						self.gold -= 200
						self.army.append(Army(input("Give your army a name:")))
						for a in self.army:
							if a.location[0] == 'none':
								a.location[0] = i.name
						continue
class enemy:
	pass

player_name = input("Enter your name!")
player = Empire(input("enter your kingdom name "))
player.first_city()


def end_turn():
	print('cities are growing...')
	#time.sleep(1)
	for i in player.army:
		i.cons_food()
	for i in player.cities:
		i.cons_food()
		i.prod_food()
		i.prod_weapons()
		i.check_morale()
		i.see_city()
		
	player.col_tax()
	global turn
	turn += 1
	print("It is now turn ", turn)

while True:
	print('\n' * 50)
	print("Menu")
	print("~" * 100)
	print("Options:\n\
	To view your cities type: view city\n\
	To view your Empire type: view empire\n\
	To build in a city type: build\n\
	To found a city type: city\n\
	To build an army type: army\n\
	To view an army type: view army\n\
	To move an army type: move\n\
	To transfer men and resources to an army type: transfer\n\
	To end your turn type: end\n\
	")
	i = input(':')
	if i in ('view city', 'View City', 'v' 'View city'):
		player.view_city()
	elif i in ('view empire', 'View Empire', 'View empire', 've'):
		player.view_empire()
	elif i in ('build', 'Build', 'b'):
		player.build_city()
	elif i in ('end', 'End', 'e'):
		end_turn()
	elif i in ('city', 'c', 'City'):
		player.found_city()
	elif i in ('army', 'a', 'Army'):
		player.build_army()
	elif i in ('va','view army', 'View Army', 'View army'):
		player.view_army()
	elif i in ('move', 'm', 'Move'):
		player.move_army()
	elif i in ('transfer', 't', 'Transfer'):
		player.transfer_res()
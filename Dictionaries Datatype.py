# 1. The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).

def email_list(domains):
	emails = []
	for domain, users in domains.items():
	  for user in users:
	    emails.append(user+'@'+domain)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

print(" ")

# 2. The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values.

def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group_names, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			if user in user_groups:
				user_groups[user].append(group_names)
			else:
				user_groups[user] = [group_names]
				
				
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

print(" ")

# 3. The add_prices function returns the total price of all of the groceries in the  dictionary. Fill in the blanks to complete this function

def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for item, price in basket.items():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += price
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44

print(" ")


# 4. Fill in the blanks to complete the “car_listing” function. This function accepts a “car_prices” dictionary. It should iterate through the keys (car models) and values (car prices) in that dictionary. For each item pair, the function should format a string so that a dictionary entry like ““Kia Soul“:19000” will print "A Kia Soul costs 19000 dollars". Each new string should appear on its own line.

def car_listing(car_prices):
  result = ""
  # Complete the for loop to iterate through the key and value items 
  # in the dictionary.
  for key, value in car_prices.items(): 
    result += "A {} costs {} dollars".format(key, value) + "\n"  # Use a string method to format the required string. 
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# Should print:
# A Kia Soul costs 19000 dollars
# A Lamborghini Diablo costs 55000 dollars
# A Ford Fiesta costs 13000 dollars
# A Toyota Prius costs 24000 dollars

print(" ")

# 5. Tessa and Rick are hosting a party. Both sent out invitations to their friends, and each one collected responses into dictionaries, with names of their friends and how many guests each friend was bringing. Each dictionary is a partial guest list, but Rick's guest list has more current information about the number of guests. 

# Complete the function to combine both dictionaries into one, with each friend listed only once, and the number of guests from Rick's dictionary taking precedence, if a name is included in both dictionaries. Then print the resulting dictionary.

def combine_guests(guests1, guests2):
  guests2.update (guests1) # Use a dictionary method to combine the dictionaries.
  return guests2

Ricks_guests = { "Adam":2, "Camila":3, "David":1, "Jamal":3, "Charley":2, "Titus":1, "Raj":4}
Tessas_guests = { "David":4, "Noemi":1, "Raj":2, "Adam":1, "Sakira":3, "Chidi":5}

print(combine_guests(Ricks_guests, Tessas_guests))
# Should print:
# {'David': 1, 'Noemi': 1, 'Raj': 4, 'Adam': 2, 'Sakira': 3, 'Chidi': 5, 'Camila': 3, 'Jamal': 3, 'Charley': 2, 'Titus': 1}

print(" ")

# 6. Use a dictionary to count the frequency of numbers in the given “text” string. Only numbers should be counted. Do not count blank spaces, letters, or punctuation. Complete the function so that input like "1001000111101" will return a dictionary that holds the count of each number that occurs in the string  {'1': 7, '0': 6}. 

def count_numbers(text):
  # Initialize a new dictionary.
  dictionary = {} 
  # Complete the for loop to iterate through each "text" character.
  for i in text:
    # Complete the if-statement using a string method to check if the
    # character is a number.
    if i.isnumeric():
      # Complete the if-statement using a logical operator to check if 
      # the number is not already in the dictionary.
      if i not in dictionary:
           # Use a dictionary operation to add the number as a key
           # and set the initial count value to zero.
           dictionary[i] = 1
      # Use a dictionary operation to increment the number count value 
      # for the existing key.
      else:
        dictionary[i] += 1
  return dictionary

print(count_numbers("1001000111101"))
# Should be {'1': 7, '0': 6}

print(count_numbers("Math is fun! 2+2=4"))
# Should be {'2': 2, '4': 1}

print(count_numbers("This is a sentence."))
# Should be {}

print(count_numbers("55 North Center Drive"))
# Should be {'5': 2}

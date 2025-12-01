
''' 
Dictionaries are a type of collection in Python
Lists have indexes and elements, and are usually called integer indexes
Dictionaries however have keys and values, similarly keys are like indexes however they dont have to be integers (can be characters instead)
Values are also similar to elements as they also contain info */

# - Dictionaries use curly brackets instead of just brackets when assigning a dictionary
#The KEYS have to be immutable and unique
#The VALUES can be immutable, mutable, and duplicates


'''

dictionary = {"Thriller" = 1982, "Back in Black" = 1980, "The Dark Side of the Moon" = 1973, "The Bodyguard" = 1992}

# - Using brackets with the dictionary + key can give you the value or output

dictionary["The Bodyguard"]

# - Using the brackets with the key can also add another row of indexes and values (Be careful with spelling so you dont accidently add one)

dictionary["Bat Out of Hell"]

# - You can check whether a key is in the dictionary by using the "in" command by outputting True or False

"The Bodyguard" in dictionary

# - You can view all the keys and values by using dictionary.keys (Or Values) to view all

dictionary.values()
dictionary.keys()
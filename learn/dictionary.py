#Accessing Values
#https://www.tutorialspoint.com/python/pdf/python_dictionary.pdf

dict = {'Name': 'Zara',
        'Age': 7,
        'Class': 'First'};
print "dict['Name']: ", dict['Name']
print "dict['Age']: ",  dict['Age']

## update existing entry
dict['Age'] = 8;

print "dict['Name']: ", dict['Name']
print "dict['Age']: ",  dict['Age']

#Delete Dictionary Elements
del dict['Name']; # remove entry with key 'Name'
print "dict['Name']: ", dict['Name']
print "dict['Age']: ",  dict['Age']

dict.clear(); # remove all entries in dict
del dict ; # delete entire dictionary

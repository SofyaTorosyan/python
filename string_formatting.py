person = {'name': 'John', 'age':23}
sentence = 'My naae is ' + person['name'] + '  and I am ' + str(person['age']) + ' years old.'
print(sentence)

# better way to do above
# in old python versions it does not work - need to specify indexes
# sentence_better = 'My name is {}'.format(person['name'])
sentence_better = 'My name is {0} and I am {1} years old'.format(person['name'], person['age'])
print(sentence_better)

tag = 'hi'
text = 'This is a headline'
senetnce_1 = '<{0}>{1}</{0}>'.format(tag,text)
print(senetnce_1)


# the same as sentence_better
sentence_2 = 'My name is {0[name]} and I am {1[age]} years old'.format(person, person)
print(sentence_2)

# for lists
list = ['Jane', 23]
sentence_3 = 'My name is {0[0]} and I am {1[1]} years old'.format(list, list)
print(sentence_3)

sentence_4 = 'My name is {name} and I am {age} years old'.format(name = 'Jane', age = 32)
print(sentence_4)


# unpack dictionary
sentence_5 = 'My name is {name} and I am {age} years old'.format(**person)
print(sentence_5)

# format and print numbers
# for i in range(1,11):
#    sentence = 'The value is {:02}'.format(i) #adding 0 make numbers 2 digit `` 1 01 2 02
#    print sentence

pi = 3.14159265
sentence_5 ='Pi is equal to {0:.3f}'.format(pi) #only 3 decimal points

# format and print dates
import datetime
date = datetime.datetime(2020, 2, 7, 16, 8, 7)
print date

# month day, year
s ='{0:%B %d, %Y}'.format(date)
print(s)











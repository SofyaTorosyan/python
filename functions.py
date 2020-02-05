def hello1():
    print("hello!")
    
hello1()

def hello2():
    return 'hello!'
    
print(hello2().upper())

def hello3(greeting, name = 'You'):
    return '{} {}'.format(greeting, name)
    
print(hello3('Hi'))
print(hello3('Hi', 'World'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Staistics']
info    = {'name': 'David', 'age': '22'}
    
student_info('Math', 'Statistics', name = 'David', age = '22')
student_info(*courses, **info) # unpacks argument


# leap year example
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year % 4 == 0 and ( year % 100 == 0 or year % 400 == 0 )
    
    
def days_in_month(month, year):
    if not  1 <= month <= 12:
        return 'Invalid input' 
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]
    

print( is_leap(2020) )
print( days_in_month(2, 2000) )
print( days_in_month(0, 2000) )

    
    
    
    

    
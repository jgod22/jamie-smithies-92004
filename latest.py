input("What is your name? \n")
bool_choice = False
str_userChoice =''


print('''Plese pick your answer: 
Question 1 - What iconic line does Gandalf say to the Balrog in Lord of the rings?
A Go away
b Get over here
c You shall not pass 
d Why did you make me do this ''')

'''
What Mr and I have done is we have set a if else so
that if i input something other than A B C D it says invalid And i'd I put A B or D
it says wrong and if it says C it says correct. And bool_choice makes it so that
once answeres moves onto the next question and doesnt stay in a loop.
'''

while bool_choice is False:
    str_userChoice = input('What leter will you pick A.B.C.D?:')
    if str_userChoice == 'a': 
        print('Wrong - try again - try again')
        bool_choice = False
    elif str_userChoice == 'b': 
        print('Wrong - try again - try again')
        bool_choice = False
    elif str_userChoice == 'c': 
        print('Correct - good job')
        bool_choice = True
    elif str_userChoice == 'd': 
        print('Wrong - try again - try again')
        bool_choice = False
    else:
        print('Invalid answer - try again')
        
while bool_choice is True:
    print('''Question 2 - What is the name of the person who wrote the lord of the rings books?)
A Wilbur Smith 
B J. K. Rowling 
C Stephen King 
D J. R. R. Tolkien''')
    str_userChoice = input("What leter will you pick A.B.C.D?: ")
    if str_userChoice == 'a': 
        print('Wrong - try again')
        bool_choice = True
    elif str_userChoice == 'b': 
        print('Wrong - try again')
        bool_choice = True
    elif str_userChoice == 'c': 
        print('Wrong - try again')
        bool_choice = True
    elif str_userChoice == 'd': 
        print('correct - well done')
        bool_choice = False
    else:
        print('Invalid answer - try again')
        
        
while bool_choice is True:
    print('''Question 3 - What is the name of the second movie in the lord of the rings series?
A  lord of the rings and the chamber of secrots
b  lord of the rings the 2 towers
c  lord of the rings The Return of the King. 
d  lord of the rings behold dark child''')
    str_userChoice = input("what leter will you pick A.B.C.D?: ")
    if str_userChoice == 'a': 
        print('Wrong - try again')
        bool_choice = True
    elif str_userChoice == 'b': 
        print('Wrong - try again')
        bool_choice = True
    elif str_userChoice == 'c': 
        print('correct')
        bool_choice = False
    elif str_userChoice == 'd': 
        print('Wrong - try again')
        bool_choice = True
    else:
        print('Invalid answer - try again')
        
        
while bool_choice is False:
    print('''Question 4 - Which lord of the rings movie made the most money?
    A The Lord of the Rings: The Return of the King
    B The Lord of the Rings: gotham fights back
    C The Lord of the Rings: 2 rings
    D The Lord of the Rings: fellowship of the rings''')
    str_userChoice = input("What leter will you pick A.B.C.D?: ")
    if str_userChoice == 'a': 
        print('correct')
        bool_choice = True
    elif str_userChoice == 'b': 
        print('Wrong - try again')
        bool_choice = True
    elif str_userChoice == 'c': 
        print('Wrong - try again')
        bool_choice = True
    elif str_userChoice == 'd': 
        print('Wrong - try again')
        bool_choice = True
    else:
        print('Invalid answer - try again')


while bool_choice is True:
    print('''Question 5 - What's the name of the main character of The Lord of the Rings?
    A golum
    b leglus
    c tom
    d frodo''')
    str_userChoice = input("what leter will you pick A.B.C.D?")
    if str_userChoice == 'a': 
        print('Wrong - try again')
        bool_choice = False
    elif str_userChoice == 'b': 
        print('Wrong - try again')
        bool_choice = False
    elif str_userChoice == 'c': 
        print('Wrong - try again')
        bool_choice = False
    elif str_userChoice == 'd': 
        print('correct')
        bool_choice = False
    else:
        print('Invalid answer - try again')
        
        
while bool_choice is True:        
    print('''Question 6 - What is the name of the director of the Lord of the rings movies?
    A Clint eastwood
    B Jamie smithies
    C Peter Jackson
    D James cameron''')
    str_userChoice = input("what leter will you pick A.B.C.D?: ")
    if str_userChoice == 'a': 
        print('Wrong - try again')
        bool_choice = True
    elif str_userChoice == 'b': 
        print('Wrong - try again')
        bool_choice = True
    elif str_userChoice == 'c': 
        print('correct')
        bool_choice = True
    elif str_userChoice == 'd': 
        print('Wrong - try again')
        bool_choice = True
    else:
        print('Invalid answer - try again')
   
    
    print('''Question 7 - Who is the main villain of the lord of the rings series?    
    A Sauron
    b Frodo
    c Godzilla
    d Golum''')
    str_userChoice = input("What leter will you pick A.B.C.D?")
    if str_userChoice == 'a': 
        print('correct')
        bool_choice = False
    elif str_userChoice == 'b': 
        print('Wrong - try again')
        bool_choice = False
    elif str_userChoice == 'c': 
        print('Wrong - try again')
        bool_choice = False
    elif str_userChoice == 'd': 
        print('Wrong - try again')
        bool_choice = False
    else:
        print('Invalid answer - try again')
    
    
    print('''Question 8 - How meany Oscars did Return of the King get?
    A 11
    B None
    C 15
    D 4''')
    str_userChoice = input("What leter will you pick A.B.C.D?: ")
    if str_userChoice == 'a': 
        print('correct')
        bool_choice = True
    elif str_userChoice == 'b': 
        print('Wrong - try again')
        bool_choice = True
    elif str_userChoice == 'c': 
        print('Wrong - try again')
        bool_choice = True
    elif str_userChoice == 'd': 
        print('Wrong - try again')
        bool_choice = True
    else:
        print('Invalid answer - try again')

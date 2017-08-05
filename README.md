# fun_stuff_4_damien
fun mini projects for Damien to learn to code in python

Task 1:
    Let's learn about strings, integers, if statements, functions, and for loops!
    1) Open up the python command line by typing:
    >>> python
    
    2) An integer is a number. It can be positive or negative but is always a whole number.
       For example: 1, 500, -20, 0 are all integers.
                    1.1, 2/5, -4.5, 0.0, are not integers.
       Make an integer of value 2 and store it in a variable called num1.
    >>> num1 = 2
       Make another integer of value 3 and store it in a variable called num2.
    >>> num2 = 2
        
    3) What is num1+num2? 
       What is num1-num2? 
       What is num1*num2? 
       What is num1/num2?
       What is num1**num2? (** means 'to the power of' so this means we are going to multiply
            num1 times itself num2 number of times aka: num1*num1*num1)       
    
    4) A string is a series of letters or 'characters'. We can signify a string by surrounding 
       it in quotes (aka: " " or ' ').
       Make a string called name1 with value hannah and a string called name2 with value damien.
    >>> name1 = 'hannah'
    >>> name2 = 'damien'
    
    5) What is name1+name2?
       What is name1[0]?
       What is name1[0:3]?
       What is name1[-1]?
       What is name1[2:-1]?
       What is len(name1)?
       What is name2[0].upper() + name2[1:]?
       What is num1 + name1? Hmm...let's try this instead: str(num1) + name1?
       What is str(num1) + str(num2)?
       What is name1[0].upper() + name1[1:] + " is " + str(num2-num1) + " year younger than " + name2[0].upper() + name2[1:] + "."?
       
    6) What is num1//num2? This is called integer division which means any decimal point/fraction gets dropped.
       3//4 = 0
       7//2 = 3
       etc...
    
    5) What if num1 = 4 instead of 3? Then the sentence would be:
    >>> name1[0].upper() + name1[1:] + " is " + str(num2-num1) + " year younger than " + name2[0].upper() + name2[1:] + "."?
        'Hannah is 2 year younger than Damien.'
       That's not really proper grammar though. So let's fix that...
       If the number is 1 then we want to use the word 'year' otherwise we want to use the word 'years'. For this we will use an
       'if-else statement'.
       >>> if num2-num1 == 1:
               name1[0].upper() + name1[1:] + " is " + str(num2-num1) + " year younger than " + name2[0].upper() + name2[1:] + "."
           else:
               name1[0].upper() + name1[1:] + " is " + str(num2-num1) + " years younger than " + name2[0].upper() + name2[1:] + "."
       TADA! All fixed!
    6) It's getting kind of annoying having to write that whole sentence out every time. Let's make a function to do it for us!
    >>> def write_sentence(age1, age2, name1, name2):
            if age2-age1 == 1:
               return name1[0].upper() + name1[1:] + " is " + str(age2-age1) + " year younger than " + name2[0].upper() + name2[1:] + "."
            else:
               return name1[0].upper() + name1[1:] + " is " + str(age2-age1) + " years younger than " + name2[0].upper() + name2[1:] + "."
    
    Let's test it out!
    >>> write_sentence(num1, num2, name1, name2)
    >>> write_sentence(10, 60, 'damien', 'grandpa')
    
    7) Let's try some loops! What if we want to spell damien backwards?
       We need to print the last letter first, the second to last letter next, etc...
    >>> name2[-1]+name2[-2]+name2[-3]+name2[-4]+name2[-5]+name2[-6]
       Well that worked, but it's a little annoying to type that whole thing out and what if the name didn't have 6 letters? Then we
       would have to change the code. Let's use a loop and store the reversed name in a new variable!
       Here we are going to use the range function to make a list of integers to loop over. range(1, 6, 1) starts at 1 and counts up
       to 6 in increments of 1 (1, 2, 3, 4, 5). range(0, 6, 2) starts at 0 and counts up to 6 in increments of 2 (0, 2, 4). We can
       also count down by setting a negative increment: range(6, 0, -1) starts at 6 and counts down to 0 in increments of 1 (6,5,4,3,2,1).
       Notice it always stops when it gets to the final number (aka the final number isn't included in the count).
    >>> reversed_name2 = ''
    >>> for letter_position in range(-1, (len(name2)+1)*-1, -1):
            reversed_name2 = reversed_name2 + name2[letter_position]
    >>> reversed_name2  
    
    Can you change the above code so it uses positive indexes instead of negative indexes?
        aka: name2[5]+name2[4]+name2[3]+name2[2]+name2[1]+name2[0]
       
    
Task 2:
    Make a Word class that checks if a word is a palindrome. See Word.py for more details.
    To run this code. Type:
    >>> python Word.py
    You can also add this directory to your path so then you can import the file and use it from inside the python console.
    >>> python
    >>> import sys; sys.path.append(r'/fun_stuff_4_damien') # you may need to replace this with the actual location of the directory/folder.
    >>> from Word import Word
    >>> name = Word('hannah')

Task 3:
    Make Word class maintain the case of a word when it reverses it. So
    Damien reverses to Neimad instead of neimaD.

Task 4:
    Make a new file called Geometry.py. It will request from a user the type of shape and the
    demensions of the shape.

    Make a new class inside Geometry.py called Rectangle. Rectangle will have attributes
    length and height. An attribute is a characteristic of a class. For example in the Word
    class it had the property self._word.

    Next add a method called area. This will return the area of the Rectangle. Print this
    value to the screen in the __main__.

    Try adding a more complicated shape like a triangle or a trapizoid. (Maybe you can use this
    to cheat a little bit in Geometry class.)


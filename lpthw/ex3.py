print "I will now count my chickens:"

print "Hens", 25+30/6 # This performs order of operations for the answer to be 30.
print "Roosters", 100-25*3%4 # This performs order of operations by the modulus (%). Here you begin by multiplying (3%4) even though it's not in parenthesis of this operation in that way before taking 100-25(12%) to then have 100-25(.12) = 100-3= 97

print "Now I will count the eggs:" # Python prints out this statement.

print 3+2+1-5+4%2-1/4+6 # Here you begin by performing order of operations by multiplying (4%2) even though it's not in parenthesis to then have the problem set become 3+2+1-5+(8%)-1/4+6. Second, this will become 6-5+(8%)-1/4+6. Third, you have 6-5+(.08)-0.25+6. Fourth, you have 6-5+(.08)+5.75. Next, you have 6-5+5.83 = (1+5.83) = 6.83 = 7. Note: in Python, it rounds answer to nearest whole number. So, instead of 6.83 you have an answer of 7. 

print "Is it true that 3+2<5-7?" # Python prints out this question. 

print 3+2<5-7 # Python automatically prints out "False" because 5 is not less than -2. 

print "What is 3+2?", 3+2 # Python prints out the question followed by the answer of "5" it calculates automatically. 
print "What is 5-7?", 5-7 # Python prints out the question folleded by the answer of "-2" it calculates automatically. 

print "Oh, that's why it's False." # Python prints out this statement.

print "How about some more." # Python prints out this statement. 

print "Is it greater?", 5>-2 # Python prints out this question followed by automatically printing the answer of "True" since 5 is greater than -2. 
print "Is it greater or equal?", 5>=-2 # Python prints out this question followed by automatically printing the answer of "True" since 5 is greater than but not equal to -2. 
print "Is it less or equal?", 5<=-2 # Python prints out this question followd by automatically printing the answer of "False" since 5 is greater than and not equal to -2. 


print " "
print " "
                                    # Using "ex3.py" and rewriting it as floating point numbers. 

print "I will now count my chickens:"

print "Hens", 25.0+30.0/6.0 # This performs order of operations for the answer to be 30.0.
print "Roosters", 100.0-25.0*3.0%4.0 # This performs order of operations by the modulus (%). Here you begin by multiplying (3%4) even though it's not in parenthesis of this operation in that way before taking 100-25(12%) to then have 100-25(.12) = 100-3= 97.0

print "Now I will count the eggs:" # Python prints out this statement.

print 3.0+2.0+1.0-5.0+4.0%2.0-1.0/4.0+6.0 # Here you begin by performing order of operations by multiplying (4.0%2.0) even though it's not in parenthesis to then have the problem set become 3.0+2.0+1.0-5.0+(8.0%)-1.0/4.0+6.0. Second, this will become 6.0-5.0+(8.0%)-1.0/4.0+6.0. Third, you have 6.0-5.0+(0.08)-0.25+6.0. Fourth, you have 6.0-5.0+(0.0)-0.25+6.0. Next, you have 1.0-0.25+6.0 = (0.75+6.0) = 6.75. Note: in Python, it rounds answer to nearest tenth or hundredth depending on the defined floating point number given. Because of the (4.0%2.0) or (0.08), Python reads this as (0.0) when making calculations. Also in (1.0/4.0), Python reads this as (0.25) that's why you have a floating point number to 2 decimal places read to the hundredth. So, all in all you have an answer of 6.75 that Python has calculated. This problem when worked out has Python's actual answer to be: (6.0-5.0+0.0-0.25+6.0)= 6.75 and not (6.0-5.0+0.0-0.25+6.0)=6.83 as a regular calculator would calculate. Plus, this example answers problem #4 in the Study Drills section as to why the math "seems" wrong not being a calculator's answer of "6.83" but instead it's Python's answer of 6.75. 
# Note: Python follows PEDMAS as in Parenthesis, Exponents, Division, Multiplication, Addition, and Subtraction order of operations. 

print "Is it true that 3.0+2.0<5.0-7.0?" # Python prints out this question. 

print 3+2<5-7 # Python automatically prints out "False" because 5.0 is not less than -2.0. 

print "What is 3.0+2.0?", 3.0+2.0 # Python prints out the question followed by the answer of "5.0" it calculates automatically. 
print "What is 5.0-7.0?", 5.0-7.0 # Python prints out the question folleded by the answer of "-2.0" it calculates automatically. 

print "Oh, that's why it's False." # Python prints out this statement.

print "How about some more." # Python prints out this statement. 

print "Is it greater?", 5.0>-2.0 # Python prints out this question followed by automatically printing the answer of "True" since 5.0 is greater than -2.0. 
print "Is it greater or equal?", 5.0>=-2.0 # Python prints out this question followed by automatically printing the answer of "True" since 5 is greater than but not equal to -2.0. 
print "Is it less or equal?", 5.0<=-2.0 # Python prints out this question followd by automatically printing the answer of "False" since 5 is greater than and not equal to -2.0. 

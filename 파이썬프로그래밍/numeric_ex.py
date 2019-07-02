#numeric_ex.py

#1
print( '{0:=^50}'.format( '1¹ø' ) )
velocity = input( 'Input velocity : ' )
distance = input( 'Input distance : ' )

#time = eval( distance + '/' + velocity )
time = int(distance) / int(velocity)

print()
print( 'velocity : {0:<6.2f}'.format( float( velocity ) ) )
print( 'distance : {0:<6.2f}'.format( float( distance ) ) )
print( 'time     : {0:<6.2f}'.format( time ) )

#2
print( '{0:=^50}'.format( '2¹ø' ) )
length = input( 'Input length : ' )
width = input( 'Input width : ' )

#area = eval( length + '*' + width )
area =  int(length) * int(width)
#circumference = eval( length + '*' + '2' + '+' + width + '*' + '2' )
circumference =  int(length) * 2 + int(width) *2

print()
print( 'length : {0:<6.2f}\twidth : {1:<6.2f}'.format( float( length ), float( width ) ) )
print( 'area : {0:<6.2f}'.format( area ) )
print( 'circumference : {0:<6.2f}'.format( circumference ) )

#3
print( '{0:=^50}'.format( '3¹ø' ) )
fahrenheit = float( input( 'Input fahrenheit : ' ) )

celsius = ( fahrenheit - 32 ) / 1.8

print()
print( 'fahrenheit : {0:<6.2f} -> celsius : {1:<6.2f}'.format( fahrenheit, celsius ) )

#4
print( '{0:=^50}'.format( '4¹ø' ) )
number1 = int( input( 'Input number1 : ' ) )
number2 = int( input( 'Input number2 : ' ) )

add = number1 + number2
subtract = number1 - number2
multiple = number1 * number2
divide = number1 / number2

print()
print( '{0:^6} + {1:^6} = {2:<6}'.format( number1, number2, add ) )
print( '{0:^6} - {1:^6} = {2:<6}'.format( number1, number2, subtract ) )
print( '{0:^6} * {1:^6} = {2:<6}'.format( number1, number2, multiple ) )
print( '{0:^6} / {1:^6} = {2:<6.2f}'.format( number1, number2, divide ) )


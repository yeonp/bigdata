#class_struct_calculator.py
class Calculator:
    def __init__( self ):
        self.result = 0
        self.op = { 1:'+', 2:'-', 3:'*', 4:'/' }
        
    def calculate( self, number1, number2, op_select ):
        self.result = eval( number1 + self.op[op_select] + number2 )
        return self.result

class ControlCalculator:
    def __init__( self ):
        self.calculator = Calculator()
        
    def calculate( self, number1, number2, op_select ):
        self.result = self.calculator.calculate( number1, number2, op_select )
        return self.result

class ViewCalculator:
    def __init__( self ):
        self.controlCalculator = ControlCalculator()
        self.op = { 1:'+', 2:'-', 3:'*', 4:'/' }
        
    def DisplayCalculator( self ):
        print( '\n' )
        self.number1 = input( 'Input number1 (0:end): ' )
        while self.number1 != '0':       
            self.number2 = input( 'Input number2 : ' )
            self.op_select = int( input( 'Input operator( 1:+, 2:-, 3:*, 4:/ ) : ' ) )
            if self.op_select == 0:
                break;
            self.result = self.controlCalculator.\
                               calculate( self.number1, self.number2, self.op_select )
            print( '\n{0:^6} {2:^3} {1:^6} = {3:<.2f}'.\
                   format( self.number1, self.number2, self.op[ self.op_select ], self.result ) )
            print( '\n' )
            self.number1 = input( 'Input number1 (0:end): ' )
        return

if __name__ == '__main__':
    viewCalculator = ViewCalculator()
    viewCalculator.DisplayCalculator()
    








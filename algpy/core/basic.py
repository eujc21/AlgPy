######### Basic -  A class for basic mathematical calculations #########
class AlgPyBasic(object):
    #----------------------------------------------------------------------
    """docstring for Basic."""
    def __init__(self, arg):
        super(AlgPyBasic, self).__init__()
        self.arg = arg
        self.functions = {
            'sum': self.sum,
            'subtract': self.subtract,
        }
    #----------------------------------------------------------------------
    def run(self):
        """ Distribute operation through registering a function """
        operation = self.arg
        print self.functions[operation]()

    #----------------------------------------------------------------------
    def sum(self):
        """ sums all arguments passed through the input """
        inputOfTuple = input('Enter your arguments, seperated by commas:  ')
        result = 0
        if isinstance(inputOfTuple, tuple):
            for x in inputOfTuple:
                result += x
            return result

    #----------------------------------------------------------------------
    def subtract(self):
        """ subtract all numbers passed through the input """
        inputOfTuple = input('Enter argument in order of subtraction:  ')
        if isinstance(inputOfTuple, tuple):
            result = inputOfTuple[0]
            for x in inputOfTuple:
                index = inputOfTuple.index(x)
                if(index != 0):
                    result -= x
            return result

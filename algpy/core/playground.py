from .basic import AlgPyBasic

if __name__ == '__main__':
    ### User input to choose what kind of basic calculations they want to use ###
    basicOperation = raw_input("Please choose an operation: sum, subtract:  ")
    operate = AlgPyBasic(basicOperation)
    operate.run()

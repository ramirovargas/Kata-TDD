class Solver:

    def calculate(self, cadena):
        arr=[]
        if(len(cadena)==0):
            arr.append(0)


        result = [x.strip() for x in cadena.split(',')]
        return arr
class Solver:

    def calculate(self, cadena):
        arr=[]
        if(len(cadena)==0):
            arr.append(0)
            arr.append(0)
            arr.append(0)
            arr.append(0)


        else:
            result = [int(x.strip()) for x in cadena.split(',')]
            arr.append(len(result))
            arr.append(min(result))
            arr.append(max(result))
            arr.append(int(sum(result)/len(result)))
        return arr


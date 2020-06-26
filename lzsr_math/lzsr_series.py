import math

class Isochromatic():
    def Isochromatic_Firstitem(Lastitem:int,tolerance:int,Numberofitems:int):
        differtence = tolerance*Numberofitems-tolerance
        return(int(Lastitem-differtence))

    def Isochromatic_Lastitem(Firstitem:int,tolerance:int,Numberofitems:int):
        differtence = tolerance*Numberofitems-tolerance
        return(int(Firstitem+differtence))

    def Isochromatic_tolerance(Firstitem:int,Lastitem:int,Numberofitems:int):
         product = Lastitem-Firstitem
         differtenceofLastitemandFirstitem = Numberofitems-1
         return(int(product/differtenceofLastitemandFirstitem))

    def Isochromatic_Numberofitems(Firstitem:int,Lastitem:int,tolerance:int):
        product = Lastitem-Firstitem
        return (int(product/tolerance+1))



class Proportional():
    def Proportional_Firstitem(Lastitem:int,Commonrato:int,Numberofitems:int):
        quotient = Commonrato**Numberofitems/Commonrato
        return(int(Lastitem/quotient))

    def Proportional_Lastitem(Firstitem:int,Commonrato:int,Numberofitems:int):
        quotient = Commonrato**Numberofitems/Commonrato
        return(int(Firstitem*quotient))

    def Proportional_Commonrato(Firstitem:int,Lastitem:int,Numberofitems:int):
         power = Lastitem/Firstitem
         quotientofLastitemandFirstitem = Numberofitems-1
         return(int(power**(1/quotientofLastitemandFirstitem)))

    def Proportional_Numberofitems(Firstitem: int, Lastitem: int, Commonrato: int):
        power = Lastitem / Firstitem
        return(int(math.ceil(math.log(power,Commonrato)+1)))



class Fibonacci():
    def Fibonacci_Specifyitem(ordinalnumbersofitem: int):
        a = 1
        b = 1
        for __count in range(ordinalnumbersofitem-3):
            c = a+b
            a = b
            b = c
        return c

    def Fidonacci_ordinalnumbersofitem(Specifyitem: int):
        a = 0
        while True:
            a += 1
            if (Fibonacci.Fibonacci_Specifyitem(a) == Specifyitem):
                return a
            else:
                if (Fibonacci.Fibonacci_Specifyitem(a) > Specifyitem):
                    return 'Specifyitem is not in Fidonacci series. '



class Catalan():
    def Catalan_Specifyitem(ordinalnumbersofitem: int):
        if ordinalnumbersofitem == 0 or ordinalnumbersofitem == 1:
            return 1
        else:
            return (4 * ordinalnumbersofitem - 2) * Catalan.Catalan_Specifyitem(ordinalnumbersofitem - 1) // (ordinalnumbersofitem + 1)

    def Catalan_ordinalnumbersofitem(Specifyitem: int):
        a = 0
        while True:
            a += 1
            if Catalan.Catalan_Specifyitem(a) == Specifyitem:
                return a
            elif Catalan.Catalan_Specifyitem(a) > Specifyitem:
                return 'Specifyitem is not Catalan number. '



class special():
 class Pascaltriangle():
    def Pascaltriangle_Specifyrow(ordinalnumbersofrow: int):
        ordinalnumbersofrowordinalnumbersofrow = [[1]]
        for i in range(1, ordinalnumbersofrow):
            ordinalnumbersofrowordinalnumbersofrow.append([(0 if j == 0 else ordinalnumbersofrowordinalnumbersofrow[i - 1][j - 1]) + (0 if j == len(ordinalnumbersofrowordinalnumbersofrow[i - 1]) else ordinalnumbersofrowordinalnumbersofrow[i - 1][j]) for j in range(i + 1)])
        return ordinalnumbersofrowordinalnumbersofrow[-1]

    def Pascaltriangle_ordinalnumbersofrow(Specifyrow: list):
        a = 0
        while True:
            a += 1
            if special.Pascaltriangle.Pascaltriangle_Specifyrow(a) == Specifyrow:
                return a
            else:
                if special.Pascaltriangle.Pascaltriangle_Specifyrow(a) > Specifyrow:
                    return 'Specifyrow is not in Pascal triangle. '


 class LookAndSay():
        def LookAndSay_Specifycontent(content: int):
            lista = list(str(content))
            # 同样数值的计数器 i
            i = 1
            # 依次弹出列表的数值
            a = lista.pop(0)
            # 处理look_s = '1'的情况
            if len(lista) == 0:
                return int(str(i) + a)
            # 结果集
            listb = ''
            while len(lista) > 0:
                s = lista.pop(0)
                if a == s:
                    i += 1
                else:
                    listb = listb + str(i) + a
                    a = s
                    i = 1
                # 处理最后弹出的情况
                if len(lista) == 0:
                    listb = listb + str(i) + s
            return int(listb)

        def LookAndSay_Specifyitem(ordinalnumbersofitem:int):
            a = '1'
            for __count in range(ordinalnumbersofitem-1):
                a = special.LookAndSay.LookAndSay_Specifycontent(a)
            return a

        def LookAndSay_ordinalnumbersofitem(Specifyitem: int):
            if Specifyitem == 1:
                return 1
            else:
                a = 0
                while True:
                    a += 1
                    if special.LookAndSay.LookAndSay_Specifyitem(a) == Specifyitem:
                        return a
                    elif int(special.LookAndSay.LookAndSay_Specifyitem(a)) > Specifyitem:
                        return 'Specifyitem is not in Look-and-say series. '



__version__ = '1.2.4'
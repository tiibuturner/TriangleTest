
## Tiina Ylimäki

def typeTriangle(a,b,c):
    if (a > 0 and b > 0 and c > 0):
        if(a + b > c and a + c > b and b + c > a):
            if (a==b and b==c):
                return 'Kolomio o tasasivune'
            elif (a==b or b==c or a==c):
                return 'Kolomio o tasakylykine'
            else:
                return 'Kolomio o epäsäännölline'
        else:
            return "Ei oo validi kolomio"
    else:
        return "Annoit negatiivisia numeroota, ei oo kolomio"
    

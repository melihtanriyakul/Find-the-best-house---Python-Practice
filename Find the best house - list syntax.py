import sys
inputfile = sys.argv[1]
myfile = open (inputfile, "r" )

def calculateTotalCost(list):
    resultList = []
    for j in list:
        total = int(j[0]) + (int(j[1])*int(10)) + ( int(j[0]) * float(j[2]) * 10 )
        resultList.append(total)
    return resultList

def displayCost(list):
    displaylist = calculateTotalCost(BulletList)
    a = 1
    print( "The total cost of each house : \n" )
    for k in displaylist:
        print( str(a) + ". house's total cost is " + str(k) )
        a += 1

def selectBestBuy(list):
    BestBuyList = calculateTotalCost(BulletList)
    cheap = BestBuyList[0]
    val = 1
    for s in BestBuyList:
        if ( s < cheap):
            cheap = s
            val = BestBuyList.index(s)+1

    print( "You should select " + str(val) + ". house whose total cost is " + str(cheap) + ".")

BulletList = []
for i in myfile.readlines():
    BulletList.append(i.split())

displayCost(BulletList)
selectBestBuy(BulletList)
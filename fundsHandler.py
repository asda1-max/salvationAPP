import json

dataSoF = {}

def addfunds():
    print("")

def addSoF():
    loadSoFData()
    idSearcher = len(dataSoF)
    SoF = ["Debit Card", "E-Wallet", "Money", "Credit Card", "Pay Pal"]
    SoFName = input("Source of Fund Name : ")

    for i, item in enumerate(SoF,1):
        print(i,". ", item)

    while True :
        try :
            typeSoF = int(input("Source of Fund Type (1-5):"))
            if 0 < typeSoF <=5:
                break
        except ValueError :
            print("Fatal Error : No Option")

    typeSoFName = SoF[typeSoF - 1]
    
    ownerSoF = input ("Owner Name    : ")
    detailSoF = input("Other Details : ")
    idSearcher += 1000

    dataSoF[idSearcher] = {
        "SoFName" : SoFName,
        "typeSoFName" : typeSoFName,
        "ownerSoF" : ownerSoF,
        "detailSoF" : detailSoF
    }
    saveSoFData()


    
def saveSoFData():
    with open("SOF_data.json", "w") as file :
        json.dump(dataSoF,file, indent=4)

def loadSoFData():
    global dataSoF
    try :
        with open("SOF_data.json", "r") as file :
            dataSoF = json.load(file)
    except :
        print("\nFailed loading data files, Creating a new one...\n")




    

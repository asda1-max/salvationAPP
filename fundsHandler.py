import json
import os

dataSoF = {}

def addfunds():
    viewAllData()
    findData = False
    pilihan = int(input("Source of Fund Type ID : "))

    for item in dataSoF:
        if int(item) == pilihan :
            findData = True
            amountEdit(item)
            break

    if findData == False:
        print ("No Such ID \n")

def searchSoF():
    viewAllData()
    findData = False
    pilihan = int(input("Source of Fund Type ID : "))

    for item in dataSoF:
        if int(item) == pilihan :
            findData = True
            editSoF(item)
            break

    if findData == False:
        print ("No Such ID \n")

def editSoF(id):
    while True :
        print("You Are Editting Funds of : "+dataSoF[id]["SoFName"])
        print(r"""
            +----------------------------------------------+
            | Source of Funds Edit Menu :                  | 
            +----------------------------------------------+
            | Menu :                                       |
            |            1. Edit Name                      |
            |            2. Edit Owner                     |
            |            3. Edit Description               |
            |            4. Save and Exit                  | 
            |            5. Cancel (not saved)             | 
            +----------------------------------------------+
        """)
        while True:
            try:
                pilihan = int(input("Choose >"))
                break
            except ValueError:
                print("Err\n")

        match pilihan:
            case 1:
                newline = input("\nchange to :")
                dataSoF[id]["SoFName"] = newline
            case 2:
                newline = input("\nchange to :")
                dataSoF[id]["ownerSoF"] = newline
            case 3:
                newline = input("\nchange to :")
                dataSoF[id]["detailSoF"] = newline
            case 4:
                saveSoFData()
                break
            case 5:
                break
            case _ :
                pause()

def deleteSoF():
    viewAllData()
    try:
        deleteID = input("ID to be deleted : ")
        for i in dataSoF:
            if deleteID == i:
                while True :
                    sure = str(input("are u sure? (y/n)"))
                    if sure == "y":
                        dataSoF.pop(i, None)
                        break
                    elif sure == "n":
                        break
                    else:
                        print("No option")
                saveSoFData()
                break
            

    except ValueError:
        print("err val")


def amountEdit(id):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        viewData(id)
        print("You Are Editting Funds of : "+dataSoF[id]["SoFName"])
        print(r"""
          +----------------------------------------------+
          | Funds Edit Menu :                            | 
          +----------------------------------------------+
          | Menu :                                       |
          |            1. Add Funds                      |
          |            2. Decrease Funds                 |
          |            3. Auto add Rp100.000             |
          |            4. Auto Decrease Rp100.000        |
          |            5. Reset to 0                     | 
          |            6. Exit                           | 
          +----------------------------------------------+
        """)
        pilihan = int(input("Choose => "))
        match pilihan :
            case 1:
                while True :
                    try :
                        amount = int(input("Amount Added : "))
                        dataSoF[id]["currentFund"] += amount
                        saveSoFData()
                        break 
                    except ValueError:
                        print("Invalid Value")
            case 2:
                while True :
                    try :
                        amount = int(input("Amount Decrased : "))
                        if dataSoF[id]["currentFund"] < amount :
                            print("Your current fund is lower than decreased amount")
                            break
                        dataSoF[id]["currentFund"] -= amount
                        saveSoFData()
                        break 
                    except ValueError:
                        print("Invalid Value")
            case 3:
                try :
                    amount = 100000
                    dataSoF[id]["currentFund"] += amount
                    saveSoFData()
                     
                except ValueError:
                    print("Invalid Value")
            case 4:
                try :
                    amount = 100000
                    if dataSoF[id]["currentFund"] < amount :
                        print("Your current fund is lower than decreased amount")
                    else :        
                        dataSoF[id]["currentFund"] -= amount
                        saveSoFData()
                     
                except ValueError:
                    print("Invalid Value")
            case 5:
                try:
                    dataSoF[id]["currentFund"] = 0
                    saveSoFData() 
                    input("\nYour funds successfully reduced to 0\n\nPress space to continue...")
                except ValueError:
                    print("Invalid Value")
                    
            case 6:
                break

            case _ :
                print("no option found\n")
                pause()

    
def addSoF():
    # Generate a unique ID by finding the max existing key and adding 1, or start from 1000 if empty
    if dataSoF:
        idSearcher = max(int(k) for k in dataSoF.keys()) + 1
    else:
        idSearcher = 1000
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
    currentfund = 0

    dataSoF[idSearcher] = {
        "SoFName" : SoFName,
        "typeSoFName" : typeSoFName,
        "ownerSoF" : ownerSoF,
        "detailSoF" : detailSoF,
        "currentFund" : currentfund
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

def viewAllData():
    for i, item in  enumerate(dataSoF,1):
        print("->Source of Fund #" , i)
        viewData(item)

def viewData(item):
        w = 70
        print("+-------------------------------------------------------------------+")
        
        current_name_str = "| Source of Fund Name   : " + str(dataSoF[item]["SoFName"])
        right = (w-len(current_name_str)) - 2
        current_name_str = current_name_str + " " *right + "|"
        print(current_name_str)

        fundonrupiah = "{:,}".format(dataSoF[item]["currentFund"]).replace(",", ".")
        current_fund_str = "CURRENT FUND : RP" + fundonrupiah
        left = (w - len(current_fund_str)) // 2 - 2
        right = w - len(current_fund_str) - left -3
        current_fund_str = "+" + "-" * left + f"\033[91m{current_fund_str}\033[0m" + "-" * right + "+"
        print(current_fund_str)

        current_id_str = "| Source of Fund ID     : " + str(item)
        right = (w-len(current_id_str)) - 2
        current_id_str = current_id_str + " " *right + "|"
        print(current_id_str)  

        current_owner_str = "| Source of Fund Owner  : " + str(dataSoF[item]["ownerSoF"])
        right = (w-len(current_owner_str)) - 2
        current_owner_str = current_owner_str + " " *right + "|"
        print(current_owner_str)  

        current_detail_str = "| Source of Fund Detail : " + str(dataSoF[item]["detailSoF"])
        right = (w-len(current_detail_str)) - 2
        current_detail_str = current_detail_str + " " *right + "|"
        print(current_detail_str)  

        print("+-------------------------------------------------------------------+\n")


def pause():
    input("\npress space to continue")

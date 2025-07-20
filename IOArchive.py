from datetime import datetime
import fundsHandler
import json
from datetime import datetime, timedelta

ioHistory = {}

def addAnOutcome():
    inputName = input("Outcome Name : ")
    inputDesc = input("Outcome Description : ")
    while True:
        try:
            inputAmount = int(input("Outcome Amount : "))
            break
        except ValueError:
            print("Amount Have to be an Integer")

    inputAmountSTR = "Rp {:,}".format(inputAmount).replace(",", ".")
    fundsHandler.viewAllData()

    SoFID = str(input("ID to Choose : "))
    print(fundsHandler.dataSoF)
    if SoFID in fundsHandler.dataSoF:
        if fundsHandler.dataSoF[SoFID]["currentFund"] > inputAmount:
            fundsHandler.reduceFund(SoFID, inputAmount)
            if ioHistory:
                ioID = max(int(k) for k in ioHistory.keys()) + 1
            else:
                ioID = 0

            ioHistory[ioID] ={
                "inputName" : inputName ,
                "inputDesc" : inputDesc ,
                "inputAmount" : "-" + inputAmountSTR ,
                "inputTime": (datetime.utcnow() + timedelta(hours=7)).strftime("%Y-%m-%d %H:%M:%S"),
                "SoFName" : fundsHandler.dataSoF[SoFID]["SoFName"] ,
                "inputType" : "Outcome"
            }

            fundsHandler.saveSoFData()
            saveData()
        else:
            input("Data is not saved because data is invalid")
    else:
        input("Data is not saved because data asu")

def addAnIncome():
    inputName = input("Income Name : ")
    inputDesc = input("Income Description : ")
    while True:
        try:
            inputAmount = int(input("Income Amount : "))
            break
        except ValueError:
            print("Price Have to be an Integer")

    inputAmountSTR = "Rp {:,}".format(inputAmount).replace(",", ".")
    fundsHandler.viewAllData()

    SoFID = str(input("ID to Choose : "))
    print(fundsHandler.dataSoF)
    if SoFID in fundsHandler.dataSoF:
    
        fundsHandler.addFund(SoFID, inputAmount)
        if ioHistory:
            ioID = max(int(k) for k in ioHistory.keys()) + 1
        else:
            ioID = 0

        ioHistory[ioID] = {
            "inputName": inputName,
            "inputDesc": inputDesc,
            "inputAmount": inputAmountSTR,
            "inputTime": (datetime.utcnow() + timedelta(hours=7)).strftime("%Y-%m-%d %H:%M:%S"),
            "SoFName": fundsHandler.dataSoF[SoFID]["SoFName"],
            "inputType": "Income"
        }

        fundsHandler.saveSoFData()
        saveData()
    else:
        input("Data is not saved because data asu")

def saveData():
    with open("IOdata.json", "w") as file :
        json.dump(ioHistory,file, indent=4)

def loadData():
    try :
        with open("IOdata.json", "r") as file :
            global ioHistory
            ioHistory = json.load(file)
    except :
        print("\nFailed loading data files, Creating a new one...\n")

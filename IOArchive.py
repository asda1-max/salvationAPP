from datetime import datetime
import fundsHandler
import json
from datetime import datetime, timedelta

ioHistory = {}

def historyMonth():
    totalI = 0
    totalO = 0
    while True:
        curmonth =  input("Enter the month (YYYY-MM): ")
        if len(curmonth) == 7 and curmonth[:4].isdigit() and curmonth[5:7].isdigit() and curmonth[4] == '-':
            break
        else:
            print("Invalid format. Please enter the year in YYYY format.")
    for i in ioHistory:
        if ioHistory[i]["inputTime"].startswith(curmonth):
            if ioHistory[i]["inputType"] == "Income":
                totalI += int(ioHistory[i]["inputAmount"].replace("Rp", "").replace(".", "").replace("-", "").strip())
                
            if ioHistory[i]["inputType"] == "Outcome":
                totalO -= int(ioHistory[i]["inputAmount"].replace("Rp", "").replace(".", "").replace("-", "").strip())

            viewIO(i)
    w = 40
    wLI = w - len("{:,}".format(totalI).replace(",", "."))
    wLO = w - len("{:,}".format(totalO * -1).replace(",", "."))
    print("\n\033[42m\033[97m Total Income  : Rp {:,}".format(totalI).replace(",", ".") + " " * wLI + "\033[0m")
    print("\033[41m\033[30m Total Outcome : Rp {:,}".format(totalO * -1).replace(",", ".") + " " * wLO + "\033[0m")

def historyYear():
    totalI = 0
    totalO = 0
    while True:
        curyear = input("Enter the year (YYYY): ")
        if len(curyear) == 4 and curyear.isdigit():
            break
        else:
            print("Invalid format. Please enter the year in YYYY format.")
    for i in ioHistory:
        if ioHistory[i]["inputTime"].startswith(curyear):
            if ioHistory[i]["inputType"] == "Income":
                totalI += int(ioHistory[i]["inputAmount"].replace("Rp", "").replace(".", "").replace("-", "").strip())
                
            if ioHistory[i]["inputType"] == "Outcome":
                totalO -= int(ioHistory[i]["inputAmount"].replace("Rp", "").replace(".", "").replace("-", "").strip())

            viewIO(i)
    w = 40
    wLI = w - len("{:,}".format(totalI).replace(",", "."))
    wLO = w - len("{:,}".format(totalO * -1).replace(",", "."))
    print("\n\033[42m\033[97m Total Income  : Rp {:,}".format(totalI).replace(",", ".") + " " * wLI + "\033[0m")
    print("\033[41m\033[30m Total Outcome : Rp {:,}".format(totalO * -1).replace(",", ".") + " " * wLO + "\033[0m")

def historyAll():
    totalI = 0
    totalO = 0
    for i in ioHistory:
        if ioHistory[i]["inputType"] == "Income":
            totalI += int(ioHistory[i]["inputAmount"].replace("Rp", "").replace(".", "").replace("-", "").strip())
                
        if ioHistory[i]["inputType"] == "Outcome":
            totalO -= int(ioHistory[i]["inputAmount"].replace("Rp", "").replace(".", "").replace("-", "").strip())

        viewIO(i)
    w = 40
    wLI = w - len("{:,}".format(totalI).replace(",", "."))
    wLO = w - len("{:,}".format(totalO * -1).replace(",", "."))
    print("\n\033[42m\033[97m Total Income  : Rp {:,}".format(totalI).replace(",", ".") + " " * wLI + "\033[0m")
    print("\033[41m\033[30m Total Outcome : Rp {:,}".format(totalO * -1).replace(",", ".") + " " * wLO + "\033[0m")


def viewIO(id):
    if ioHistory[id]["inputType"] == "Income":
        print(f"\033[92mthere's an {ioHistory[id]['inputType']} on {ioHistory[id]['inputTime']}\033[0m")
        print(f"\033[92m|-> {ioHistory[id]['inputAmount']}\033[0m")
    else:
        print(f"\033[91mthere's an {ioHistory[id]['inputType']} on {ioHistory[id]['inputTime']}\033[0m")
        print(f"\033[91m|-> {ioHistory[id]['inputAmount']}\033[0m")
    
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

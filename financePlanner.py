import json
import os
import fundsHandler

planData = {}
globalData = []

def addplan():

    if planData :
        Id = max(int(i) for i in planData.keys()) + 1
    else:
        Id = 0

    while True :
        try :
            planName = str(input( "Plan Name         : "))
            planDesc = str(input( "Plan Description  : "))
            planPrice = int(input("Plan Price        : "))
            break
        except :
            print("Error 3.1 = Value Error, Check The Price, Should be Integer\n")
            pause()
    
    while True :
        try :
            while True :
                planPriotize = int(input("Plan Prioritize (1-10, higher more important) :"))
                planOutcome = int(input("Plan Benefit Outcome (1-10, higher more important) :")) 
                if 0 < planPriotize <= 10 or 0 < planOutcome <= 10:
                    break
                else :
                    print ("The Value should between 1 - 10")
                    pause()
            break
        except :
            print("Error 3.2 = Value Plan Error should be an Integer\n")
            pause()

    planData[Id] = {
        "planName" : planName,
        "planDesc" : planDesc,
        "planPrice" : planPrice,
        "planPrioritize" : planPriotize,
        "planOutcome" : planOutcome
    }

    saveData()


def saveData():
    with open("planData.json","w") as file :
        json.dump(planData, file, indent=4)

def loadData():
    global planData
    try :
        with open("planData.json","r") as file :
            planData = json.load(file)
    except :
        print("Cant open Data File")

def dataPriorityD():
    i = 0
    global globalData
    globalData = []
    for id in planData:
        i+=1
        valueOfPlan = float((int(planData[id]["planPrioritize"]) * 0.7) + (int(planData[id]["planOutcome"]) * 0.3))
        normalizedValueOfPlan = float(valueOfPlan / 10)

        curPrice = int(planData[id]["planPrice"])

        if curPrice <= 100000:
            level = "Cheap"
            score = float(5 - curPrice * 0.00000002)
        elif 100000 < curPrice <= 500000:
            level = "Medium"
            score = float(4 - curPrice * 0.00000002)
        elif 500000 < curPrice <= 1000000:
            level = "High"
            score = float(3 - curPrice * 0.00000002)
        elif 1000000 < curPrice <= 5000000:
            level = "Very High"
            score = float(2 - curPrice * 0.00000002)
        elif 5000000 < curPrice:
            level = "Extremely High"
            score = float(1 - curPrice * 0.00000002)

        normalizedPriceScore = float(score / 5.0)
        finalscore = float((0.7 * normalizedValueOfPlan) +  (0.3 * normalizedPriceScore))
        globalData.append({"planName" : planData[id]["planName"],
        "planId" : id,
        "planDesc" : planData[id]["planDesc"],
        "planPrice" : planData[id]["planPrice"],
        "planPrioritize" : planData[id]["planPrioritize"],
        "planOutcome" : planData[id]["planOutcome"],
        "planPriceLevel" : level,
        "finalScore" : finalscore
        })

def viewAllPlanModified():
    
    totalPrice = totalPricePlan() 
    totalFunds = fundsHandler.countAllFundAvaiable() 
    print("Your ALL Current Plan : \n")
    viewAllPlan()
    print("\n|-> Your Total Price : Rp {:,}".format(totalPrice).replace(",", "."))
    print("|-> Your Funds From All Saving : Rp {:,}".format(totalFunds).replace(",", "."))

    if totalFunds < totalPrice:
        print("\033[37;41m|-> You Are Lacking Money Of : Rp {:,} \033[0m".format((totalPricePlan() - fundsHandler.countAllFundAvaiable()) * -1).replace(",", "."))
    else :
        print("\033[37;42m|-> You Have Surplus Money Of : Rp {:,} \033[0m".format((fundsHandler.countAllFundAvaiable() - totalPricePlan())).replace(",", "."))

def totalPricePlan():
    totalPrice = 0
    for i in planData:
        totalPrice += planData[i]["planPrice"]
    return totalPrice

def viewAllPlan():
    globalData.sort(key=lambda x: x["finalScore"], reverse=True)
    # Print header with black foreground and white background
    print(" \033[30;47m| {:<3} | {:<3}  | {:<30} | {:<15} | {:<12} | {:<10} | {:<15} | {:<10} | {:<35}  \033[0m".format(
        "no","ID", "Plan Name", "Price", "Priority", "Outcome", "Price Level", "Score", "Description                        "
    ))
    print(" " + "-" * 162)
    for idx, plan in enumerate(globalData, 1):
        desc = plan['planDesc']
        desc_lines = [desc[i:i+30] for i in range(0, len(desc), 30)]
        price_rupiah = f"Rp {int(plan['planPrice']):,}".replace(",", ".")
        
        if idx == 1:
            print(" \033[30;102m| {:<3} | \033[30;48;5;208m {:<3}\033[30;102m | {:<30} | {:<15} | {:<12} | {:<10} | {:<15} | {:<10.6f} | {:<35} |".format(
            idx,
            plan['planId'],
            plan['planName'],
            price_rupiah,
            plan['planPrioritize'],
            plan['planOutcome'],
            plan['planPriceLevel'],
            plan['finalScore'],
            desc_lines[0]
            ))
        else:
            print(" | {:<3} | \033[30;103m {:<3}\033[0m | {:<30} | {:<15} | {:<12} | {:<10} | {:<15} | {:<10.6f} | {:<35} |".format(
            idx,
            plan['planId'],
            plan['planName'],
            price_rupiah,
            plan['planPrioritize'],
            plan['planOutcome'],
            plan['planPriceLevel'],
            plan['finalScore'],
            desc_lines[0]
            ))
        if idx == 1:
            print("\033[0m", end="")   # Reset text color
        for cont_line in desc_lines[1:]:
            print(" | {:<3} | \033[30;103m {:<3}\033[0m | {:<30} | {:<15} | {:<12} | {:<10} | {:<15} | {:<10} | {:<35} | ".format(
                '', '','', '', '', '', '', '', cont_line
            ))


    print(" " + "-" * 162)

def editPlanData():
    viewAllPlan()
    isDataFounded = False
    inputID = str(input("Which ID you want to Edit : "))
    for id in planData:
        if inputID == id:
            editMenu(id)
            isDataFounded = True
            break

    if isDataFounded != True:
        print("No ID has been Found")

def viewOnePlan(id):
    for plan in globalData:
        if str(plan['planId']) == str(id):
            print ("\033[31mPLAN NAME : ", plan['planName'],"\033[0m")
            print ("-" * 40)
            print ("|->Description    : ",plan['planDesc'])
            print ("|->Price          : ",plan['planPrice'])
            print ("|->Priority Value : ",plan['planPrioritize'])
            print ("|->Outcome Value  : ",plan['planOutcome'])
            print ("-" * 40 + "\n")

            print("Price Level : ", plan["planPriceLevel"])
            print("Final Score : ",plan["finalScore"])

def deletePlan():
    dataPriorityD()
    viewAllPlan()
    while True:
        print("Which One You Want to Delete? (Type 'cancel' to cancel)")
        deleteData = str(input("ID to Delete : "))
        if deleteData in planData:
            confirmation = input(f"are you sure you want to delete {planData[deleteData]["planName"]} ? (y/n) : ").strip().lower()
            if confirmation == 'y':
                planData.pop(deleteData, None)
                saveData()
                break
            else:
                print("The Deletion has been cancelled successfully")
                pause()
                break
        else:
            print("No such ID found.\n")
            pause()

def editMenu(id):
        while True:
            dataPriorityD()
            os.system('cls' if os.name == 'nt' else 'clear')
            viewOnePlan(id)
            print(r"""
            +----------------------------------------------+
            | Plan Edit Menu :                             | 
            +----------------------------------------------+
            | Menu :                                       |
            |            1. Edit Plan Name                 |
            |            2. Edit Price                     |
            |            3. Edit Description               |
            |            4. Edit Plan Priority             |
            |            5. Edit Plan Outcome              |
            |            6. Exit                           | 
            +----------------------------------------------+
            """)
            inputChoose = str(input("Choose an option = "))

            match inputChoose :

                case "1" :
                    userInput = str(input("Change Plan Name Into : "))
                    planData[id]["planName"] = userInput

                case "2" :
                    while True :
                        try:
                            userInput = int(input("Change Plan Price Into : "))
                            planData[id]["planPrice"] = userInput
                            break
                        except ValueError:
                            print("err 3.2 Value Error")

                case "3" :
                    userInput = str(input("Change Plan Description Into : "))
                    planData[id]["planDesc"] = userInput

                case "4" :
                    while True :
                        try:
                            while True :
                                userInput = int(input("Change Plan Priority Value Into : "))
                                if 0 < userInput <= 10: 
                                    planData[id]["planPrioritize"] = userInput
                                    break
                                else :
                                    print("Value Error Choose Between 1 - 10")
                            break
                        except ValueError:
                            print("err 3.2 Value Error")
                case "5" :
                    while True :
                        try:
                            while True :
                                userInput = int(input("Change Plan Outcome Value Into :" ))
                                if 0 < userInput <= 10: 
                                    planData[id]["planOutcome"] = userInput
                                    break
                                else :
                                    print("Value Error Choose Between 1 - 10")
                            break
                        except ValueError:
                            print("err 3.2 Value Error")

                case "6" :
                    break

                case _ :
                    print("No Option")

            print("The Data Has Been Saved Successfully\n")
            pause()
            saveData()



        

    


def pause():
    input("Press Enter to Continue...")



    
    

    

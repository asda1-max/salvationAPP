import json

planData = {}

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
    sortedArray = []
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

        sortedArray.append({"planName" : planData[id]["planName"],
        "planId" : id,
        "planDesc" : planData[id]["planDesc"],
        "planPrice" : planData[id]["planPrice"],
        "planPrioritize" : planData[id]["planPrioritize"],
        "planOutcome" : planData[id]["planOutcome"],
        "planPriceLevel" : level,
        "finalScore" : finalscore
        })

    sortedArray.sort(key=lambda x: x["finalScore"], reverse=True)
    # Print header with black foreground and white background
    print("\033[30;47m\n{:<3} {:<3} {:<30} {:<15} {:<12} {:<10} {:<15} {:<10} {:<35}\033[0m".format(
        "no","ID", "Plan Name", "Price", "Priority", "Outcome", "Price Level", "Score", "Description                        "
    ))
    print("-" * 141)
    for idx, plan in enumerate(sortedArray, 1):
        desc = plan['planDesc']
        desc_lines = [desc[i:i+30] for i in range(0, len(desc), 30)]
        price_rupiah = f"Rp{int(plan['planPrice']):,}".replace(",", ".")
        if idx == 1:
            print("\033[102m", end="")  # Set background color to green
        if idx == 1:
            print("{:<3} \033[48;5;208m{:<3}\033[102m {:<30} {:<15} {:<12} {:<10} {:<15} {:<10.6f} {:<35}".format(
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
            print("{:<3} \033[103m{:<3}\033[0m {:<30} {:<15} {:<12} {:<10} {:<15} {:<10.6f} {:<35}".format(
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
            print("{:<3} {:<3} {:<30} {:<15} {:<12} {:<10} {:<15} {:<10} {:<30}".format(
                '', '','', '', '', '', '', '', cont_line
            ))
    print("-" * 141)

def pause():
    input("Press Enter to Continue...")



    
    

    

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
    dataPriorityD()

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
            score = float(5 - curPrice * 0.0000002)
        elif 100000 < curPrice <= 500000:
            level = "Medium"
            score = float(4 - curPrice * 0.0000002)
        elif 500000 < curPrice <= 1000000:
            level = "High"
            score = float(3 - curPrice * 0.0000002)
        elif 1000000 < curPrice <= 5000000:
            level = "Very High"
            score = float(2 - curPrice * 0.0000002)
        elif 5000000 < curPrice:
            level = "Extremely High"
            score = float(1 - curPrice * 0.0000002)

        normalizedPriceScore = float(score / 5.0)
        finalscore = float((0.7 * normalizedValueOfPlan) +  (0.3 * normalizedPriceScore))

        sortedArray.append({"planName" : planData[id]["planName"],
        "planDesc" : planData[id]["planDesc"],
        "planPrice" : planData[id]["planPrice"],
        "planPrioritize" : planData[id]["planPrioritize"],
        "planOutcome" : planData[id]["planOutcome"],
        "planPriceLevel" : level,
        "finalScore" : finalscore
        })

    sortedArray.sort(key=lambda x: x["finalScore"], reverse=True)
    print("\n{:<3} {:<20} {:<10} {:<12} {:<10} {:<15} {:<10} {:<10}".format(
        "No", "Plan Name", "Price", "Priority", "Outcome", "Price Level", "Score", "Description"
    ))
    print("-" * 100)
    for idx, plan in enumerate(sortedArray, 1):
        print("{:<3} {:<20} {:<10} {:<12} {:<10} {:<15} {:<10.4f} {:<10}".format(
            idx,
            plan['planName'],
            plan['planPrice'],
            plan['planPrioritize'],
            plan['planOutcome'],
            plan['planPriceLevel'],
            plan['finalScore'],
            plan['planDesc'][:30]  # Truncate description for neatness
        ))
    print("-" * 100)

def pause():
    input("Press Enter to Continue...")



    
    

    

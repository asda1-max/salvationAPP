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
                planPriotize = int(input("Plan Prioritize (1-3, lesser more important) :"))
                if 0 < planPriotize < 4:
                    break
                else :
                    print ("The Value should between 1 - 3")
                    pause()
            break
        except :
            print("Error 3.2 = Value Plan Error should be an Integer\n")
            pause()
    
    planList = ["Top Priority", "Priority", "Less Priority"]
    planPriotizeText = planList[planPriotize-1]

    planData[Id] = {
        "planName" : planName,
        "planDesc" : planDesc,
        "planPrice" : planPrice,
        "planPrioritize" : planPriotizeText
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
    
def pause():
    input("Press Enter to Continue...")



    
    

    

import os
import fundsHandler
import IOArchive
import financePlanner
from CopyrightLicence import copyright

def main():
    while True:
        fundsHandler.loadSoFData()
        financePlanner.loadData()
        os.system('cls' if os.name == 'nt' else 'clear')

        print(r""" 
         
███████╗ █████╗ ██╗    ██╗   ██╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔════╝██╔══██╗██║    ██║   ██║██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
███████╗███████║██║    ██║   ██║███████║   ██║   ██║██║   ██║██╔██╗ ██║
╚════██║██╔══██║██║    ╚██╗ ██╔╝██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
███████║██║  ██║███████╗╚████╔╝ ██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
╚══════╝╚═╝  ╚═╝╚══════╝ ╚═══╝  ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
             
          /| ________________
    O|===|* >________________> --Your Life Savior (Finance Management)
          \|                     

          +----------------------------------------------+
          | Welcome to Salvation Program :               | 
          +----------------------------------------------+
          | Menu :                                       |
          |             1. Source of Funds               |
          |             2. Finance Planner               |
          |             3. Income and Outcome            |
          |             4. Copyright                     |
          |             5. Exit                          |
          +----------------------------------------------+
              
         """)
        pilih = input("Choose an Option = >")
        os.system('cls' if os.name == 'nt' else 'clear')
        match pilih:
            case '1':
                sourceOfFunds()
            case '2':
                fplanner()
            case '3':
                ioArchive()
            case '4':
                copyright()
                pause()
            case '5':
                exit()
            case _ :
                print("no option found\n")
                pause()
            

def sourceOfFunds():
    while True :
        os.system('cls' if os.name == 'nt' else 'clear')
        print(r"""
          +----------------------------------------------+
          | Source of Funds Menu :                       | 
          +----------------------------------------------+
          | Menu :                                       |
          |            1. Edit Funds                     |
          |            2. Add Source of Fund             |
          |            3. Edit Source of Fund            |
          |            4. Delete Source of Fund          |
          |            5. View Source of Fund            |
          |            6. Back to Main Menu              |      
          +----------------------------------------------+
            """)
        pilih = input("Choose an Option = > ")
        os.system('cls' if os.name == 'nt' else 'clear')
        match pilih:
            case '1':
                print( "\n--You choosed Add Funds Menu --\n")
                fundsHandler.addfunds()
                pause()
            case '2':
                print( "\n--You choosed Add Source of Fund Menu --\n")
                fundsHandler.addSoF()
                pause()
            case '3':
                print( "\n--You choosed Edit Source of Fund Menu --\n")
                fundsHandler.searchSoF()
            case '4':
                print( "\n--You choosed Delete Source of Fund Menu --\n")
                fundsHandler.deleteSoF()
            case '5':
                print( "\n--You choosed View Source of Fund Menu --\n")
                fundsHandler.viewAllData()
                pause()
            case '6':
                break
            case _ :
                    print("no option found\n")
                    pause()
    
def fplanner():
    while True:
        financePlanner.dataPriorityD()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(r"""
          +----------------------------------------------+
          | Finance Planner menu :                       | 
          +----------------------------------------------+
          | Menu :                                       |
          |            1. Add A Plan                     |
          |            2. View Plan Priority             |
          |            3. Edit Plan                      |
          |            4. Delete Plan                    |
          |            5. Back to Main Menu              |
          +----------------------------------------------+
        """)
        pilih = input("Choose an Option = > ")
        os.system('cls' if os.name == 'nt' else 'clear')
        match pilih:
            case '1':
                financePlanner.addplan()
            case '2':
                financePlanner.viewAllPlanModified()
                pause()
            case '3':
                financePlanner.editPlanData()
            case '4':
                financePlanner.deletePlan()
            case '5':
                break
            case _ :
                    print("no option found\n")
                    pause()
    
def pause():
    input("\npress space to continue")


def ioArchive():
    while True:
        IOArchive.loadData()
        os.system('cls' if os.name == 'nt' else 'clear')
        totalFund = fundsHandler.countAllFundAvaiable()
        print(f"\033[91mYour Current Fund = {totalFund}\033[0m")
        print(r"""
          +----------------------------------------------+
          | Income and Outcome Archive menu :            | 
          +----------------------------------------------+
          | Menu :                                       |
          |            1. Add An Income                  |
          |            2. Add An Outcome                 | 
          |            3. View History                   | 
          |            4. Exit                           | 
          +----------------------------------------------+
        """)
        pilih = input("Choose an Option = > ")
        os.system('cls' if os.name == 'nt' else 'clear')
        match pilih:
            case '1':
                IOArchive.addAnIncome()
            case '2':
                IOArchive.addAnOutcome()
            case '3':
                history()
                pause()
            case '4':
                break
            case _ :
                    print("no option found\n")
                    pause()

def history():
    while True:
        IOArchive.loadData()
        os.system('cls' if os.name == 'nt' else 'clear')
        totalFund = fundsHandler.countAllFundAvaiable()
        print(f"\033[91mYour Current Fund = {totalFund}\033[0m")
        print(r"""
          +----------------------------------------------+
          | Income and Outcome Archive menu :            | 
          +----------------------------------------------+
          | Menu :                                       |
          |            1. History by Month               |
          |            2. History by Year                | 
          |            3. All Time History               | 
          |            4. Exit                           | 
          +----------------------------------------------+
        """)
        pilih = input("Choose an Option = > ")
        os.system('cls' if os.name == 'nt' else 'clear')
        match pilih:
            case '1':
                IOArchive.historyMonth()
                pause()
            case '2':
                IOArchive.historyYear()
                pause()
            case '3':
                IOArchive.historyAll()
                pause()
            case '4':
                break
            case _ :
                    print("no option found\n")
                    pause()

if __name__ == "__main__":
    main()

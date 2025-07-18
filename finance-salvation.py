import os
import fundsHandler
import financePlanner

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
          |             3. Exit                          |
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
                financePlanner.dataPriorityD()
                pause()
            case '3':
                financePlanner.editPlanData()
            case '4':
                financePlanner.dataPriorityD()
            case '5':
                break
            case _ :
                    print("no option found\n")
                    pause()
    
def pause():
    input("\npress space to continue")


if __name__ == "__main__":
    main()
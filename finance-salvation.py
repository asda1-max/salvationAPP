import os
import fundsHandler

def main():
    while True:
        fundsHandler.loadSoFData()
        os.system('cls' if os.name == 'nt' else 'clear')

        # Start of Menu
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
            #End of menu

def sourceOfFunds():
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
            print( "\n--You choosed Add Funds Menu --\n")
            print("a")
        case '4':
            print( "\n--You choosed Add Funds Menu --\n")
            print("a")
        case '5':
            print( "\n--You choosed View Source of Fund Menu --\n")
            fundsHandler.viewAllData()
            pause()
        case '6':
            print( "\n--You choosed Add Funds Menu --\n")
            print("a") 
    
def fplanner():
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
    match pilih:
        case '1':
            print("a")
        case '2':
            print("a")
        case '3':
            print("a")
        case '4':
            print("a")
        case '5':
            print("a")
    
def pause():
    input("\npress space to continue")

if __name__ == "__main__":
    main()
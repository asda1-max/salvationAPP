import os

def main():
    while True:
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
                print("a")
            case '3':
                exit()

def sourceOfFunds():
    print(r"""
          +----------------------------------------------+
          | Source of Funds Menu :                       | 
          +----------------------------------------------+
          | Menu :                                       |
          |            1. Add Funds                      |
          |            2. Add Source of Fund             |
          |            3. Edit Source of Fund            |
          |            4. Delete Source of Fund          |
          |            5. Back to Main Menu              |
          +----------------------------------------------+
         """)
    
def fplanner():
    print(r"""
          +----------------------------------------------+
          | Finance Planner menu :                       | 
          +----------------------------------------------+
          | Menu :                                       |
          |            1. Add A Plan                     |
          |            2. Edit Source of Fund            |
          |            3. Delete Source of Fund          |
          |            4. Back to Main Menu              |
          +----------------------------------------------+
         """)
    

if __name__ == "__main__":
    main()
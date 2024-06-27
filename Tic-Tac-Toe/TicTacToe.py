def printbord(xstring,zstring):
    zero='X' if xstring[0] else ('O' if zstring[0] else 0)
    one='X' if xstring[1] else ('O' if zstring[1] else 1)
    two='X' if xstring[2] else ('O' if zstring[2] else 2)
    three='X' if xstring[3] else ('O' if zstring[3] else 3)
    four='X' if xstring[4] else ('O' if zstring[4] else 4)
    five='X' if xstring[5] else ('O' if zstring[5] else 5)
    six='X' if xstring[6] else ('O' if zstring[6] else 6)
    seven='X' if xstring[7] else ('O' if zstring[7] else 7)
    eight='X' if xstring[8] else ('O' if zstring[8] else 8)

    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")

print("Welcome to the game!!!!!!")
if __name__ =="__main__":
    xstring=[0,0,0,0,0,0,0,0,0];
    zstring=[0,0,0,0,0,0,0,0,0];
    turn =1;#1 s for X's turn and 0 s for O'x turn 
    counter = 1

    def winn():
        solarry = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    # logic : to iterate in solarray(sol_item) => check xstring[sol_item[0]] == 1 AND check xstring[sol_item[1]] == 1 AND check xstring[sol_item[2]] == 1 If true x win else check same in zstring... 

        for sol_item in solarry:
          if xstring[sol_item[0]] == 1 and xstring[sol_item[1]] == 1 and xstring[sol_item[2]] == 1:
           print("X WINS THE GAME!")
           global counter
           counter = 0
           break
          elif zstring[sol_item[0]] == 1 and zstring[sol_item[1]] == 1 and zstring[sol_item[2]] == 1:
           print("Z WINS THE GAME!") 
           counter = 0
           break 
            

    while(counter == 1):
        printbord(xstring,zstring)
        if (turn == 1):
            print("X's chance")
            value = int(input("Enter a number :"))
            xstring[value] = 1
            turn = 1 - turn
            if winn():
               break
                                  
        else:
            print(counter,"cucboi")
            print("O's chance")
            value = int(input("Enter a number :"))
            zstring[value] = 1
            turn = 1
            if winn():
               break
           
        # method to check win on every iteration # winn()


       
def main():
    #Input

    teamName = input("Enter the team's name : ")
    numbersOfWins = int(input("Enter number of wins : "))
    numberOfLosses = int(input("Enter number of losses : "))

    #Processing

    totalGames = numbersOfWins + numberOfLosses
    winPct = numbersOfWins/totalGames
    #The Calgary Flames have 10 wins and 5 losses
    # with the win percentage of 0.6667
    print(winPct)

    #Output
    print("The {0} have {1} wins and {2} losses, with a win percentage of {3:.4f}.".format(teamName,numbersOfWins,numberOfLosses,winPct))
    


main()

class Euro2012:
    def __init__(self):
        import requests
        self.url = requests.get("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv")
        self.euro2012 = self.url.content
        self.lines = self.euro2012.decode("ASCII").splitlines()
        self.base_line = self.lines[0]
        self.estadistics = self.base_line.split(",")
        self.number_of_teams = 0
        for teams in self.lines:
            if teams == self.base_line:
                continue
            else:    
                self.number_of_teams = self.number_of_teams + 1




    def teams_data(self, team, stadistic):

        line_len = range(len(self.base_line.split(",")))

        for n in line_len:
            if self.estadistics[n] == stadistic:
                break

        for line in self.lines:
            line = line.split(",")
            if line[0] == team:
                break
    
        return print(f"{team}, {stadistic}:{line[n]}")
    
        print("--------------------------------------------------------------------------------------------------------------------------")


    def disciplina(self):

        line_len = range(len(self.base_line.split(",")))

        total_Y_cards = 0
        
        for team in self.lines:
            team = team.split(",")
            for s in line_len:
                if self.estadistics[s] == "Yellow Cards" and team[s].isnumeric():
                    total_Y_cards = total_Y_cards + int(team[s])  
                    print(f"{team[s]} \t \t {team[s+1]} \t \t {team[0]} ")
                elif self.estadistics[s] == "Yellow Cards":
                    print(f"{team[s]} \t {team[s+1]} \t {team[0]}")

        med_total_Y_cards = total_Y_cards/self.number_of_teams

        print(" ")

        print(f"{med_total_Y_cards} yellow cards each team")

        print("--------------------------------------------------------------------------------------------------------------------------")


    def goals(self, number):

        print(f"Teams with more than {number} goals:")
        print("    ")

        line_len = range(len(self.base_line.split(",")))

        for team in self.lines:
            if team == self.base_line:
                continue
            else:
                team = team.split(",")
                for s in line_len:
                    if self.estadistics[s] == "Goals" and int(team[s]) >= number :
                        print(f"{team[0]}, goals: {team[s]}")

        print("--------------------------------------------------------------------------------------------------------------------------")


    def columna(self, number):

        list = ""
        for n in range(number):
            list = list + self.estadistics[n] + "   "
        print(list)

        for m in self.lines:
            list = ""
            if m != self.base_line:
                m = m.split(",")
                for n in range(number):
                    list = list + m[n] + "    "
                print(list)
        print("--------------------------------------------------------------------------------------------------------------------------")
    
    def teams_by(self, letter):
        print(f"Teams that start with the letter: {letter}")
        for team in self.lines:
            if team.split(",")[0] == "Team":
                continue
            elif team[0] == letter:
                print(team.split(",")[0])
            
        print("--------------------------------------------------------------------------------------------------------------------------")
           



    





                        
                

euro12 = Euro2012()

print(f"Participaron {euro12.number_of_teams} equipos en la Euro 2012")

euro12.disciplina()

euro12.goals(6)

euro12.teams_by("G")

euro12.columna(7)

euro12.columna(len(euro12.estadistics)- 3)

euro12.teams_data("England", "Shooting Accuracy" )

euro12.teams_data("Russia", "Shooting Accuracy" )

euro12.teams_data("Italy", "Shooting Accuracy" )







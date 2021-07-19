from bs4 import BeautifulSoup
import requests

req = requests.get("https://teamcolorcodes.com/nba-team-color-codes/")
soup = BeautifulSoup(req.text, "lxml")

team_buttons = soup.find_all("a", class_="team-button")
with open("team_colors.csv", "w") as file:
    file.write("team, color, border_color\n")
    for team in team_buttons:
        team_name = team.text
        team_color = team["style"].split(": ")[1].split(";")[0]
        team_border_color = team["style"].split(" ")[-1].strip(";")
        file.write(f"{team_name}, {team_color}, {team_border_color}\n")

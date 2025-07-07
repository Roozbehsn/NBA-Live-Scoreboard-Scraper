from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

user_date = input("Enter the date (YYYY-MM-DD): ").strip()

url = f"https://www.nba.com/games?date={user_date}"

options = Options()
options.add_argument("--headless")   #comment if code not execute right
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

print(f"Loading NBA games page for {user_date}...")
driver.get(url)


time.sleep(15)  

html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, "html.parser")


games = soup.find_all("div", class_="GameCard_gc__UCI46")

if not games:
    print("No Games Scheduled.")
else:
    print(f"Found {len(games)} game(s):\n")
    for game in games:
        team_names = game.find_all("span", class_="MatchupCardTeamName_teamName__9YaBA")

        team1 = team_names[0].text.strip()
        team2 = team_names[1].text.strip()

        score_tags = game.find_all("p", class_="MatchupCardScore_p__dfNvc")
        if len(score_tags) != 2:
            score1 = score2 = "N/A"
        else:
            score1 = score_tags[0].text.strip()
            score2 = score_tags[1].text.strip()

        print(f"{team1} ({score1}) vs {team2} ({score2})")


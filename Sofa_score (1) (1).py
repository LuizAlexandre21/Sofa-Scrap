from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# Iniciando do Chromedriver
drive_options = webdriver.ChromeOptions()
drive_options.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies2": 2})
drive_options.add_argument("--disable-site-isolation-trials")
#drive_options.add_argument("--headless")
drive_options.add_argument('--no-sandbox')
drive_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path="/home/alexandre/Documentos/CRC/chromedriver_linux64 (2)/chromedriver",options=drive_options)

# Iniciando a Simulação do mouse
actions=ActionChains(driver)

# Iniciando a pagina da web
url = driver.get("https://www.sofascore.com/")
sleep(20)
# Abrindo a aba Campeonato Brasileiro
# Esperando a pagina abrir após 10 segundos
WebDriverWait(driver,10)
# Rolando a pagina
driver.execute_script("window.scrollBy(0,300)")
a=driver.find_element_by_xpath("//*[@href='/tournament/football/brazil/brasileiro-serie-a/325']")
a.click()
# Numero de rodadas
sleep(4)
driver.execute_script("window.scrollBy(0,900)")
driver.find_elements_by_link_text('BY ROUND')[0].click()

# Extrair o numero de rodadas jogadas
sleep(4)
#driver.find_element_by_xpath("//*[@class='styles__Wrapper-cdd802-0 iuumCP ItemizedEventList__Select-sc-1g9vtzd-0 wRSaA']").click()
Home_team = []
Away_team = []
Round = []
Goals_home =[]
Goals_aways =[]
num = ['1','2','3','4','5','6','7','8','9','0']
for i in range(0,37):
    volta=driver.find_elements_by_xpath("//*[@class='Content-sc-1o55eay-0 styles__HeaderNavigationContent-b3g57w-1 epVTwK']")
    volta[0].click()
for i in range(0,37):
    #driver.find_elements_by_xpath("//*[@class='styles__EventListContent-b3g57w-2 dotAOs']")
    partidas = driver.find_elements_by_xpath("//*[@class='EventCellstyles__Link-sc-1m83enb-0 dhKVQJ']")
    for k in range(0,len(partidas)):
        if k <10:
            print(k)
            b=partidas[0].find_element_by_xpath("//*[@class='Section-sc-1a7xrsb-0 hwkKwf']").find_elements_by_xpath("//*[@class='Content-sc-1o55eay-0 EventCellstyles__WinIndicator-ni00fg-4 kCvfzg']")[k]
            if b.text not in num:
                Home_team.append(b.text)
                Round.append(i)
            else:
                Goals_home.append(b.text)
            try:
                c = partidas[0].find_element_by_xpath("//*[@class='Section-sc-1a7xrsb-0 hwkKwf']").find_elements_by_xpath("//*[@class='Content-sc-1o55eay-0 EventCellstyles__WinIndicator-ni00fg-4 iCJwzy']")[k]
                if c.text not in num:
                    Away_team.append(c.text)
                else:
                    Goals_aways.append(c.text)
            except:
                c= partidas[0].find_element_by_xpath("//*[@class='Section-sc-1a7xrsb-0 hwkKwf']").find_elements_by_xpath("//*[@class='Content-sc-1o55eay-0 EventCellstyles__WinIndicator-ni00fg-4 kCvfzg']")[j]
                if k % 2==0:
                    Away_team.append(c.text)

    if i>24:
        for j in range(0,19):
            if j%2==0:
                e=partidas[0].find_elements_by_xpath("//*[@class='Content-sc-1o55eay-0 EventCellstyles__WinIndicator-ni00fg-4 kCvfzg']")[j]
                Home_team.append(e.text)
                Round.append(i)
            else:
                f = partidas[0].find_elements_by_xpath("//*[@class='Content-sc-1o55eay-0 EventCellstyles__WinIndicator-ni00fg-4 kCvfzg']")[j]
                Away_team.append(f.text)

    volta[1].click()
# Salvando os resultados das partidas do campeonato brasileiro
print(Home_team)



## Salvando o data frame

data=pd.dataframe({'Casa':Home_team,'Gols_Casa':Goals_home,'Gols_Fora':Goals_aways,'Fora':Away_team,})
data.to_csv("a.csv")

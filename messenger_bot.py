#!/usr/bin/python
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from random import randint

Mail2 = "YOUR_MAIL"
Pass2 = "PASSWORD"

def logi(mail:str, password:str):
    login = driver.find_element_by_xpath('//*[@id="email"]').send_keys(mail)
    haslo = driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
    sleep(4)
    loguj = driver.find_element_by_xpath('//*[@id="loginbutton"]')
    loguj.click()

def send_message(list_of_mess:tuple):
    for i in range(2,84):
        try:
            mess = list_of_mess[randint(0,len(list_of_mess)-1)]
            znaj = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div/div[{cos}]/div[1]/div/a/div[1]'.format(cos=i))
            znaj.click()
            sleep(2)
            cosa = driver.find_element_by_xpath('//br[@data-text=\"true\"]').send_keys(mess) # "Dosiego!!!") # mess
            sleep(2)
            wysl = driver.find_element_by_xpath('//div[@aria-label=\"Naciśnij klawisz Enter, aby wysłać\"]').click()
            sleep(2)
        except:
            pass

lista_zyczen = ("Niech na co dzień, nie od święta, gęba będzie uśmiechnięta. Niech też zdrowie tęgie będzie i kasiory niech przybędzie. Niechaj łaski płyną z nieba, tyle ile będzie trzeba. Do Siego Roku...!", 
                "Kolejny Sylwester, lecz życzenia te same - Byś w przyszłym roku wybudował zamek, byś miał sto koni i sto samochodów, i byś nigdy nie miał do płaczu powodów. Niech na co dzień, nie od święta. Buzia będzie uśmiechnięta. Niech też zdrowie tęgie będzie i pieniędzy niech przybędzie.",
                "Kuligiem chciałam do Was przyjechać, lecz kare konie nie chciały czekać. Porwały sanie, mkną pod gwiazdamia ja zostałam sama z życzeniami. Ale gdy tylko okno otworzycie,w świeżym płateczku życzenia złożę,w gwiazdce co spada tutaj z obłokówbędę życzyć: DOBREGO ROKU 2022!",
                "Fajerwerki, śnieg, muzyka, już szampana każdy łyka, stary rok się w Nowy zmienia, przeto szczęścia śle życzenia.",
                "Płoną sztuczne ognie,Płynie już muzyka,Idzie Nowy Rok, Stary Niech umyka.Więc wznieśmy puchary,Tańczmy do rana,Niech los nam nie szczędzi.Szczęścia i szampana!",
                "Szampana piccolo, Brokatu na czoło, Uśmiechu na twarzy, Szampańskiej zabawy, Życzeń serdecznych, Wspomnień najlepszych oraz braku kaca,kiedy w nowym roku pamięć wraca!",
                "Niech Nowy Rok przyniesie Ci radość, Miłość, pomyślność i spełnienie Wszystkich marzeń, a gdy się one jużSpełnią niech dorzuci garść nowychMarzeń, bo tylko one nadają życiu sens!W Nowym Roku wielu szczęśliwych tylko chwil.Szczęścia w domu i wszędzie, gdzie będziesz."
                )

if __name__ == "__main__":
	driver = webdriver.Chrome('/usr/bin/chromedriver')
	driver.get("https://www.messenger.com/t")
	try:
    		x = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]')
    		x.click()
	except:
    		pass
	sleep(2)
	logi(Mail2, Pass2)
	sleep(4)
	send_message(lista_zyczen)

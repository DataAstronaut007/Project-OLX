from selenium import webdriver
import time


browser = webdriver.Chrome('/Users/kamil/Downloads/chromedriver')
browser.maximize_window()
#browser.get('https://www.olx.pl/d/elektronika/gry-konsole/konsole/playstation/?search%5Border%5D=created_at:desc&search%5Bfilter_enum_state%5D%5B0%5D=used')
browser.get('https://www.olx.pl/d/elektronika/gry-konsole/konsole/?search%5Border%5D=created_at:desc&search%5Bfilter_enum_state%5D%5B0%5D=used')
browser.find_element_by_xpath('//button[text()="Akceptuję"]').click()
time.sleep(7)
browser.minimize_window()

while 2 > 1:
    
    
    zens = browser.find_elements_by_xpath("//a[contains(@href, 'oferta')]")
    result = []
    for zen in zens:
        x = (zen.get_attribute("href"))
        result.append(x)
        
    tabela_1 = result[3:10]
    print("-----------------------")
    

    time.sleep(90)
    browser.refresh()
    time.sleep(7)
    
    mens = browser.find_elements_by_xpath("//a[contains(@href, 'oferta')]")
    result_2 = []
    for men in mens:
        x = (men.get_attribute("href"))
        result_2.append(x)
    
    tabela_2 = result_2[3:10]
    
    res = [x for x in tabela_2 if x not in tabela_1]
    if not res:
        print("   Brak nowych aukcji")
        print("-----------------------")
    else:
        print("     Nowe aukcje")
        print("-----------------------")
        print(res)
        print("-----------------------")
        
    time.sleep(90)
    browser.refresh()
    time.sleep(7)
        
    dens = browser.find_elements_by_xpath("//a[contains(@href, 'oferta')]")
    result_3 = []
    for den in dens:
        x = (den.get_attribute("href"))
        result_3.append(x)
        
    tabela_3 = result_3[3:10]
    
    res = [x for x in tabela_3 if x not in tabela_2]
    if not res:
        print("   Brak nowych aukcji")
        print("-----------------------")
    else:
        print("     Nowe aukcje")
        print("-----------------------")
        print(res)
 


########Librerías
import sys
import os
import Functions as ft
from selenium import webdriver
import networkx as nx
import matplotlib.pyplot as plt
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from selenium.common.exceptions import (NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException, TimeoutException)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle

driver = webdriver.Chrome()
counter = 0

related = []
df = pd.read_csv('list.csv')
G = nx.DiGraph() #or G = nx.MultiDiGraph()

noBo = 1

ft.start(driver)
ft.login(driver)
longi =len(df)-1
print("Cantidad de BOs: %s \nNumero en loop: %s" % (len(df),longi))

try:
    for objeto in range(longi):
        print("Numero de loop %s" % counter)
        
        if counter == 0:
            print("Entro en condición counter == 0")
            ft.search('Business Object Details',driver)
            ft.BODetails(df.iloc[counter, 1], driver)
            ft.submit(driver)
                
            print("Completo busqueda de BO")
            print("Scrapping RBO y agrego nodos")   
            ft.guardarRBO(driver, related)
            G.add_node(df.iloc[counter, 0])
            
            for item in related:
                G.add_edge(df.iloc[counter, 0], item)
                
            print("Completo relaciones de: %s" % df.iloc[counter, 0])
            counter = counter + 1
            
        if counter > 0:
            print("Entro en condición counter > 0")
            
            related.clear()
            ft.close(driver)
            print("Cierro ventana, para inicar busqueda")
            ft.search('Business Object Details',driver)
            try:
                ft.BODetails(df.iloc[counter, 1], driver)
            except (TimeoutException,NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException):
                print("Salta excepcion de busqueda de BO BODetails")
                ft.cancel(driver)
                driver.implicitly_wait(10)
                ft.close(driver)
                driver.implicitly_wait(10)
                tarea = "bo:" + df.iloc[counter, 0]
                busquedaGlobal = driver.find_element(By.XPATH, "//input[@data-automation-id='globalSearchInput']")
                action = ActionChains(driver)
                action.click(on_element = busquedaGlobal)
                action.send_keys(tarea)
                action.send_keys(Keys.RETURN)
                action.perform()
                    
                task = driver.find_element(By.XPATH, "//a[text()='"+df.iloc[counter, 0]+"']")
                task.click()
                ft.guardarRBO(driver, related)
                    
                G.add_node(df.iloc[counter, 0])
                    
                for item in related:
                    G.add_edge(df.iloc[counter, 0], item)
            
            try:
                ft.submit(driver)  
            except (TimeoutException,NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException):
                print("Salta excepcion de busqueda de BO Submit")
                ft.cancel(driver)
                driver.implicitly_wait(10)
                ft.close(driver)
                driver.implicitly_wait(10)
                tarea = "bo:" + df.iloc[counter, 0]
                busquedaGlobal = driver.find_element(By.XPATH, "//input[@data-automation-id='globalSearchInput']")
                action = ActionChains(driver)
                action.click(on_element = busquedaGlobal)
                action.send_keys(tarea)
                action.send_keys(Keys.RETURN)
                action.perform()
                    
                task = driver.find_element(By.XPATH, "//a[text()='"+df.iloc[counter, 0]+"']")
                task.click()
                ft.guardarRBO(driver, related)
                    
                G.add_node(df.iloc[counter, 0])
                    
                for item in related:
                    G.add_edge(df.iloc[counter, 0], item) 
                    
            print("Completo busqueda de BO")
            
            try: 
                ft.guardarRBO(driver, related)
            except (TimeoutException,NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException):
                print("Salta excepcion de busqueda de BO guardarRBO")
                ft.cancel(driver)
                driver.implicitly_wait(10)
                ft.close(driver)
                driver.implicitly_wait(10)
                tarea = "bo:" + df.iloc[counter, 0]
                busquedaGlobal = driver.find_element(By.XPATH, "//input[@data-automation-id='globalSearchInput']")
                action = ActionChains(driver)
                action.click(on_element = busquedaGlobal)
                action.send_keys(tarea)
                action.send_keys(Keys.RETURN)
                action.perform()
                    
                task = driver.find_element(By.XPATH, "//a[text()='"+df.iloc[counter, 0]+"']")
                task.click()
                ft.guardarRBO(driver, related)
                    
                G.add_node(df.iloc[counter, 0])
                    
                for item in related:
                    G.add_edge(df.iloc[counter, 0], item)
            
            print("Scrapping RBO y agrego nodos")  
                
            G.add_node(df.iloc[counter, 0])
                
            for item in related:
                G.add_edge(df.iloc[counter, 0], item)
            
            
            print("Completo relaciones de: %s" % df.iloc[counter, 0])
            counter = counter + 1
            
except (TimeoutException,NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException):
    print("Salta excepción total")
    ft.cancel(driver)
    driver.implicitly_wait(10)
    ft.close(driver)
    driver.implicitly_wait(10)
    tarea = "bo:" + df.iloc[counter, 0]
    busquedaGlobal = driver.find_element(By.XPATH, "//input[@data-automation-id='globalSearchInput']")
    action = ActionChains(driver)
    action.click(on_element = busquedaGlobal)
    action.send_keys(tarea)
    action.send_keys(Keys.RETURN)
    action.perform()
    
    task = driver.find_element(By.XPATH, "//a[text()='"+df.iloc[counter, 0]+"']")
    task.click()
    ft.guardarRBO(driver, related)
    G.add_node(df.iloc[counter, 0])
    for item in related:
        G.add_edge(df.iloc[counter, 0], item)
        print(df.iloc[counter, 0])


print("Final de programa") 

pickle.dump(G, open('graph.pickle', 'wb'))

pos = nx.spring_layout(G)
nx.draw(G, with_labels=True)
plt.show()
        





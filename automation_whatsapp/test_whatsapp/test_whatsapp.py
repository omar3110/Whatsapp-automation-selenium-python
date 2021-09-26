from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
import sys
import time
# import pytest
# # import allure


driver = webdriver.Chrome("chromedriver")
driver.get("https://web.whatsapp.com/")
time.sleep(5)


def send_msg():
    name = input("\n enter a name: ")
    message = input("enter a message: ")

    # search = driver.find_element_by_class_name("_1Jn3C")
    # time.sleep(2)
    # search.send_keys(name)
    # time.sleep(1)

    search = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    time.sleep(1)
    search.click()

    time.sleep(3)

    text_box = driver.find_element_by_class_name("p3_M1")
    time.sleep(3)
    text_box.send_keys(message)
    time.sleep(5)

    button = driver.find_element_by_class_name("_4sWnG")
    time.sleep(1)
    button.click()
    time.sleep(1)


def message_status():

    time.sleep(10)
    deliver = driver.find_element_by_xpath(
        '//span[@aria-label = " Delivered "]')
    time.sleep(10)
    deliver.get_attribute('aria-label')

    time.sleep(5)

    if deliver == True:

        print("delivered")
    else:

        print("not delivered")


def read_status():

    time.sleep(5)
    deliver = driver.find_element_by_xpath(
        '//span[@aria-label=" Read "]')

    time.sleep(5)
    deliver.get_attribute('aria-label')

    time.sleep(5)

    if deliver == True:

        print("read")
    else:

        print("not read")


def logout():

    menu = driver.find_element_by_xpath('//span[@data-testid="menu"]')
    time.sleep(2)
    menu.click()
    time.sleep(2)
    log_out = driver.find_element_by_xpath('//div[@aria-label="Log out"]')
    time.sleep(2)
    log_out.click()


send_msg()
message_status()
read_status()
logout()

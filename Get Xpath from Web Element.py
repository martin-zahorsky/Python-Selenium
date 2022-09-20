from selenium import webdriver
from selenium.webdriver.common.by import By

def get_xpath(element:webdriver) -> str:
    def bubleUp(element:webdriver) -> list:
        tag = element.get_attribute('tagName').lower()
        if tag == 'html':
            return ['html']
        else:
            parent = element.find_element(By.XPATH,'..')
            elements = parent.find_elements(By.XPATH,f'./{tag}')
            index = 1
            for index, el in enumerate(elements):
                if el == element:
                    break
            output = tag if len(elements) == 1 else tag + f'[{index + 1}]'
            next = bubleUp(parent)
            next.append(output)
            return next

    xpath_origin = ''
    for i in bubleUp(element):
        xpath_origin += '/' + i
    
    return xpath_origin

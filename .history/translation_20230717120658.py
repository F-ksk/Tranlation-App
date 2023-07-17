from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import PySimpleGUI as sg
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--log-level=3')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://translate.google.com/?hl=ja')

sg.theme('Dark')
layout = [
    [sg.Text('入力してください')],
    [sg.InputText(key='word')],
    [sg.Text('翻訳する言語を選んでください')],
    [sg.Radio('日本語', group_id='r', key='jap', default= True), 
        sg.Radio('英語', group_id='r', key='eng'), 
        sg.Radio('韓国語', group_id='r', key='kor')],
    [sg.Button('翻訳')],
    [sg.Text('-----------------', key='info', size=(40,2))]
]

win = sg.Window('Translation App', layout)
i = 0
while True:
    event, val = win.read()
    if event == sg.WINDOW_CLOSED: break
    if event == '翻訳':
        if(val['jap']):
            if(i  % 3 != 0):
                btn = driver.find_element_by_css_selector('button#i12')
                btn.click()
                time.sleep(1)
            el = driver.find_element_by_class_name('er8xn')
            word = val['word']
            el.send_keys(word)
            time.sleep(1)
            ans = driver.find_elements_by_css_selector('span.ryNqvb')
            for a in ans:
                win['info'].update(a.text)
            el.clear()
            i = 0;
        if(val['eng']):
            if(i % 3 != 1):
                btn = driver.find_element_by_css_selector('button#i13')
                btn.click()
                time.sleep(1)
            el = driver.find_element_by_class_name('er8xn')
            word = val['word']
            el.send_keys(word)
            time.sleep(1)
            ans = driver.find_elements_by_css_selector('span.ryNqvb')
            for a in ans:
                win['info'].update(a.text)
            el.clear()
            i = 1;
        if(val['kor']):
            if(i % 3 != 2):
                btn = driver.find_element_by_css_selector('button#i14')
                btn.click()
                time.sleep(1)
            el = driver.find_element_by_class_name('er8xn')
            word = val['word']
            el.send_keys(word)
            time.sleep(1)
            ans = driver.find_elements_by_css_selector('span.ryNqvb')
            for a in ans:
                win['info'].update(a.text)
            el.clear()
            i = 2
        
        
time.sleep(3)
driver.close()
win.close()

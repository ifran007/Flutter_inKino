import os

command = f"pytest -s --alluredir=report_allure testcases"

os.system(command)


command1= 'allure serve report_allure/'
os.system(command1)
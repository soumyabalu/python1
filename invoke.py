from selenium import webdriver  # here we are importing webdriver class from selenium

# driver = webdriver.Firefox()
driver = webdriver.Chrome()  # creating the object called driver for the class webdriver. Here webdriver is the class
# in selenium and chrome is a method in the webdriver class
driver.get("http://google.com")   # get method is used to hit the url
driver.maximize_window()  # to maximize the window
print(driver.name)  # will pprint the name of the underlying browser
print(driver.title)  # will print the title of the current page. title is a property which does not have a bracket at
# the end .p stands for property
print(driver.current_url)  # will print the current url ., helps us to make sure that we landed in the current url
driver.get("https://www.udemy.com/")
# driver.minimize_window()  # to minimize the window
driver.back()  # will go bone step backward in the browser history
# driver.forward()  # will go one step forward in the browser history
driver.refresh()  # will refresh the current page
driver.close()  # closes the browser along with the executables. quit is a method. it has bracket at the end . M stands
# for method
# driver.close()  # close the current window

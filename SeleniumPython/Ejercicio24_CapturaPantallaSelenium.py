from selenium import webdriver

driver = webdriver.Chrome(executable_path = r"C:\DriverChrome\chromedriver.exe")
driver.get("https://www.youtube.com/watch?v=DnsNYxDbaAA")
driver.get_screenshot_as_file("C:\\Users\\rjrtxh\\Documents\\SeleniumPython\\screenshot1.png")
driver.close()

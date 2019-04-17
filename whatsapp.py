from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

user = input("Enter the user name")
msg = input("Enter the message to be sent")
count = int(input("Enter the no. of times message to be sent"))
input("Enter anything after scanning")

user =  driver.find_element_by_xpath("//span[@title = '{}']".format(user))
user.click()
msg_box = driver.find_element_by_class_name("_2S1VP")


for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name("_35EW6")
    button.click()
    

from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


# open the chrome browser
browser=webdriver.Chrome(executable_path='C:\\Users\\Basavaraj\\PycharmProjects\\anushree_class\\chromedriver.exe')
browser.implicitly_wait(10)
# maximize the window and enter the URL
browser.maximize_window()
browser.get("https://grofers.com/")

# to handle unexpected hidden division pop up
try:
    if browser.find_element_by_xpath("//div[@class='location']").is_displayed():
        browser.find_element_by_xpath("//div[text()='Kolkata']").click()
        sleep(5)
except Exception:
   pass

#  this is a random click: this is to make sure that "page down" button is under  working
browser.find_element_by_xpath("//div[@title='Next Product']").click()

# click on "page down" button
for i in range(10):
    ActionChains(browser).send_keys(Keys.PAGE_DOWN).perform()
    sleep(2)

# click 'Grocery & Staples' link
browser.find_element_by_xpath("//a[text()='Grocery & Staples']").click()
sleep(4)

# click on 'Atta & other Flours'
browser.find_element_by_xpath("//span[text()='Atta & Other Flours']").click()


elements=browser.find_elements_by_xpath("//div[@class='plp-product']/descendant::div[@title='5 kg']/following-sibling::div[@class='relative']/div[@class='plp-product__add-to-cart']")
sleep(2)

# handled pop up
browser.find_element_by_xpath("//div[@class='wzrk-alert wiz-show-animate']")
browser.find_element_by_xpath("//button[text()='No, Thanks']").click()

product_names=browser.find_elements_by_xpath("// div[ @class ='plp-product'] / descendant:: div[ @ title = '5 kg'] /./preceding-sibling::div[@data-test-id='plp-product-name']")

#  element with 5kg variants : its product name are appended into list
p=[]
for product_name in product_names:
    print(product_name.text)
    p.append(product_name.text)

#  element with 5kg variants are added to cart
for element in elements:
    element.click()
    sleep(2)

# click on cart
browser.find_element_by_xpath("//div[@class='shopping-cart shopping-cart--empty']").click()

cart_prod_names=browser.find_elements_by_xpath("//div[@class='cart-items-product cart-card']/descendant::div[@class='product-name']")

#  in cart products with 5 kg variants are listed
cp=[]
for cp_name in cart_prod_names:
    print(cp_name.text)
    cp.append(cp_name.text)

# verify all the added items are there in cart
if len(p)==len(cp):
    p_set, cp_set=set(p), set(cp)
    if p_set==cp_set: print("Required items are added into cart ............: ")
else:
    print("some improper items have been added into cart......")

# close the browser
browser.close()

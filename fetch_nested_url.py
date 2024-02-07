from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
out_lines=[]
with open("base_links.txt", "r") as f:
    lines = f.read().splitlines()
    for line in lines:
        browser.get(line)

        elem = browser.find_element(By.CSS_SELECTOR, "[type='submit']")  # Find the search box
        elem.click()
        browser.switch_to.window(browser.window_handles[-1])
        url = browser.current_url
        print(f"current url : {url}")
        out_lines.append(url+'\n')
        
browser.close()

with open("links.txt", "w") as f_out:
    f_out.writelines(out_lines)


browser.quit()
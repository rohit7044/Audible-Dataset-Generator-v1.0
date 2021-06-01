
import time
import re
import audible_data_handling as adh
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options

book_title = ""
book_author = ""
book_narrator = ""
audio_runtime = ""
audiobook_type = ""
categories = ""
rating = ""
book_price = ""
reviews = ""
final_reviews_list =[]
book_data_list =[]
showmore_open_times = 0

def audible_homepage_open(audible_homepage_link,audible_link,open_times):
    global showmore_open_times
    showmore_open_times = open_times
    chrome_options = Options()
    chrome_options.add_extension('C:/chropath/extension_6_1_11_0.crx')
    driver = webdriver.Chrome(executable_path="C:/chromedriver/chromedriver.exe", chrome_options = chrome_options)
    driver.get(audible_homepage_link)
    driver.get(audible_link)
    return click_element(driver)

def click_element(driver):
    product_list = driver.find_elements_by_xpath("//div[contains(@data-widget,'productList')]/li")
    length_of_product_list = len(product_list)
    for item in range (1, length_of_product_list):
        book_link = driver.find_element_by_xpath("//div[contains(@data-widget,'productList')]/li["+str(item)+"]//li[1]//a")
        tab_switch(driver,book_link,item)
        print("end of "+book_link.text)
    try:
        nextButton = driver.find_element_by_xpath("//span[contains(@class,'nextButton')]")
        if nextButton.is_enabled():
            nextButton.click()
            click_element(driver)
        else:
            print("End of List")
    except:
        print("End of list")

def tab_switch(driver,book_link,item):
    book_link.send_keys(Keys.CONTROL + Keys.ENTER)
    driver.switch_to.window(driver.window_handles[1])
    fetch_element_data(driver,item)

def tab_close(driver):
    driver.close()
    driver.switch_to_window(driver.window_handles[0])

def fetch_element_data(driver,item):
    # global final_reviews_list
    try:
        book_title = (driver.find_element_by_xpath("//div[contains(@class,'centerSlot')][2]/div//li[1]")).text
        try:
            book_subtitle = (driver.find_element_by_xpath("//div[contains(@class,'centerSlot')][2]/div//li[2]")).text
            # print(book_subtitle)
        except:
            book_subtitle = ""
        book_author = (driver.find_element_by_xpath("//div[contains(@class,'centerSlot')][2]/div//li[contains(@class,'authorLabel')]/a")).text
        book_narrator = (driver.find_element_by_xpath("//div[contains(@class,'centerSlot')][2]/div//li[contains(@class,'narratorLabel')]/a")).text
        audio_runtime = (driver.find_element_by_xpath("//div[contains(@class,'centerSlot')][2]/div//li[contains(@class,'runtimeLabel')]")).text
        audiobook_type = (driver.find_element_by_xpath("//div[contains(@class,'centerSlot')][2]/div//li[contains(@class,'format')]")).text
        try:
            categories = (driver.find_element_by_xpath("//div[contains(@class,'centerSlot')][2]/div//li[contains(@class,'categoriesLabel')]/a")).text

        except:
            categories = ""
        try:
            rating = (driver.find_element_by_xpath("//div[contains(@class,'centerSlot')][2]/div//li[contains(@class,'ratingsLabel')]/span[2]")).text

        except:
            rating = ""
        try:
            total_ratings = (driver.find_element_by_xpath("//div[contains(@class,'centerSlot')][2]/div//li[contains(@class,'ratingsLabel')]")).text
            final_string = re.search(r'\((.*?)\)', total_ratings)
            ratings_cleaned = re.sub(r'[^0-9]', "", final_string.group(1))
        except:
            # total_ratings = ""
            ratings_cleaned = ""
        book_price = (driver.find_element_by_xpath("//a[contains(@title,"+"\""+book_title+"\""+")]")).text
        p_audio_runtime,p_book_price = adh.data_preprocessing(audio_runtime,book_price)
        final_reviews_list = reviews_crawler(driver)
        book_data_list = [book_title, book_subtitle, book_author,book_narrator, p_audio_runtime,audiobook_type, categories, rating,ratings_cleaned,p_book_price]
        adh.write_to_csv(book_data_list,final_reviews_list)
        tab_close(driver)
    except:
        final_reviews_list = reviews_crawler(driver)
        tab_close(driver)
        book_data_list = data_not_found(driver,item)
        adh.write_to_csv(book_data_list,final_reviews_list)

def reviews_crawler(driver):
    local_reviews_list = []
    total_review_columns = showmore_open_times*10
    adh.review_column_creator(total_review_columns)
    try:
        review_list = driver.find_elements_by_xpath("//div[contains(@class,'ReviewsTabUS')]/div/div[2]/p[1]")
        if not review_list:
            local_reviews_list = [""]*total_review_columns
        else:
            for review_item in range(1, showmore_open_times):
                time.sleep(3)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                more_reviews = driver.find_element_by_xpath("//span[contains(@class,'showMoreReviews')]")
                more_reviews.click()
            time.sleep(5)
            review_list = driver.find_elements_by_xpath("//div[contains(@class,'ReviewsTabUS')]/div/div[2]/p[1]")
            for item in range(1, len(review_list)):
                reviews = driver.find_element_by_xpath("//div[contains(@class,'ReviewsTabUS')]/div["+str(item)+"]/div[2]/p[1]")
                review_cleaned = re.sub(r'[^a-zA-Z0-9()\[\]\{\}.,!?\' */\"]', "", reviews.text)
                local_reviews_list.append(review_cleaned)
                if item == len(review_list)-1:
                    last_item = int(len(review_list))
                    reviews = driver.find_element_by_xpath("//div[contains(@class,'ReviewsTabUS')]/div[" +str(last_item)+ "]/div[2]/p[1]")
                    review_cleaned = re.sub(r'[^a-zA-Z0-9()\[\]\{\}.,!?\' */\"]', "", reviews.text)
                    local_reviews_list.append(review_cleaned)
            # print(local_reviews_list)


    except Exception as e:
        review_list = driver.find_elements_by_xpath("//div[contains(@class,'ReviewsTabUS')]/div/div[2]/p[1]")
        local_reviews_list = []
        if not review_list:
            local_reviews_list = [""] * total_review_columns
        else:
            for item in range(1, len(review_list)):
                reviews = driver.find_element_by_xpath("//div[contains(@class,'ReviewsTabUS')]/div["+str(item)+"]/div[2]/p[1]")
                review_cleaned = re.sub(r'[^a-zA-Z0-9()\[\]\{\}.,!?\' */\"]', "", reviews.text)
                local_reviews_list.append(review_cleaned)
                if item == len(review_list) - 1:
                    last_item = int(len(review_list))
                    reviews = driver.find_element_by_xpath("//div[contains(@class,'ReviewsTabUS')]/div[" + str(last_item) + "]/div[2]/p[1]")
                    review_cleaned = re.sub(r'[^a-zA-Z0-9()\[\]\{\}.,!?\' */\"]', "", reviews.text)
                    local_reviews_list.append(review_cleaned)

    return local_reviews_list

def data_not_found(driver,item):

    book_title = (driver.find_element_by_xpath("//div[contains(@data-widget,'productList')]/li["+str(item)+"]//h3[contains(@class,'heading')]")).text
    try:
        book_subtitle = (driver.find_element_by_xpath("//div[contains(@data-widget,'productList')]/li["+str(item)+"]//li[contains(@class,'subtitle')]")).text
        # print(book_subtitle)
    except:
        book_subtitle = ""
    book_author = (driver.find_element_by_xpath("//div[contains(@data-widget,'productList')]/li["+str(item)+"]//li[contains(@class,'authorLabel')]//a")).text
    try:
        book_narrator = (driver.find_element_by_xpath("//div[contains(@data-widget,'productList')]/li["+str(item)+"]//li[contains(@class,'narratorLabel')]//a")).text
    except:
        book_narrator = ""
    audio_runtime = (driver.find_element_by_xpath("//div[contains(@data-widget,'productList')]/li["+str(item)+"]//li[contains(@class,'runtimeLabel')]")).text
    audiobook_type = ""
    categories = ""
    try:
        rating = (driver.find_element_by_xpath("//div[contains(@data-widget,'productList')]/li["+str(item)+"]//li[contains(@class,'ratingsLabel')]/span[1]")).text
    except:
        rating = ""
    try:
        total_ratings = (driver.find_element_by_xpath("//div[contains(@data-widget,'productList')]/li["+str(item)+"]//li[contains(@class,'ratingsLabel')]/span[1]")).text
        ratings_cleaned = re.sub(r'[^0-9]', "", total_ratings)
    except:
        # total_ratings = ""
        ratings_cleaned = ""
    book_price = (driver.find_element_by_xpath("//div[contains(@data-widget,'productList')]/li["+str(item)+"]//div[contains(@class,'BuyBox')]/p[1]")).text
    p_audio_runtime, p_book_price = adh.data_preprocessing(audio_runtime, book_price)
    book_data_list = [book_title, book_subtitle, book_author,book_narrator, p_audio_runtime,audiobook_type, categories, rating,ratings_cleaned,p_book_price]

    return book_data_list




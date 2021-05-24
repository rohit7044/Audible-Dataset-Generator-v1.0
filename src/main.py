
import audible_webpage_automation as awa
import audible_data_handling as adh
audible_homepage_link ="https://www.audible.com/?ipRedirectOverride=true&ipRedirectOverride=true&overrideBaseCountry=true&overrideBaseCountry=true&pf_rd_p=ba485dc1-f49f-438a-92e0-9e8cdea09e44&pf_rd_r=G8BYTK5GMVH44V8TKQXX"
audible_all_categories_relevance_link = "https://www.audible.com/search?pf_rd_p=adc4b13b-d074-4e1c-ac46-9f54aa53072b&pf_rd_r=TN0P1XGXWHR4Z9M9S601"
# audible_newest_arrival_link = "https://www.audible.com/search?ref=a_search_c1_sort_1&pf_rd_p=073d8370-97e5-4b7b-be04-aa06cf22d7dd&pf_rd_r=1AYWGVRJD26KWNP37H76&feature_twelve_browse-bin=18685552011&sort=pubdate-desc-rank"
# audible_best_selling_link = "https://www.audible.com/search?ref=a_search_c1_sort_2&pf_rd_p=073d8370-97e5-4b7b-be04-aa06cf22d7dd&pf_rd_r=0WKA3V9SSRYH00AKFF8R&feature_twelve_browse-bin=18685552011&sort=popularity-rank"
# audible_title_link = "https://www.audible.com/search?ref=a_search_c1_sort_3&pf_rd_p=073d8370-97e5-4b7b-be04-aa06cf22d7dd&pf_rd_r=DV72G2TA9M3XFP6P3G2R&feature_twelve_browse-bin=18685552011&sort=title-asc-rank"
# audible_running_time_link = "https://www.audible.com/search?ref=a_search_c1_sort_4&pf_rd_p=073d8370-97e5-4b7b-be04-aa06cf22d7dd&pf_rd_r=9YTAR14SS1BX2XQKRRSB&feature_twelve_browse-bin=18685552011&sort=runtime-asc-rank"
# audible_average_customer_review_link = "https://www.audible.com/search?ref=a_search_c1_sort_5&pf_rd_p=073d8370-97e5-4b7b-be04-aa06cf22d7dd&pf_rd_r=QYD3QJP9Y5NZ1G6K6HEM&feature_twelve_browse-bin=18685552011&sort=review-rank"
# audible_bestseller_link = "https://www.audible.com/adblbestsellers?pf_rd_p=adc4b13b-d074-4e1c-ac46-9f54aa53072b&pf_rd_r=DFQ47PHR9RF53WFQ7J8D"
showmore_open_times = 10
if __name__ == "__main__":
   awa.audible_homepage_open(audible_homepage_link,audible_all_categories_relevance_link,showmore_open_times)

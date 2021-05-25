
import csv
import os
import re
final_data_list = []
book_data_list = []
final_reviews_list = []
book_data_columns = ["Book Title","Book Subtitle","Book Author", "Book Narrator", "Audio Runtime", "Audiobook_Type", "Categories" , "Rating", "Price"]
book_review_columns = []
total_review_count =""
final_column_data =[]

def data_preprocessing(length,price):
    length_sub = length
    n_length = re.sub('Length: ', '', length_sub)
    price_sub = price
    if "Pre" in price_sub:
        n_price = re.sub('Pre-order for ', '', price_sub)
    if "Reg" in price_sub:
        n_price = re.sub('Regular price: ', '', price_sub)
    if "Buy" in price_sub:
        price_sub = price
        n_price = re.sub('Buy for ', '', price_sub)
    return(n_length,n_price)
def write_to_csv(book_data_list,final_reviews_list):
    global final_data_list
    final_data_list = book_data_list + final_reviews_list
    csv_file_path = "output_encoded.csv"

    try:
        if os.path.exists(csv_file_path):
            if os.path.getsize(csv_file_path) is 0:
                csv_file = open(csv_file_path, "w", encoding="utf-8",newline ="")
                writer = csv.writer(csv_file, delimiter = ",")
                
                writer.writerow(final_column_data)
                writer.writerow(final_data_list)          
            else:
                csv_file = open(csv_file_path, "a", encoding="utf-8", newline="")
                writer = csv.writer(csv_file, delimiter=",")
                writer.writerow(final_data_list)

        else:
            csv_file = open(csv_file_path, "w", encoding="utf-8", newline="")
            writer = csv.writer(csv_file, delimiter=",")
            writer.writerow(final_column_data)
            writer.writerow(final_data_list)

        csv_file.close()
    except Exception as e:
        print(e)
    # try:
    #     if os.path.exists(txt_file_path):
    #         if os.path.getsize(txt_file_path) is 0:
    #             txt_file = open(txt_file_path, "w", encoding=None)
    #
    #             for data in range(len(final_column_data)):
    #                 txt_file.write(final_column_data[data]+",")
    #                 if data == len(final_column_data) - 1:
    #                     txt_file.write("\n")
    #             for data in range(len(final_data_list)):
    #                 temp = "\""+final_data_list[data]+"\""+","
    #                 txt_file.write("\""+final_data_list[data]+"\""+",")
    #                 if data == len(final_data_list) - 1:
    #                     txt_file.write("\n")
    #         else:
    #             txt_file = open(txt_file_path, "a", encoding=None)
    #
    #             for data in range(len(final_data_list)):
    #                 temp = "\"" + final_data_list[data] + "\"" + ","
    #                 txt_file.write("\"" + final_data_list[data] + "\"" + ",")
    #                 if data == len(final_data_list) - 1:
    #                     txt_file.write("\n")
    #     else:
    #         txt_file = open(txt_file_path, "w", encoding=None)
    #
    #         for data in range(len(final_column_data)):
    #             txt_file.write(final_column_data[data] + ",")
    #             if data == len(final_column_data) - 1:
    #                 txt_file.write("\n")
    #         for data in range(len(final_data_list)):
    #             temp = "\"" + final_data_list[data] + "\"" + ","
    #             txt_file.write("\"" + final_data_list[data] + "\"" + ",")
    #             if data == len(final_data_list) - 1:
    #                 txt_file.write("\n")
    #     txt_file.close()
    # except Exception as e:
    #     print(e)

    return
def review_column_creator(review_list):
    global final_column_data
    if len(final_column_data) == 0:
        book_review_columns = []
        total_review_counts = review_list
        for item in range(1,total_review_counts):
            book_review_columns.append("Review "+str(item))
            if item == total_review_counts - 1:
                book_review_columns.append("Review"+str(item+1))
        final_column_data = book_data_columns + book_review_columns
    return


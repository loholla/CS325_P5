from bs4 import BeautifulSoup
import os
#from module_3 import summary

# This module takes in a variable which says how many articles are in the "Data/raw" directory. It will then open the first of those files, named article_1_raw.txt, and
# store all of its HTML data in the variable rawData. It will then close the file and open a new file called article_1.txt, and in article_1.txt it will put in the
# processed text, which is when the raw data has all of the HTML tags removed and all of the whitespace stripped. Then it closes article_1.txt and moves on to the next
# file until it has processed all of the files in the "Data/raw" directory. It also stores all of these processed files into the "Data/processed" directory.

def process(articleNum):
    num = 1
    rawDirectory = "Data/raw" # Directory for RAW data
    p_Directory = "Data/processed" # Directory for processed data
    while(num < articleNum): # While the number is less than the number of articles
        rawArticleName = "article_" + str(num) + "_raw.txt" # The raw file names
        p_articleName = "article_" + str(num) + "_full.txt" # The processed file names
        rawPath = os.path.join(rawDirectory, rawArticleName) # The raw file path
        p_Path = os.path.join(p_Directory, p_articleName) # The processed file path
        article = open(rawPath, "r", encoding="utf-8") # Opens the raw file to read
        rawData = article.read() # Reads the raw file
        rawData = BeautifulSoup(rawData, "html.parser") # Parses the raw file
        article.close() # Closes the raw file
        article = open(p_Path, "w", encoding="utf-8") # opens the blank file, for the processed data
        elements = rawData.find_all("p", class_="paragraph inline-placeholder") # Files the <p> tag with the classes "paragraph" and "inline-placeholder"
        for element in elements:
            text = element.text.strip() + "\n" # Puts in one of the lines of the file, and adds a newline tag to make it look nice
            article.write(text) # Writes the data into the new file
        article.close() # Closes the new file, meaning all of the processed data should be in there
        #summary.summary(num)
        num += 1 # Increases num by 1
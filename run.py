import sys
from module_1 import raw_data_collector
from module_2 import processor
from module_4 import text_to_html

num = 1
num = raw_data_collector.rdc(sys.argv)
processor.process(num)

iterator = 1
while iterator < num:
    articleName = "article_" + str(iterator) + ".txt"
    htmlFile = "article_" + str(iterator) + ".html"
    text_to_html.txt_to_html(articleName,htmlFile)
    iterator+=1
#01_how_to_get_data_from_url

import urllib.request

url_to_catch="https://www.jkforum.net/forum-141-1.html"
path_to_save="D:/Google Sync/同步用資料夾/程式語言/Python/Crawer_Practice/"
file_name1="catched_1.html"
file_name2="catched_2.html"


"""

"""
#方法一

file=urllib.request.urlopen(url_to_catch)
data=file.read()

print(data)

fhandle=open(path_to_save+file_name1,"wb") # wb means "write in binary"
fhandle.write(data)
fhandle.close()


print(file.getcode()) #get success code 200
print(file.info())    #get info
print(file.geturl())  #get current url



#方法二
filename=urllib.request.urlretrieve(url_to_catch,filename=path_to_save+file_name2)
urllib.request.urlcleanup()



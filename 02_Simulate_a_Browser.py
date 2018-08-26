#02_Simulate_a_Browser

import urllib.request

url="http://blog.csdn.net/weiwei_pig/article/details/51178226"
header=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0")
#url_to_catch="http://blog.csdn.net/weiwei_pig/article/details/51178226" // URL that book say fail


path_to_save="D:/Google Sync/同步用資料夾/程式語言/Python/Crawer_Practice/"
file_name1="catched_1.html"
file_name2="catched_2.html"
file_name3="catched_3.html"


"""
"""

#方法一 用build_opener()修改header

opener=urllib.request.build_opener()
opener.addheaders = [header]
data=opener.open(url).read()
fhandle=open(path_to_save+file_name3,"wb") # wb means "write in binary"
fhandle.write(data)
fhandle.close()




"""
#方法二 用add_header()添加header

req=urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0')
data=urllib.request.urlopen(req).read()

# 好像不能用

"""
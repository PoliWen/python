#for循环遍历
list1=['aaa','bbb','ccc','ddd']
for i in list1:
	if i!='aaa':
	   print(i)
	   break
	print(i)
else:
	print('没有循环数据')	#如果没有找到循环项就走else语句
print('完成循环！')
for i in range(len(list1)):
	print(i,list1[i])#利用此方法可以输出一个列表的序列号和序列对应的值
print('python 其实是挺好玩的呀，不浪费一丁点字符，不多写一个符号，人生苦短，我学python')
print('commit把自己的项目托管到git上面去')

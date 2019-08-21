try:
	print(x)
except:
	print('x is not defined')
#学习要攻坚克难，当你觉得难的时候，麻烦的时候，你就要给自己的洗脑了
y = '错误异常处理'
try:
	print(y)
except NameError:
	print('variable y is not defined')
except:
	print('Somethins else went wrong')
else:
	print('no error')
finally:
	print('the try except is finished!')


#用python输出一个日历
import calendar
yy = int(input('输入年'))
mm = int(input('输入月'))
print('*'*20)

#显示日历
print(calendar.month(yy,mm))
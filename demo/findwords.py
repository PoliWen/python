'''
@Author: kingw
@Date: 2020-03-13 10:16:34
@Description: file content
'''
#写一个查找单词的各个字母的code码相加等于100来证明谬误
def sum_of_words(words):
    sum=0
    for i in words:
        sum+=ord(i)-96
    return sum

def find_words():
    with open('./file/words_alpha.txt','r') as fs:
        result=[]
        i = 0
        for n in fs.readlines():
            i+=1
            if sum_of_words(n.strip())==100:
                #在这里进行验证，检测错误
                '''
                for w in n:
                    print(f'{w}:{ord(w)-96}')
                '''
                result.append(n)
        with open('./file/words_result.txt','w') as fs2:
            fs2.writelines(result)
            print(f'一共计算了{i}个单词')
            print(f'查找出了{len(result)}个符合条件的单词')
            fs2.close()
        fs.close()
def main():
    print(f"发现有空格计算结果是-86,{ord(' ')-96},xxxx")
    print('验证单词是否符合条件，以此来验证函数书写是否正确' + str(sum_of_words('abactinally')))
    find_words()
if __name__=="__main__":
    main()

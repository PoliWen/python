# 如何用python去反驳别人论点

'''
如果把字母 a 计为 1、b 计为 2、c 计为 3 …… z 计为 26，那么：

knowledge = 96
hardwork = 98
attitude = 100

所以结论是：

知识（knowledge）与勤奋（hardwork）固然都很重要；
但是，决定成败的却是态度（attitude）！

'''
# print(ord('a')) 97 - 96 = 1
# print(ord('z')) 122 - 96 = 26


def sum_of_word(word):
    sum = 0
    for w in word:
        sum += ord(w) - 96
    return sum


def run():
    with open('./file/words_alpha.txt', 'r') as f1:
        result = []
        i = 0
        for w in f1.readlines():
            i += 1
            if sum_of_word(w.strip()) == 100:  # 空字符串在任何时候都要注意,如果你不注意空字符串可能会给你带来灾难
                ''' pass  # debug函数
                for c in w:
                    print(c+'\t', ord(c)-96)  # 统计的结果出来个-86，是因为没有清除空格
                break
                pass '''  # pass这中间一段是用来调试bug的，要记住这个调试bug的思维
                result.append(w)
        with open('./file/result.txt', 'w') as f2:
            f2.writelines(result)
            print(f'一共统计了{i}个单词')
            print('统计的结果为！', len(result))
            f2.close()
        f1.close()
        


def main():
    run()


print('验证统计的结果abactinally', sum_of_word('abactinally'))

# 代码框架
if __name__ == '__main__':
    main()

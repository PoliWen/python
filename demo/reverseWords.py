def reverseWords(input):
    input = input.split(' ')
    reverseInput = input[-1::-1]
    output = ' '.join(reverseInput)
    return output
if __name__=="__main__":
    input = "python is so easy"
    rw = reverseWords(input)
    print(rw)


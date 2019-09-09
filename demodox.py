import docx
print(dir(docx))
# def get_docx(file_name):
#     doc = 
#     return doc

doc = docx.document('./rootdir/1.docx')
print(doc)  # 输出行数：1075
for d in doc[:5]:
    print(d) # 打印前5行

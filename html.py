import docx
def get_docx(file_name):
    d = docx.opendocx(file_name)
    doc = docx.getdocumenttext(d)
    return doc

doc = get_docx("./rootdir/1.docx")
print(doc)  # 输出行数：1075
for d in doc[:5]:
    print(d) # 打印前5行

import xlrd
from lxml import etree
from xml.dom.minidom import Document


def read_xls(path):
    data = xlrd.open_workbook(path)
    table = data.sheets()[0]
    ob_json = {}
    for i in range(table.nrows):
        ob_json[str(int(table.cell(i, 0).value))] = table.row_values(i)[1:]
        # c[table.cell(i,0).value] = table.row_values(i)[1:]
    return ob_json


def write_xlsx_to_xml(data, savename):
    # 创建dom文档
    doc = Document()
    # 创建根节点
    root = doc.createElement('root')
    # 创建student节点
    student = doc.createElement('citys')
    # 根节点插入dom树
    doc.appendChild(root)
    # 将student子节点加入根节点
    root.appendChild(student)
    # 加入注释
    comment = doc.createComment('\n城市信息\n')
    student.appendChild(comment)
    # 加入内容
    text_node = doc.createTextNode(str(data))
    student.appendChild(text_node)
    # 保存为xml文件
    with open(savename, 'wb') as f:
        # doc.writexml(f, addindent='  ', newl='\n', encoding='utf-8')
        f.write(doc.toprettyxml(encoding='utf-8'))


if __name__ == '__main__':
    filename = 'city.xls'
    a = read_xls(filename)
    write_xlsx_to_xml(a, filename.replace('xls', 'xml'))
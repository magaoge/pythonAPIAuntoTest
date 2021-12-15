# excel操作
from openpyxl import load_workbook

class LoadExcel:

    def __init__(self,filePath,sheetName):
        self.filePath = filePath
        self.sheetName = sheetName
        self.file_screem = load_workbook(self.filePath)
        self.sheet = self.file_screem[self.sheetName]
        # 获取表单所有行
        self.maxRow = self.sheet.max_row
        # 获取表单所有列
        self.maxColumn = self.sheet.max_column

    def get_header(self):
        head = []
        for i in range(1,self.maxColumn+1):
            head_value = self.sheet.cell(1,i).value
            head.append(head_value)
        return head
    
    def load_excel(self):
        head = LoadExcel.get_header(self)
        # 首先声明一个列表，用来承接所有的数据
        sheet_data = []
        # 声明一个字典，用来承接每一行每一列的对应值
        # 从head里取出来，每一列的列头信息
        # 从每一行中取出每一列的信息
        # 将每个列头于每一行的每一列的值，组合起来放入字典中
        for i in range(2,self.maxRow+1):
            row_data = {}
            for j in range(1,self.maxColumn+1):
                every_row_column_value = self.sheet.cell(i, j).value
                # 列表索引从0开始，j需要-1
                row_data[head[j-1]] = every_row_column_value
            sheet_data.append(row_data)
        return sheet_data

    def write_back(self,rowNum,value):
        self.sheet.cell(rowNum,self.maxColumn).value = value
        self.file_screem.save(self.filePath)


if __name__ == '__main__':
    filePath = "../test_data/apiTestData.xlsx"
    sheetName = "login"

    db = LoadExcel(filePath, sheetName)
    db.get_header()

    db.load_excel()

    # sheet_data = .loadExcel()
    # print(sheet_data)




# # 3.定位表单行列，python中直接从1开始索引定位
# res = sheet.cell(1,1).value
#
# # 数据回写，注意数据回写的时候要关闭Excel文件，不会报错，但是无法写入保存
# sheet.cell(1,5).value = "你好"
# # 必须要保存，不保存的话只是临时写入
# wb.save("../test_data/apiTestData.xlsx")
#
# res2 = sheet.cell(1,5).value
# print(res2)
#
# print(maxRow,maxRow)


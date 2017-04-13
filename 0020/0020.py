import xlrd
import re


def read_xls(path):
    data = xlrd.open_workbook(path)
    table = data.sheets()[0]
    data_dict = []
    for i in range(1, table.nrows):
        data_dict.append(table.row_values(i)[3])
        # c[table.cell(i,0).value] = table.row_values(i)[1:]
    return data_dict


def calculate_call_time(data):
    minutes = 0
    seconds = 0
    min_par = '(\d*?)分(\d*?)秒'
    sec_par = '(\d*?)秒'
    for time in data:
        if re.search(min_par, time):
            match = re.search(min_par, time)
            minutes += int(match.group(1))
            seconds += int(match.group(2))
        else:
            seconds += int(re.search(sec_par, time).group(1))
    print(minutes)
    print(seconds)
    calculate_sum(minutes, seconds)


def calculate_sum(minutes, seconds):
    hours = 0
    minutes += seconds / 60
    seconds = seconds % 60
    hours += minutes / 60
    minutes = minutes % 60
    print('本月通话时间为：%d小时%d分钟%d秒' % (hours, minutes, seconds))


if __name__ == '__main__':
    calculate_call_time(read_xls('test.xls'))
import math
import random
import xlsxwriter


def uunifast(n, u):  # n = number of task, u = utilization
    sum_u = u
    tasks = []
    for i in range(n - 1):
        nextSum_u = sum_u * math.pow(random.uniform(0, 1), 1 / (n - 1))
        tasks.append(sum_u - nextSum_u)
        sum_u = nextSum_u
    tasks.append(sum_u)
    return tasks


def create_xls(tasks):
    workbook = xlsxwriter.Workbook('tasks.xlsx')
    worksheet = workbook.add_worksheet()
    row = 1
    worksheet.write(0, 0, 'task')
    worksheet.write(0, 1, 'utilization')
    # iterating through content list
    for i in range(len(tasks) ):
        # write operation perform
        worksheet.write(row, 0, 'task' + str(i))
        worksheet.write(row, 1, tasks[i])
        row += 1

    workbook.close()


if __name__ == "__main__":
    while 1:
        try:
            n = int(input("enter number of task:"))
            u = int(input("enter total utilization:"))
            break
        except:
            print("invalid input")

    create_xls(uunifast(n, u))

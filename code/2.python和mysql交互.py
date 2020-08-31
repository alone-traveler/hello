import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root',
                       password='', database='jing_dong', charset='utf8'
                       )

#  创建游标，也就是执行器
cursor = conn.cursor()

# sql = "insert into goods values(0,'123 456','123','华硕','3000',default,default); "
sql = "select * from goods"

ret = cursor.execute(sql)

# print(ret)
#  for循环遍历，一条一条输出结果信息
# for i in range(ret):
#     print(cursor.fetchone())
#  把所有查询结果都放在同一个元组中
print(cursor.fetchall())
#  确认执行操作
conn.commit()

#  关闭游标
cursor.close()
#  关闭连接对象
conn.close()

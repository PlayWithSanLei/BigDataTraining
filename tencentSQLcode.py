import pymysql
import pandas as pd
conn=pymysql.connect(host = '127.0.0.1' # 连接名称，默认127.0.0.1
                    ,user = 'root' # 用户名
                    ,passwd='111111' # 密码
                    ,port= 3306 # 端口，默认为3306
                    ,db='qiye' # 数据库名称
                    ,charset='utf8' # 字符编码
                    )
cur = conn.cursor() # 生成游标对象
sql1="select * from `qiye` " # SQL语句
cur.execute(sql1) # 执行SQL语句
	data = cur.fetchall() # 通过fetchall方法获得数据
for i in data[:2]: # 打印输出前2条数据
    print(i)
    print(type(i))
def get_df_from_db_1(sql):
    return pd.read_sql(sql,conn)
dat1=get_df_from_db_1(sql1)
print(dat1)
cur.close() # 关闭游标
conn.close() # 关闭连接

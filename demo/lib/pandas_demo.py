import pandas as pd
import numpy as np

print('type(None): {}'.format(type(None)))
print('type(np.NAN): {}'.format(type(np.NAN)))

# 初始化数组
s = pd.Series(list('Hello'))
s[0] = None
s[1] = np.NAN
print('pd.Series([None, np.NAN, 0, 1, 2]).isnull():\n{}'.format(pd.Series([None, np.NAN, 0, 1, 2]).isnull()))
print('pd.Series([None, np.NAN, 0, 1, 2]).notnull():\n{}'.format(pd.Series([None, np.NAN, 0, 1, 2]).notnull()))
# 删除为空的元素
print('pd.Series([None, np.NAN, 0, 1, 2]).dropna():\n{}'.format(pd.Series([None, np.NAN, 0, 1, 2]).dropna()))

# Data Frame
df = pd.DataFrame([
    [np.nan, 2, np.nan, 0],
    [3, 4, np.nan, 1],
    [np.nan, np.nan, np.nan, 5],
    [np.nan, 3, np.nan, 4],
    [np.nan, np.nan, np.nan, 4],
    [np.nan, np.nan, np.nan, 4]],
    columns=list('ABCD'))

#  删除有空元素的行
print('删除有空元素的行：pd.DataFrame().dropna():\n{}'.format(df.dropna()))
# 删除所有元素都为空的行
print('删除所有元素都为空的行： pd.DataFrame().dropna(how=\'all\'):\n{}'.format(df.dropna(how='all')))

#  inplace=True 替换原数组
print('所有空元素替换为0：pd.DataFrame().fillna(0):\n{}'.format(df.fillna(0)))
print(" 中位数:\n{}".format(df.fillna(0).median()))
print('每一列的中位数填充：pd.DataFrame().fillna(df.median()):\n{}'.format(df.fillna(df.fillna(0).median())))

print('用上一行的数据替换下一行的空数据， limit 限制上下行数：pd.DataFrame().fillna(method=\'ffill\'):\n{}'.format(
    df.fillna(method='ffill', limit=1)))
print('替换指定列的值为对应值：\n:{}'.format(df.fillna(value={'A': 0, 'B': 1, 'C': 2, 'D': 3})))

df.fillna(0, inplace=True)
print('在原数组上进行替换：pd.DataFrame().fillna(0, inplace=True):\n{}'.format(df))

# 删除重复行
print('判断行是不是和上一行重复：df.duplicated(): \n{}'.format(df.duplicated()))
print('删除重复的行：df.drop_duplicates(): \n{}'.format(df.drop_duplicates()))

# 数据
df = pd.DataFrame(np.random.randn(100, 2), columns=['A', 'B'])
print('数据：\n{}'.format(df))
print('简单数据分析，基于列：\n {}'.format(df.describe()))

print('第二列绝对值大于2的行:\n{}'.format(df['A'][np.abs(df['A']) > 2]))
print('任意一列有数据绝对值大于2的行:\n{}'.format(df[(np.abs(df) > 2).any(1)]))
print('第一列排序：\n{}'.format(df.sort_values(by=['A'], ascending=False)))
# 数据替换n


df = pd.DataFrame([
    [1, 2, -999],
    [-1000, 999, -999],
    [8, 999, -999]
])
print('df.replace(-999, np.nan):\n{}'.format(df.replace(-999, np.nan)))
print('df.replace([-999, -1000], np.nan):\n{}'.format(df.replace([-999, -1000], np.nan)))
print('df.replace([[-999, np.nan], [-1000, None]]):\n{}'.format(df.replace([[-999, np.nan], [-1000, None]])))
print('df.replace(-999: np.nan, -1000: None\):\n{}'.format(df.replace({-999: np.nan, -1000: None})))

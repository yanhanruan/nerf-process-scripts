import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Read the CSV file
data = pd.read_csv('./csv/rice ear.CSV')

# Convert columns to NumPy arrays
x = np.array(data['Column1'])
y = np.array(data['Column2'])

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决坐标轴负号显示问题

# 计算相关系数
correlation_coefficient = np.corrcoef(x, y)[0, 1]

# 进行线性拟合
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
line = slope * x + intercept  # 线性拟合函数

# 绘制散点图和拟合直线
plt.figure(figsize=(8, 6))
plt.scatter(x, y, label='数据点')  # 散点图

if intercept >= 0:
    label = f'拟合线: y = {slope:.3f}x + {intercept:.3f}'
else:
    label = f'拟合线: y = {slope:.3f}x - {abs(intercept):.3f}'

plt.plot(x, line, color='red', label=label)  # 拟合直线

# 添加标题和轴标签
# plt.title('水稻株高提取精度分析')
plt.xlabel('实验实测株高/cm')
plt.ylabel('点云提取株高/cm')

# 计算 R²
r_squared = correlation_coefficient ** 2

# 显示 R²
plt.text(0.05, 0.95, f'$R^2 = {r_squared:.3f}$', 
         transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')

# 图例调整至右下角
plt.legend(loc='lower right')

# 删除网格线
plt.grid(False)

# 显示图表
plt.show()

# 输出相关系数和线性回归结果
print(f'Correlation Coefficient: {correlation_coefficient:.3f}')
print(f'Linear Fit: y = {slope:.2f}x + {intercept:.3f}')

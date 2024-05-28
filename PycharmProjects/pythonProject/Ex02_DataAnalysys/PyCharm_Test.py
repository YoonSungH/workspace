import matplotlib.pyplot as plt
import pandas as pd

from matplotlib import font_manager, rc
font_path = "C:\\Windows\\Fonts\\gulim.ttc"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

data = pd.read_csv('연도별_고용률_통계표.csv', encoding='cp949')

print(data)


# print(f'{"1번 문제":=^20}')
# data = data[['2022', '2023']]
# print(data[['2022', '2023']].iloc[0].values)
#
# select_data = data[['2022', '2023']].iloc[0].values
# print(select_data)
#
# year = ['2022','2023']
# plt.bar(year,select_data)
#
# for i in range(len(year)):
#     plt.text(year[i], select_data[i], str(select_data[i]), ha='center', va='bottom')
#
# plt.title('2022년,2023년 각각 고용률')
# plt.xlabel('연도')
# plt.ylabel('고용률')
# plt.rc(font)
# plt.show()

# print("======================================")
# print(f'{"2번 문제":=^20}')
#
# data1 = data[['2023']]
# select_data = data1[['2023']].iloc[3:]
# group = ['15~19세', '20~29세', '30~39세', '40~49세', '50~59세', '60세 이상']
#
# datalist = select_data['2023'].tolist()
# print(select_data)
#
#
# plt.figure(figsize=(8, 8))
# plt.pie(datalist,labels=group, autopct='%1.1f%%', startangle=140)
# plt.title('2023년 나이별 고용비율')
# plt.axis('equal')
# plt.rc(font)
# plt.show()

print("======================================")
print(f'{"3번 문제":=^20}')

year = data.columns[1:]
data = data.iloc[0,1:]
print(year,data)

plt.plot(year,data,color='blue')
plt.title('연도별 고용률')
plt.xlabel('연도')
plt.ylabel('고용률(%)')
plt.grid(True)
plt.rc(font)
plt.show()


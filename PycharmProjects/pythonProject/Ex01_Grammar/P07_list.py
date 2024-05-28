def pArr(arr):
  for i in range(0, len(arr), 1):
    for j in range(0, len(arr[i]), 1):
      print(arr[i][j], end=" ")
    print(end="\n")

# 1. list
l = list();
l.append(1);  # 끝에 추가
l.insert(3, 2);  # 원하는 곳에 추가
l.extend([3, 4, 5])  # list를 추가
l = l + [6, 7]
del l[len(l) - 1];
print(l)  # 마지막 인덱스를 지움
del l[l.index(6)];
print(l)  # index(원소) 해당 원소가 있는 위치를 인덱스로 반환
l.remove(5)  # 4라는 원소를 찾아서 지움
print(l, id(l))  # 연산자로 더하기

l = [5, 6, 7];
print(l, id(l))
l.clear()  # 모두 삭제
for i in range(0, 10, 1):
  l.append(i)
print(l);
print(l[0]);
print(l[0:3])
l.append("hello")
l.append(True)
l.append(12.34)
lcopy = l.copy()  # 새로운 주소의 리스트를 생성, 주소가 다름
print(lcopy, id(lcopy))

lists = [
  ["이길동", 95, 85, 100],
  ["홍길동", 85, 95, 100],
  ["박길동", 100, 95, 85]
]
print(lists, type(lists))
print(lists[1], lists[0][0])

# 새로운 리스트 생성
lists2 = [[0 for j in range(len(lists[0])+1)] for i in range(len(lists))]
pArr(lists2)
print(">>", len(lists2), len(lists2[0]))

for i in range(0, len(lists)):
  for j in range(0, len(lists[i]), 1):
    lists2[i][j] = lists[i][j]
    if j!= 0:
      lists2[i][len(lists[0])] += lists[i][j]
  print(end="\n")

print("{0:=^20}".format('결과'))
pArr(lists2)

lists3 = list()
for i in range(0, len(lists)):
    tmpList = list()
    for j in range(0, len(lists[i]), 1):
        tmpList.append(lists[i][j]); tmpList.append(lists[i][j])
        if j>1: tmpList.append(lists[i][j-1] + lists[i][j])
        lists3.append(tmpList)

print("{0:=^20}".format('결과'))
pArr(lists2)

# 성호씨 코드
for i in range(0, len(lists), 1):
    total = lists[i][1] + lists[i][2] + lists[i][3]
    lists3 = list()
    for j in range(0, len(lists[i]), 1):
        lists3.append(lists[i][j])
    lists3.append(total)

    print(lists3, end='\n')

listStr = ["Life", "is", "Good", "and", "Happy"]
print(listStr)
listStr.reverse(); print(listStr)
print(listStr.index("Good"))
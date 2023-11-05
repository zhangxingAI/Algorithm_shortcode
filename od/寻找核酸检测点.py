'''
题目描述

张三要去外地出差，需要做核酸，需要在指定时间点前做完核酸，请帮他找到满足条件的核酸检测Q点。
1.给出一组核酸检测点的距离和每个核酸检测点当前的人数。
2.给出张三当前要去做核酸的出发时间，出发时间是10分钟的倍数，同时给出张三做核酸的最晚结束时间。
3. 题目中给出的距离是整数，单位是公里，时间1分钟为一基本单位。

去找核酸点时，有如下的限制：
1. 去往核酸点的路上，每公里距离花费时间10分钟，费用是10元。
2. 核酸点每检查一个人的时间花费是1分钟。
3.每个核酸点工作时间都是8点到20点（中间不休息）。核酸点准时工作，早到晚到都不检测。
4. 核酸检测结果可立刻知道。
5.在张三去某个核酸点的路上花费的时间内，此核酸检测点的人数是动态变化的，变化的规则是：
5.1 在非核酸检测时间内，没有人排队。
5.2 8点-10点每分钟增加3人。
5.3 12点-14点每分钟增加10人。



要求将所有满足条件的核酸检测点按照优选规则排序列出：

优选规则：
1. 花费时间最少的核酸检测点排在前面。
2. 花费时间一样，花费费用最少的核酸检测点排在前面。
3. 时间和费用一样，则ID值最小的排在前面。

输入描述

H1 M1
H2 M2
N
ID1 D1C1
ID2 D2 C2
⋯
IDn Dn Cn

H1：当前时间Q的小时数。
M1：当前时间的分钟数。
H2：指定完成核酸时间的小时数。
M2：指定完成核酸时间的分钟数。
N：所有的核酸检测点个数。
ID1：核酸点的ID值。
D1：核酸检测点距离张三的距离。
C1：核酸检测点当前检测的人数。

输出描述

N
12 T2 M2
13 T3 M3
N：满足要求的核酸检测点个数。
12：选择后的核酸点ID值。
T2：做完核素花费的总共时间（分钟）。
M3：去改核酸点花费的费用。

input
10 30
14 50
3
1 10 19
2 8 20
3 21 3

output
2
2 80 80
1 190 100

'''
def parse_input(input_string):
    return list(map(int, input_string.split()))

def cal_time_in_min(time_info):
    return time_info[0]*60+time_info[1]
def calculate_time(start, point_info, distance):
    time = distance
    remaining_queue = max(0, point_info[2] - distance)
    arrive_time = start + distance

    if arrive_time <= first_stage_start:
        return first_stage_start-start
    elif arrive_time <= first_stage_end:
        remaining_queue += (arrive_time - first_stage_start)*3-(arrive_time-first_stage_start)
    elif arrive_time <= sec_stage_start:
        pass
    elif arrive_time <= sec_stage_end:
        remaining_queue += (arrive_time - sec_stage_start)*10-(arrive_time-sec_stage_start)
    return time + remaining_queue

def sort_point(points):
    points.sort(key = lambda x: (x[4], x[3]))

def filter_valid_points(start, end, points):
    valid_points = []
    for point in points:
        arrival_time = start+point[4]
        if arrival_time < end:
            valid_points.append(point)
    return valid_points


first_stage_start = 480
first_stage_end = 600
sec_stage_start = 720
sec_stage_end = 840

start_time_info = parse_input((input()))
start = cal_time_in_min(start_time_info)

end_time_info = parse_input(input())
end = cal_time_in_min(end_time_info)

number_of_points = int(input())

points = []
for _ in range(number_of_points):
    point_info = parse_input(input())
    distance = point_info[1]*10
    time = calculate_time(start, point_info, distance)
    point_info.extend([distance, time])
    points.append(point_info)

sort_point(points)
valid_points = filter_valid_points(start, end, points)
print(len(valid_points))
for point in valid_points:
    print(point[0], point[4], point[3])



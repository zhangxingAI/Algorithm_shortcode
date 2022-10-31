import pandas as pd
'''
输出字典，方便后处理
interval数据结构:（TSS_start，TSS_stop, id）, point数据结构:(position, cellbarcode)
'''
def search(interval, point):
    interval_dict, point_dict, pick_dict = dict(), dict(), dict()
    num = []
    interval['id'] = interval['TSS_start'].astype('str') + '_' + interval['TSS_stop'].astype('str')
    for k1, k2, k3 in zip(interval['TSS_start'], interval['TSS_stop'], interval['id']):
        interval_dict[(k1, k2)] = k3
    for k1, k2 in zip(point['position'], point['cellBarcode']):
        if k1 not in point_dict:
            point_dict[k1] = []
        point_dict[k1].append(k2)
    for k1, v1 in interval_dict.items():
        ls = []
        for k2, v2 in point_dict.items():
            if k2>= k1[0] and k2<= k1[1]:
                ls = ls + v2
        pick_dict[v1] = ls
    return pick_dict
'''
数据前处理
'''
def datafilter(url1,url2,gen_id):
    interval = pd.read_csv(url1, low_memory=False)
    point = pd.read_csv(url2)
    interval = interval[interval['gene_id']==gen_id]
    return interval, point
'''
输出df
'''
def dfoutput(dict):
    df = pd.DataFrame(dict.items(), columns=['interval', 'cellBarcode'])
    df['num'] = [len(x) for x in df['cellBarcode']]
    return df
'''
主函数
'''
if __name__ == '__main__':
    url1 = './ref_TSS_region.csv'
    url2 = './point.csv'
    gen_id = 'ENSG00000160072'
    interval, point = datafilter(url1, url2, gen_id)
    dict = search(interval, point)
    df = dfoutput(dict)
    print(df)




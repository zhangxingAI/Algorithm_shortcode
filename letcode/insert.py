import pandas as pd
'''
输出字典，方便后处理
interval数据结构:（TSS_start，TSS_stop, id）, point数据结构:(position, cellbarcode)
'''
def search(interval, point):
    interval_dict, point_dict, pick_dict = dict(), dict(), dict()
    interval['id'] = interval['TSS_start'].astype('str') + '_' + interval['TSS_stop'].astype('str')
    for TSS_start, TSS_stop, id in zip(interval['TSS_start'], interval['TSS_stop'], interval['id']):
        interval_dict[(TSS_start, TSS_stop)] = id
    for position, cellBarcode in zip(point['position'], point['cellBarcode']):
        if position not in point_dict:
            point_dict[position] = []
        point_dict[position].append(cellBarcode)
    for TSS, id in interval_dict.items():
        ls = []
        for position, cellBarcode in point_dict.items():
            if position>= TSS[0] and position<= TSS[1]:
                ls = ls + cellBarcode
        pick_dict[id] = ls
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
    # print(dict)
    df = dfoutput(dict)
    print(df)




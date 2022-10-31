import pandas as pd
data = pd.read_csv('./ref_TSS_region.csv',low_memory=False)
data1 = pd.read_csv('./point.csv')
data = data[data['gene_id']=='ENSG00000160072']
data['id']=data['TSS_start'].astype('str')+'_'+data['TSS_stop'].astype('str')
id = data['id'].tolist()
start_stop = [(k,v) for k,v in zip(data['TSS_start'].tolist(),data['TSS_stop'])]
point = [(k,v) for k,v in zip(data1['position'].tolist(),data1['cellBarcode'])]
def search(target, point):
    inteval = dict()
    point_dict = dict()
    for k, v in target:
        inteval[k] = v
    num = []
    for i, j in inteval.items():
        ls = []
        for k, v in point:
            # print(j)
            if k>= i[0] and k<= i[1]:
                ls.append(v)
        point_dict[j] = ls
        num.append(len(ls))
        print(ls)
    df = pd.DataFrame(point_dict.items(), columns=['interval', 'cellBarcode'])
    df['num'] = num
    return df
df = search(zip(start_stop, id),point)
# print(df)




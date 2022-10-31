import pandas as pd
point = pd.read_csv('./point.csv')['0'].tolist()
data = pd.read_csv('./ref_TSS_region.csv',low_memory=False)
data = data[data['gene_id']=='ENSG00000160072']
data['id']=data['TSS_start'].astype('str')+'_'+data['TSS_stop'].astype('str')
id = data['id'].tolist()
start_stop = [(k,v) for k,v in zip(data['TSS_start'].tolist(),data['TSS_stop'])]

def search(target, point):
    inteval = dict()
    point_dict = dict()c
    for k, v in target:
        inteval[k] = v
    for p in point:
        for i, j in inteval.items():
            # print(j)
            if p>= i[0] and p<= i[1]:
                # print(v)
                point_dict[p] = j
    df = pd.DataFrame(point_dict.items(), columns=['value', 'interval'])
    return df

df = search(zip(start_stop, id),point)
print(df)




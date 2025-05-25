import json
import math
with open(f'../dataset/dataset_train.json', 'r', encoding='utf-8') as f:
    dataset_train = json.load(f)
with open(f'../dataset/dataset_test.json', 'r', encoding='utf-8') as f:
    dataset_test = json.load(f)

def normalize(dataset,type_dataset):
    f_count_5000 = 0
    accounts = []
    accounts_address=[]
    accounts_id = []
    count_c=0
    for account in dataset:
        a=[]
        sr_count_month=0
        max_count_month=0
        count=0
        if type_dataset=="train":
            if account["buildingType"] != 'Частный':continue
            # accounts_type.append(account["buildingType"])
        if type_dataset=="train":
            if account['address'] in accounts_address:continue
            if account['accountId'] in accounts_id: continue
            accounts_address.append(account['address'])
            accounts_id.append(account['accountId'])
        for month in range(1,13):
            if str(month) not in account["consumption"]:account["consumption"][str(month)]=0
            else:
                account["consumption"][str(month)]/= 100
            # if type_dataset=="train" and account["isCommercial"] and (account["consumption"][str(month)]<3):
            #     flag=True
            if account["consumption"][str(month)]>0:
                sr_count_month+=account["consumption"][str(month)]
                count+=1
            if max_count_month<account["consumption"][str(month)]:
                max_count_month=account["consumption"][str(month)]
            a.append(account["consumption"][str(month)]/10)
        # if flag:
        #     f_count_5000+=1
        #     continue
        # print(count,account["consumption"],max_count_month)
        if type_dataset=="train" and not account["isCommercial"] and max_count_month > 45:
            f_count_5000 += 1
            continue
        sr_count_month = sr_count_month / (count if count else 1)
        for month in range(1,12):
            razn=account["consumption"][str(month+1)]-account["consumption"][str(month)]
            a.append(razn)
        # for i in range(len(a)):
        #     a[i]=a[i]/max_count_month
        a.append(sr_count_month)
        a.append(count)
        # a.append(accounts_type.index(account["buildingType"]))
        a.append(account["roomsCount"] if "roomsCount" in account else 0)
        a.append(account["residentsCount"] if "residentsCount" in account else 0)
        a.append(account["totalArea"] if "totalArea" in account else 0)
        # if type_dataset == "train" and not account["isCommercial"] and max_count_month > 100:
        #     a.append(1)
        #     a.append(0)
        # else:
        a.append(int(account["isCommercial"]))
        a.append(int(not account["isCommercial"]))
        if account["isCommercial"]:
            count_c+=1
        accounts.append(a)
    with open(f'data_{type_dataset}_change.json', 'w', encoding='utf-8') as f:
        json.dump(accounts, f, ensure_ascii=False)
    print(count_c, len(dataset),count_c/len(accounts))

normalize(dataset_train,'train')
normalize(dataset_test,'test')





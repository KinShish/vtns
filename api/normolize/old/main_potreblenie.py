import json
max_roomsCount=0
max_residentsCount=0
max_totalArea=0
type_array=[]
cites=[]
with open(f'../../dataset/dataset_train.json', 'r', encoding='utf-8') as f:
    dataset_train = json.load(f)
with open(f'../../dataset/dataset_test.json', 'r', encoding='utf-8') as f:
    dataset_test = json.load(f)
def getAllParams(dataset):
    global max_roomsCount, max_residentsCount, max_totalArea
    for account in dataset:
        if account["buildingType"] not in type_array:
            type_array.append(account["buildingType"])
        address = account["address"].split(', ')
        if len(address) < 4: continue  # отсеиваем не полные адреса
        city_and_street = address[2] + "," + address[3]
        if city_and_street not in cites:
            cites.append(city_and_street)
        account["roomsCount"] = account["roomsCount"] if "roomsCount" in account else 0
        account["residentsCount"] = account["residentsCount"] if "residentsCount" in account else 0
        account["totalArea"] = account["totalArea"] if "totalArea" in account else 0
        if max_roomsCount < account["roomsCount"]:
            max_roomsCount = account["roomsCount"]
        if max_residentsCount < account["residentsCount"]:
            max_residentsCount = account["residentsCount"]
        if max_totalArea < account["totalArea"]:
            max_totalArea = account["totalArea"]
getAllParams(dataset_train)
getAllParams(dataset_test)
def normalize(dataset,type_dataset):
    accounts={
        "commercial":{
        },
        "noncommercial":{
        }
    }
    for type in type_array:
        accounts["commercial"][type]=[]
        accounts["noncommercial"][type] = []
    for account in dataset:
        address = account["address"].split(', ')
        if len(address) < 4: continue  # отсеиваем не полные адреса
        city_and_street = address[2] + "," + address[3]
        for month in account["consumption"]:
            if type_dataset=="train" and (account["consumption"][month]>15000 or account["consumption"][month]<1000):
                # print(account["consumption"][month])
                continue
            accounts["commercial" if account["isCommercial"] else "noncommercial"][account["buildingType"]].append([
                type_array.index(account["buildingType"])/len(type_array),
                cites.index(city_and_street)/len(cites),
                account["roomsCount"],
                account["residentsCount"],
                account["totalArea"],
                int(month)/12,
                account["consumption"][month]/5000
            ])
    for type in accounts["commercial"]:
        for account in accounts["commercial"][type]:
            account[2]=account[2]/max_roomsCount
            account[3]=account[3]/max_residentsCount
            account[4] = account[4] / max_totalArea
    for type in accounts["noncommercial"]:
        for account in accounts["noncommercial"][type]:
            account[2] = account[2]/ max_roomsCount
            account[3] = account[3]/ max_residentsCount
            account[4] = account[4] / max_totalArea
    # accounts["type"]=type
    # accounts["cites"]=cites

    with open(f'data_{type_dataset}.json', 'w', encoding='utf-8') as f:
        json.dump(accounts, f, ensure_ascii=False)
print(type_array)
normalize(dataset_train,'train')
normalize(dataset_test,'test')



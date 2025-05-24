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
    accounts=[]
    for account in dataset:
        # if account["buildingType"]!="Частный":continue
        address = account["address"].split(', ')
        if len(address) < 4: continue  # отсеиваем не полные адреса
        city_and_street = address[2] + "," + address[3]
        a=[
            # (type_array.index(account["buildingType"])+1) / (len(type_array)+1),
            (cites.index(city_and_street)+1) / (len(cites)+1),
            account["roomsCount"]+1,
            account["residentsCount"]+1,
            account["totalArea"]+1,
            int(account["isCommercial"])
        ]
        for i in range(12):
            if str(i) in account["consumption"]:
                a.append(account["consumption"][str(i)]/5000)
            else:
                a.append(0)
        accounts.append(a)
    for account in accounts:
        account[1]=account[1]/(max_roomsCount+1)
        account[2]=account[2]/(max_residentsCount+1)
        account[3] = account[3] /( max_totalArea+1)

    with open(f'data_{type_dataset}.json', 'w', encoding='utf-8') as f:
        json.dump(accounts, f, ensure_ascii=False)
print(type_array)
normalize(dataset_train,'train')
normalize(dataset_test,'test')



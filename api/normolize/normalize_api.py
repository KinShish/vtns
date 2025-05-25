def normalize(dataset):
    accounts = []
    for account in dataset:
        a=[]
        sr_count_month=0
        count=0
        for month in range(1,13):
            if str(month) not in account["consumption"]:account["consumption"][str(month)]=0
            else:
                account["consumption"][str(month)]/= 100
            if account["consumption"][str(month)]>0:
                sr_count_month+=account["consumption"][str(month)]
                count+=1
        sr_count_month = sr_count_month / (count if count else 1)
        for month in range(1,12):
            razn=account["consumption"][str(month+1)]-account["consumption"][str(month)]
            a.append(razn)
        a.append(sr_count_month)
        a.append(account["accountId"])
        a.append(int(account["isCommercial"]))
        a.append(int(not account["isCommercial"]))
        accounts.append(a)
    return accounts

def normalize_commerce(dataset):
    accounts = []
    for account in dataset:
        a=[]
        sr_count_month=0
        count=0
        for month in range(1,13):
            if str(month) not in account["consumption"]:account["consumption"][str(month)]=0
            else:
                account["consumption"][str(month)]/= 100
            if account["consumption"][str(month)]>0:
                sr_count_month+=account["consumption"][str(month)]
                count+=1
        sr_count_month = sr_count_month / (count if count else 1)
        for month in range(1,12):
            razn=account["consumption"][str(month+1)]-account["consumption"][str(month)]
            a.append(razn)
        a.append(sr_count_month)
        a.append(account["accountId"])
        accounts.append(a)
    return accounts





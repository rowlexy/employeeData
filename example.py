def filterLoads(shipments, **load_list):
    filtered_list = []
    for loads in shipments:
        match = True
        for key, value in load_list.items():
            if key == "month":
                if loads["ActivityDate"].split("-")[1] != value:
                    match == False
                    break
            elif loads.get(key) != value:
                match == False
                break
        if match:
            filtered_list.append(loads)
    return filtered_list

def regularFilter(shipments, load_num=None, month=None, pu_date=None, origin=None, status=None, consignee=None):
    loads_list = []
    for loads in shipments:
        if(load_num and loads["LoadNum"] != load_num):
            continue
        if(month and loads["ActivityDate"].split("-")[1] != month):
            continue
        if(pu_date and loads["ActivityDate"] != pu_date):
            continue
        if(origin and loads["Origin"] != origin):
            continue
        if(status and loads["Status"] != status):
            continue
        if(consignee and loads["Destination"] != consignee):
            continue
        loads_list.append(loads)
    return loads_list
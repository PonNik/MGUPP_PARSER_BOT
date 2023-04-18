

async def parse_Lessons(day):    
    itog = []
    for itr in day:
        if '1  П.Гр.' not in itr['name']:
            name = itr['name']
            data_start = itr['data-start']
            data_end= itr['data-end']
            audit = itr['_auditoria']
            data_type = itr['data-type']
            msg = f"({data_start}-{data_end})\n{name} {data_type}\n{audit}"
            itog.append(msg)
    return itog
  
import csv

def parse_csv(filename, select=[], types=[]):
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        if select:
            indices = [headers.index(item) for item in select]
            colInfo = list((zip(types,indices)))
        else:
            indices = []
            colInfo = []
        
        records = []
        for row in rows:
            if not row:
                continue
            if indices:
                row = [datatype(row[idx]) for datatype, idx in colInfo]
                d = dict(zip(select, row))
                records.append(d)
    return records





import csv

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    rhet = []

    file = open(csv_file_path)

    readFile = csv.reader(file)

    for row in readFile:
        newRow = []
        for val in row:
            if val.isdigit():
                newRow.append(int(val))
            else:
                newRow.append(val)
        rhet.append(newRow)
        
    return rhet

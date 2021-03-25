from VastData import VastData

data = VastData("readings.csv", "measures.csv")

rows_to_delete = []
for i in range(len(data.sample_id)):
    if data.sample_value[i] == 0:
        rows_to_delete.append(data.sample_id[i])
        
for sample_id in rows_to_delete:
    data.removeRowById(sample_id)
    
data.save("no_zeros.csv")
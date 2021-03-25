from VastData import VastData

data = VastData("readings.csv", "measures.csv")

measure_counts = []
for measure in data.measure_names:
    for location in data.sensor_location:
        measure_counts.append(0)
    
for measure in range(len(data.measure_names)):
    for location in range(len(data.sensor_location)):
        for i in range(len(data.sample_id)):
            if data.sample_measure[i] == data.measure_names[measure] and data.sample_location[i] == data.sensor_location[location]:
                measure_counts[measure * 10 + location] += 1

counts_file = open("measure_counts.csv", "w")

counts_file.write("Measure,Total,Achara,Boonsri,Busarakhan,Chai,Decha,Kannika,Kohsoom,Sadka,Somchair,Tansanee\n")
for measure in range(len(data.measure_names)):
    measure_total = 0
    for loc in range(len(data.sensor_location)):
        measure_total += measure_counts[measure * 10 + loc]
    
    counts_file.write("{measure},{total},{a},{b},{bu},{c},{d},{k},{ko},{s},{so},{t}\n".format(
            measure=data.measure_names[measure],total=measure_total, a=measure_counts[measure*10], 
            b=measure_counts[measure*10+1], bu=measure_counts[measure*10+2], c=measure_counts[measure*10+3], 
            d=measure_counts[measure*10+4], k=measure_counts[measure*10+5], ko=measure_counts[measure*10+6], 
            s=measure_counts[measure*10+7], so=measure_counts[measure*10+8], t=measure_counts[measure*10+9]))
counts_file.close()
from VastData import VastData

data = VastData("no_zeros.csv", "measures.csv")

rows_to_delete = []

consecutive_report = open("consecutive_report.csv", "w")
consecutive_report.write("Measure,Location,StartDate,EndDate,Value,Removed\n")

# Loops through all measures and locations
for measure in range(len(data.measure_names)):
    for location in range(len(data.sensor_location)):
        last_measure = 0
        consecutive_ids = []
        # Loops through each row in table
        for i in range(len(data.sample_id)):
            # Checks if the row is for the current measure and location
            if data.sample_measure[i] == data.measure_names[measure] and data.sample_location[i] == data.sensor_location[location]:
                # If the value of this row is the same as the last, add its id to list of consecutive ids
                if data.sample_value[i] == last_measure:
                    consecutive_ids.append(data.sample_id[i])
                else:
                    # Check if the consecutive_ids list is longer than 10 elements, if it is add the ids contained to rows to delete
                    if len(consecutive_ids) > 10:
                        # Generates CSV file that contains log for each group removed
                        consecutive_report.write("{q}{m}{q},{l},{s},{e},{v},{r}\n".format(
                                m=data.measure_names[measure], l=data.sample_location[location], 
                                s=data.sample_date[data.sample_id.index(consecutive_ids[0])].strftime("%d-%b-%y"), 
                                e=data.sample_date[data.sample_id.index(consecutive_ids[-1])].strftime("%d-%b-%y"),
                                v=last_measure, r=len(consecutive_ids), q=("\"" if "," in data.measure_names[measure] else "")))
                        for row in consecutive_ids:
                            rows_to_delete.append(row)
                    consecutive_ids = [data.sample_id[i]]
                last_measure = data.sample_value[i]
        
        # Need to check if consecutive ids list is longer than 10 after loop executes as well, otherwise consecutive 
        # values at the end will not be removed
        if len(consecutive_ids) > 10:
            consecutive_report.write("{q}{m}{q},{l},{s},{e},{v},{r}\n".format(
                    m=data.measure_names[measure], l=data.sample_location[location], 
                    s=data.sample_date[data.sample_id.index(consecutive_ids[0])].strftime("%d-%b-%y"), 
                    e=data.sample_date[data.sample_id.index(consecutive_ids[-1])].strftime("%d-%b-%y"),
                    v=last_measure, r=len(consecutive_ids), q=("\"" if "," in data.measure_names[measure] else "")))

            for row in consecutive_ids:
                rows_to_delete.append(row)

consecutive_report.close()

# Deletes all rows marked to be deleted above
for sample_id in rows_to_delete:
    data.removeRowById(sample_id)
    
# Saves remaining data to csv
data.save("no_consecutive.csv")
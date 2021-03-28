from VastData import VastData

data = VastData("no_consecutive.csv", "measures.csv")

year_differences = []
month_differences = []

overall_year_differences = []
overall_month_differences = []

for measure in range(len(data.measure_names)):
    for location in range(len(data.sensor_location)):
        
        year_averages = []
        month_averages = []
        curr_year = -1
        curr_month = -1
        
        year_total = 0.0
        year_measurements = 0
        month_total = 0.0
        month_measurements = 0
        
        
        for i in range(len(data.sample_id)):
            if data.sample_measure[i] == data.measure_names[measure] and data.sample_location[i] == data.sensor_location[location]:
                # In different month, update relevant variables
                if data.sample_date[i].month != curr_month:
                    if month_measurements > 0:
                        month_averages.append(month_total / month_measurements)
                        month_total = 0.0
                        month_measurements = 0
                    month_total = data.sample_value[i]
                    month_measurements = 1
                # Else, increase month total and measurements
                else:
                    month_measurements += 1
                    month_total += data.sample_value[i]
                # In different year, increase relevant variables
                if data.sample_date[i].year == curr_year:
                    if year_measurements > 0:
                        year_averages.append(year_total / year_measurements)
                        year_total = 0.0
                        year_measurements = 0
                    # If the year has changed, but the next measurement is in the same month as the last
                    if data.sample_date[i].month == curr_month and month_measurements > 0:
                        month_averages.append(month_total / month_measurements)
                        month_total = 0.0
                        month_measurements = 0
                    
                # Else, increase year total and measurements
                else:
                    year_measurements += 1
                    year_total += data.sample_value[i]
                    
                curr_year = data.sample_date[i].year
                curr_month = data.sample_date[i].month
        
        # Add last month and year averages
        if month_measurements != 0:
            month_averages.append(month_total / month_measurements)
            month_total = 0.0
            month_measurements = 0
        
        if year_measurements != 0:
            year_averages.append(year_total / year_measurements)
            year_total = 0.0
            year_measurements = 0
        
        # Add differences between first and last year / month to resepective lists
        if len(year_averages) > 0 and year_averages[0] != 0:
            year_differences.append((year_averages[-1] - year_averages[0]) / year_averages[0])
            month_differences.append((month_averages[-1] - month_averages[0]) / month_averages[0])
        else:
            year_differences.append(0)
            month_differences.append(0)
    
    overall_year_averages = []
    overall_month_averages = []
    overall_curr_month = -1
    overall_curr_year = -1
    
    overall_year_total = 0.0
    overall_year_measurements = 0
    overall_month_total = 0.0
    overall_month_measurements = 0
    # Loop for overall differences
    for i in range(len(data.sample_id)):
        if data.sample_measure[i] == data.measure_names[measure]:
            if data.sample_date[i].month != overall_curr_month:
                if overall_month_measurements > 0:
                    overall_month_averages.append(overall_month_total / overall_month_measurements)
                    overall_month_total = 0.0
                    overall_month_measurements = 0
                overall_month_total = data.sample_value[i]
                overall_month_measurements = 1
            # Else, increase month total and measurements
            else:
                overall_month_measurements += 1
                overall_month_total += data.sample_value[i]
            # In different year, increase relevant variables
            if data.sample_date[i].year == overall_curr_year:
                if overall_year_measurements > 0:
                    overall_year_averages.append(overall_year_total / overall_year_measurements)
                    overall_year_total = 0.0
                    overall_year_measurements = 0
                # If the year has changed, but the next measurement is in the same month as the last
                if data.sample_date[i].month == overall_curr_month and overall_month_measurements > 0:
                    overall_month_averages.append(overall_month_total / overall_month_measurements)
                    overall_month_total = 0.0
                    overall_month_measurements = 0
                    
            # Else, increase year total and measurements
            else:
                overall_year_measurements += 1
                overall_year_total += data.sample_value[i]
                    
            overall_curr_year = data.sample_date[i].year
            overall_curr_month = data.sample_date[i].month
            
    # Add last month and year averages
    if overall_month_measurements != 0:
        overall_month_averages.append(overall_month_total / overall_month_measurements)
        overall_month_total = 0.0
        overall_month_measurements = 0
        
    if overall_year_measurements != 0:
        overall_year_averages.append(overall_year_total / overall_year_measurements)
        overall_year_total = 0.0
        overall_year_measurements = 0
        
    # Add differences between first and last year / month to resepective lists
    if len(overall_year_averages) > 0 and overall_year_averages[0] != 0:
        overall_year_differences.append((overall_year_averages[-1] - overall_year_averages[0]) / overall_year_averages[0])
        overall_month_differences.append((overall_month_averages[-1] - overall_month_averages[0]) / overall_month_averages[0])
    else:
        overall_year_differences.append(0)
        overall_month_differences.append(0)
    
summary_file = open("year_changes.csv", "w")
summary_file.write("Measure,YearChange,Achara,Boonsri,Busarakhan,Chai,Decha,Kannika,Kohsoom,Sadka,Somchair,Tansanee")
for measure in range(len(data.measure_names)):
    summary_file.write("\n{q}{m}{q},{y},{a},{b},{bu},{c},{d},{k},{ko},{s},{so},{t}".format(
            q=("\"" if "," in data.measure_names[measure] else ""), m=data.measure_names[measure], 
            y=overall_year_differences[measure], a=year_differences[measure*10], 
            b=year_differences[measure*10+1], bu=year_differences[measure*10+2], c=year_differences[measure*10+3], 
            d=year_differences[measure*10+4], k=year_differences[measure*10+5], ko=year_differences[measure*10+6], 
            s=year_differences[measure*10+7], so=year_differences[measure*10+8], t=year_differences[measure*10+9]))
summary_file.close()
    
month_file = open("month_changes.csv", "w")
month_file.write("Measure,Achara,Boonsri,Busarakhan,Chai,Decha,Kannika,Kohsoom,Sadka,Somchair,Tansanee")
for measure in range(len(data.measure_names)):
    month_file.write("\n{q}{m}{q},{mo},{a},{b},{bu},{c},{d},{k},{ko},{s},{so},{t}".format(
            q=("\"" if "," in data.measure_names[measure] else ""), m=data.measure_names[measure], 
            mo=overall_month_differences[measure], a=month_differences[measure*10], 
            b=month_differences[measure*10+1], bu=month_differences[measure*10+2], c=month_differences[measure*10+3], 
            d=month_differences[measure*10+4], k=month_differences[measure*10+5], ko=month_differences[measure*10+6], 
            s=month_differences[measure*10+7], so=month_differences[measure*10+8], t=month_differences[measure*10+9]))
month_file.close()
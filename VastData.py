import csv

from datetime import datetime

class VastData:
    def __init__ (self, readings, measures):
        
        # Creates csv readers for both sheets
        readings_reader = csv.reader(open(readings))
        next(readings_reader)
        measure_reader = csv.reader(open(measures))
        next(measure_reader)
        
        # Initialize sample variables
        self.sample_id = []
        self.sample_value = []
        self.sample_location = []
        self.sample_date = []
        self.sample_measure = []
        
        # Initialize measure variables
        self.measure_names = []
        self.measure_units = []
        
        self.sensor_location = ["Achara", "Boonsri", "Busarakhan", "Chai", "Decha", "Kannika", "Kohsoom", "Sakda", "Somchair", "Tansanee"]
        
        # Adds values from readings.csv to appropriate variables
        for row in readings_reader:
            self.sample_id.append(row[0])
            self.sample_value.append(float(row[1]))
            self.sample_location.append(row[2])
            self.sample_date.append(datetime.strptime(row[3], '%d-%b-%y'))
            self.sample_measure.append(row[4])
            
        # Adds values from measures.csv
        for row in measure_reader:
            self.measure_names.append(row[0])
            self.measure_units.append(row[1])
            
    # Removes row at given index
    # Causes problems when iterating over list, do not recommend using, instead save a list with the ids of the
    # rows you want to remove, removing them after finished iterating over list
    def removeRow(self, index):
        self.sample_id.pop(index)
        self.sample_value.pop(index)
        self.sample_location.pop(index)
        self.sample_date.pop(index)
        self.sample_measure.pop(index)
        
    # Removes row with given id
    def removeRowById(self, sample_id):
        index = self.sample_id.index(sample_id)
        self.removeRow(index)
    
    # Saves reading data as csv at given filepath
    def save(self, file_path):
        new_file = open(file_path, "w")
        new_file.write("id,value,location,sample date,measure\n")
        for i in range(len(self.sample_id)):
            new_file.write('{id},{value},{location},{date},{q}{measure}{q}\n'.format(id=self.sample_id[i], 
                    value=self.sample_value[i], location=self.sample_location[i], date=self.sample_date[i].strftime("%d-%b-%y"), 
                    measure=self.sample_measure[i], q="\"" if "," in self.sample_measure[i] else ""))
        new_file.close()
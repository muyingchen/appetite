import csv
import os

class CSVManager:
    """
    CSV Manager contains functions for csv writer & csv reader
    """
    def __init__(self, csv_file_path, fields=[]):
        """
        Define config information for csv file
        Args:
            csv_file_path (string): file path to the csv file we want to write
            fields_list (list(string)): fields in the csv file. ex) ['label', 'actual', 'tweets']
        """
        self.path = csv_file_path
        self.fields = fields
        self.create_file()
    
    def create_file(self):
        if not os.path.isfile(self.path):
            try:
                with open(self.path, 'w', newline='') as csvfile:
                    print('write one line on a csv file')
                    writer = csv.DictWriter(csvfile, fieldnames=self.fields)
                    writer.writeheader()    
            except:
                csvfile.close()
                raise Exception
            csvfile.close()
        else:
            print("create_file is not executed since file already exists")


    def write_line(self, data):
        """
        write a line to a csv file.
        Args:
            data(dict): dictionary of data that will be written in the row. 
                        It will ignore fields that are not contained in self.fields
        """
        self.check_if_file_exist()

        try:
            with open(self.path, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.fields, extrasaction='ignore')
                writer.writerow(data)
        except:
            csvfile.close()
            raise Exception
        
        csvfile.close()


    def write(self, data_list):
        """
        Write a list of data into the self.path csv file
        Args:
            data_list([dict]): list of dictionary that contains data to be written in self.path.
                                It will ignore fields that are not contained in self.fields.
        """
        self.check_if_file_exist()

        try:
            with open(self.path, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.fields, extrasaction='ignore')
                for data in data_list:
                    writer.writerow(data)
        except:
            csvfile.close()
            raise Exception
        
        csvfile.close()
    
    def read(self):
        """
        Return the list of dictionary of all the row in a csv file
        Return:
            stream of dictionary that contains data of each row,
        """
        self.check_if_file_exist()

        try:
            with open(self.path, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                return [row for row in reader]
                    
        except:
            csvfile.close()
            raise Exception
        
        csvfile.close()
    
    def read_stream(self):
        """
        Generate stream of row data in a csv file.
        Return (generator):
            stream of dictionary that contains data of each row,
        """
        self.check_if_file_exist()

        try:
            with open(self.path, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    yield row
        except:
            csvfile.close()
            raise Exception
        
        csvfile.close()
    
    def get_fields(self):
        """
        Return the name of fields
        """
        return self.fields
    
    def get_file_path(self):
        """
        Return the file path
        """
        return self.path

    def check_if_file_exist(self):
        if not os.path.isfile(self.path):
            raise Exception("file {} does not exist. Please run a function CSVManager.create_file()".format(self.path))
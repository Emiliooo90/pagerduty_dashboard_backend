import csv

class CSVReport:
    @staticmethod
    def generate_report(data, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data[0].keys())
            for row in data:
                writer.writerow(row.values())
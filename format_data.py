import csv
import os

def write_output_file(filename, directory):
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)


        # Write header
        writer.writerow(["Sales", "Date", "Region"])

        # Loop through all the data files in directory
        for data in os.listdir(directory):
            # Read file
            with open(f"data/{data}", 'r') as raw_data:
                reader = csv.reader(raw_data)
                for row in reader:
                    if 'pink morsel' in row:
                        quantity = int(row[2])
                        price = float(row[1].replace('$', ''))

                        sale = quantity * price
                        date = row[3]
                        region = row[4]

                        writer.writerow([sale, date, region])


write_output_file("DATA_FORMATTED","data")
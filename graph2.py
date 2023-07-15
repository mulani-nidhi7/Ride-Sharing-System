import matplotlib.pyplot as plt
import csv
def graph2():
    plt.figure(figsize=(25,15))
    # Open the CSV file and create a dictionary
    with open('database.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        drivers = {}

        # Iterate over the rows in the CSV file
        for row in reader:
            # Extract the location name and add it to the dictionary
            Driver_name = row['Driver']
            if Driver_name in drivers:
                drivers[Driver_name] += 1
            else:
                drivers[Driver_name] = 1

    font1={'family':'serif','weight':'bold','size':20,'color':'Green'}
    x=list(drivers.keys())
    y=list(drivers.values())
    plt.pie(y,labels=x,autopct='%0.f')
    plt.title('Pie Chart Showing The Total Count Of Trips Made By Each Driver',fontdict=font1)

    plt.show()
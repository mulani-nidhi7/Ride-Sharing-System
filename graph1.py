import matplotlib.pyplot as plt
import csv
def graph1():
    plt.figure(figsize=(25,15))
    # Open the CSV file and create a dictionary
    with open('database.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        locations = {}

        # Iterate over the rows in the CSV file
        for row in reader:
            # Extract the location name and add it to the dictionary
            location_name = row['pickup']
            if location_name in locations:
                locations[location_name] += 1
            else:
                locations[location_name] = 1
        for row in reader:
            # Extract the location name and add it to the dictionary
            location_name = row['drop']
            if location_name in locations:
                locations[location_name] += 1
            else:
                locations[location_name] = 1

    x=list(locations.keys())
    for i in range(len(x)):
        x[i]=x[i].split(',')[0]
    #print(x)
    y=list(locations.values())
    size=[]
    for i in y:
        size.append(i*50)
    plt.scatter(x,y,s=size,alpha=0.5)
    plt.xticks(fontsize=6, rotation=45)
    plt.title('Scatter Graph Showing Locations v/s their Count of Occuerence',color='blue')
    plt.show()
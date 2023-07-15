import matplotlib.pyplot as plt
import csv
def graph3():
    plt.figure(figsize=(15,15))
    # Open the CSV file and create a dictionary
    with open('database.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        distances= []
        c=0
        for row in reader:
            if c<25:
                distances.append(row[('distance')])
                c+=1

    distances.sort(key=float)
    #print(sorted(distances))
    #print(distances)

    font1={'family':'serif','weight':'bold','color':'Green'}
    plt.xticks(rotation=45)
    plt.xlabel('Distance in Kilometer',fontdict=font1)
    plt.ylabel('Frequency of range of Distance',fontdict=font1)
    plt.title('Hist Graph Showing Frequency for Distance Range',fontdict=font1)
    plt.hist(distances)
    plt.show()
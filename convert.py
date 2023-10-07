import pandas as pd
import numpy as np
import math
import pyxlsb

import pyxlsb
import pandas as pd
import matplotlib.pyplot as plt
import collections

def read_xlsb_to_dataframe_new(xlsb_file):
    dfs = []
    with pyxlsb.open_workbook(xlsb_file) as wb:
        with wb.get_sheet(1) as sheet:
            data = []
            header = None
            for i, row in enumerate(sheet.rows()):
                if i == 0:
                    # Use the 0th row as the header
                    header = [item.v for item in row]
                else:
                    data.append([item.v for item in row])
            df = pd.DataFrame(data, columns=header)
            dfs.append(df)
    return pd.concat(dfs, ignore_index=True)



def read_xlsb_to_dataframe(xlsb_file):
    dfs = []
    with pyxlsb.open_workbook(xlsb_file) as wb:
        with wb.get_sheet(1) as sheet:
            data = []
            for row in sheet.rows():
                data.append([item.v for item in row])
            df = pd.DataFrame(data)
            dfs.append(df)
    return pd.concat(dfs, ignore_index=True)


#main
#convert
input_path = "Global_Terrorism_Data_new.csv"
data = pd.read_csv(input_path, encoding="ISO-8859-1")
#data = read_xlsb_to_dataframe_new(input_path)
print(data.head())


#print attacktyp[e_1_txt

#number of attack_types
attacktypes = np.unique(data["attacktype1_txt"])
print(attacktypes)
#print(data["city"])

#singular frequenncy of attacktypes

#print(len(data["city"]))



city_types = np.unique(data["city"])
#print(city_types)
#print(len(city_types))

count = [0] * len(city_types)

category_counts = data['city'].value_counts()
print(category_counts)

top_categories = category_counts.head(50)

# Plot the top 50 categories in a bar graph
plt.figure(figsize=(10, 6))
top_categories.plot(kind='bar')
plt.title('Top 50 Categories by Frequency')
plt.xlabel('Category')
plt.ylabel('Frequency')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()



attacktype_list = [0] * len(attacktypes)
#now for every attacktype
for i in range(0, len(data["attacktype1_txt"])):
    #for attacktypes[0]
    for j in range(0, len(attacktypes)):

        if(data["attacktype1_txt"][i]==attacktypes[j]):
            attacktype_list[j] = attacktype_list[j] + 1





#percentage of attacks
total = sum(attacktype_list)
percentages = [(count / total) * 100 for count in attacktype_list]



# Add smaller text for labels outside the chart
'''for i, label in enumerate(attacktypes):
    plt.text(
        1,  # Adjust the x-coordinate for text outside the chart
        i / len(attacktypes) - 0.1,  # Adjust the y-coordinate for text outside the chart
        f"{label}: {attacktype_list[i]}",
        fontsize=10,  # Adjust font size for text outside the chart
        bbox={'facecolor': 'white', 'edgecolor': 'black', 'boxstyle': 'round'},
    )

plt.title("All attacktype frequencies")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the chart
plt.show()'''
plt.figure(figsize=(10, 6))  # Adjust the figure size
ax = plt.gca()
ax.pie(
    percentages,
    labels=attacktype_list,
    autopct='%1.1f%%',
    startangle=140,
    textprops={'fontsize': 10},  # Adjust font size for text inside the chart
    pctdistance=0.85,  # Move the percentage text inside the chart
)

# Move the pie chart to the right
plt.subplots_adjust(left=0.1)

# Add labels outside the chart with adjusted positions and font size
outside_labels = [f"{label}: {attacktype_list[i]}" for i, label in enumerate(attacktypes)]
plt.legend(outside_labels, title="Frequency", bbox_to_anchor=(1.5,1.025), loc="upper right", fontsize=8)

plt.title("All attacktypes frequencies")

# Display the chart
plt.show()



#attacktypes charts With their corresponding location 
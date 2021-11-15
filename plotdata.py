#Thomas Pallan - Check In 1
import seaborn as sns
import matplotlib.pyplot as plt

def displayCharts():
    """Displays the car dealership data into several useful visual plots.
    Args:
        filepath (string): path to data file. (will eventually need, used 
            sample data from seaborn so I didn't use arg yet)
    Side effects:
        Displays seaborn and matplotlib plots.
    """
    
    sns.set_theme()
    sns.set(rc={'figure.figsize':(8,8)})
    colors = sns.color_palette('pastel')[0:5]

    
    cars = sns.load_dataset('mpg').dropna()

    
    cars['brand'] = cars['name'].str.extract(r"(^\w+)", expand=True)
    pie_data = cars['brand'].value_counts()
    
    count = 0
    for i in list(pie_data.keys()):
        if pie_data[i] < 10:
            count +=1
            del pie_data[i]
    pie_data['other'] = count

    pie_label = pie_data.keys()
    plt.pie(pie_data, labels = pie_label, colors = colors, autopct='%.0f%%')

    #PLEASE READ STATEMENT BELOW:
    #boxplot (to display boxplot comment out plt.pie command above and uncomment below)
    #sns.boxplot(x=cars.horsepower).set(xlabel = "Horsepower", title='Boxplot of Vehicle Horsepower')

    plt.show()
    
displayCharts()

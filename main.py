import pandas as pd
import seaborn as sns
sns.set_theme()
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

data = pd.read_csv("strong.csv")
data['ord'] = data["Date"]
data['ord'] = pd.to_datetime(data['ord'])
data['ord'] = data['ord'].map(dt.datetime.toordinal)
i = 0
data['Year'] = data['Date']
data['month'] = data['Date']
for m in data['Date']:
    data['Year'][i] = data['Date'][i][0:4]
    data['month'][i] = data['Date'][i][5:7]
    i+=1

benchData = data[data['Exercise Name'] == 'Bench Press (Barbell)'] 
squatData = data[data['Exercise Name'] == 'Squat (Barbell)']
deadliftData = data[data['Exercise Name'] == 'Deadlift (Barbell)']
plotdata = pd.concat([benchData, squatData, deadliftData])
plotdata = plotdata[plotdata["Reps"]==1]

sp = sns.lmplot(data=plotdata, x='ord', y='Weight', hue='Exercise Name', col='Year', facet_kws=dict(sharex=False, sharey=False, legend_out=False))
sns.move_legend(sp, "lower center", ncol=3, title=None)
i=0

for axis in sp.axes_dict.values():
    if i==0:
        axis.set_xticklabels(plotdata['month'][plotdata['Year']=='2020'])
    elif i==1:
        axis.set_xticklabels(plotdata['month'][plotdata['Year']=='2021'])
    elif i==2:
        axis.set_xticklabels(plotdata['month'][plotdata['Year']=='2022'])
    axis.set_xlabel('Month')
    #axis.title('ORMs')
    i+=1


plt.show()
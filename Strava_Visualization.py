import pandas as pd
import matplotlib.pyplot as plt

file = 'strava_activities.csv'
data = pd.read_csv(file)

activity_type = data['type']
activity_count = activity_type.value_counts()
# a = activity_type.unique()
a = activity_type.groupby(by='type')

x = data['start_date_local']
y = data['moving_time']

# print(activity_type, activity_count)
# print(a)
# print(activity_type.groupby(by='type'))
# print(data)


plt.bar(a, activity_count)
plt.xlabel('Type')
plt.ylabel('Count')
plt.title('Data')
plt.show()

plt.plot(x,y)
plt.xlabel('Date')
plt.ylabel('Moving Time')
plt.show()


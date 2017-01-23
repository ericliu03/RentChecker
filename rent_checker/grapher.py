import matplotlib.pyplot as plt
from matplotlib.mlab import csv2rec
from dbaccessor import DBAccessor

db = DBAccessor()
data_cursor = db.find()
units_dict = {}

for data in data_cursor:
    title = data['title']
    if title not in units_dict:
        units_dict[title] = {'time_list': [], 'price_list': [], 'beds': data['bads']}
    units_dict[title]['time_list'].append(data['record_time'])
    units_dict[title]['price_list'].append(float(data['price']))

# fig, ax = plt.subplots(1, 1, figsize=(12, 14))

for title, data_dict in units_dict.iteritems():
    if sum(data_dict['price_list']):
        beds = data_dict['beds']
        color = 'r'
        if beds == '1':
            color = 'g'
        plt.plot(data_dict['time_list'], data_dict['price_list'],
                 color=color,marker='o', linestyle='--', label=title + ' beds: '+beds+' : '+str(data_dict['price_list'][-1]))


plt.xlabel('Date/Time')
plt.ylabel('Price')
plt.title('Price trend of Olivian')

# Finally, save the figure as a PNG.
# You can also save it as a PDF, JPEG, etc.
# Just change the file extension in this call.
plt.legend(loc=9, bbox_to_anchor=(1.4, 1))
plt.savefig('./data/result.png', bbox_inches='tight')

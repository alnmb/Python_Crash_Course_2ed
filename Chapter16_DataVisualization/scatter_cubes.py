import matplotlib.pyplot as plt

#x_values = [1,2,3,4,5]
#y_values = [1,8,27,64,125]

x_values = range(1,5000)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
#ax.scatter(x_values,y_values,c='red',s=10)
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.inferno,s=20)

#set chart title and label axes
ax.set_title("Cubes Numbers", fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)
#ax.set(xlim=(0,5100),ylim=(0,550000))

#set size of tick labels
ax.tick_params(axis='both',which='major',labelsize=14)
plt.savefig('Chapter16_DataVisualization/cubes_plot_scatter.png',bbox_inches='tight')
plt.show()

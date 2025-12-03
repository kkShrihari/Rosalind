import numpy as np
import matplotlib.pyplot as plt


#Creating bars
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

#if u want horizontal bars
plt.barh(x,y,color='skyblue',height=0.5)
plt.show()

# vertical bar and color and bar width
plt.bar(x, y, color='hotpink',width = 0.1) #or use hexagonal color values eg #4CAF50
plt.show()



##########################################################################################
#Histogram
##########################################################################################


import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(170, 10, 250)
print(x)

plt.hist(x)
plt.show()

#Complete example
# 1. Generate random data
np.random.seed(42)  # for reproducibility
x1 = np.random.normal(170, 10, 250)  # mean=170, sd=10
x2 = np.random.normal(160, 8, 250)   # second dataset for comparison

# 2. Create the figure
plt.figure(figsize=(10, 6))

#  3. Plot histogram
plt.hist(
    x1,                      # data
    bins=20,                 # number of bins (divisions on x-axis)
    color='skyblue',         # bar color
    edgecolor='black',       # bar border color
    linewidth=1.2,           # border thickness
    alpha=0.7,               # transparency (0–1)
    label='Dataset 1 (mean=170)',  # label for legend
    histtype='bar',          # options: 'bar', 'barstacked', 'step', 'stepfilled'
    density=False,           # if True → show probability density instead of counts
    orientation='vertical',  # options: 'vertical' or 'horizontal'
)

#  4. Add a second histogram overlapping the first
plt.hist(
    x2,
    bins=20,
    color='lightcoral',
    edgecolor='black',
    linewidth=1.2,
    alpha=0.5,
    label='Dataset 2 (mean=160)',
    histtype='stepfilled'
)

#  5. Axis labels and title
plt.title("Height Distribution Comparison", fontsize=16, fontweight='bold', color='navy')
plt.xlabel("Height (cm)", fontsize=12)
plt.ylabel("Frequency (count)", fontsize=12)

# 6. Optional axis limits
plt.xlim(130, 200)   # restrict x-axis range
plt.ylim(0, 50)      # restrict y-axis range

# 7. Add grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

#  8. Add legend
plt.legend(loc='upper right', fontsize=10)

#  9. Add annotations
plt.text(175, 45, 'Peak frequency area', fontsize=10, color='darkred')

# 10. Add density line (optional)
from scipy.stats import norm
mean, std = np.mean(x1), np.std(x1)
xmin, xmax = plt.xlim()
x_vals = np.linspace(xmin, xmax, 100)
p = norm.pdf(x_vals, mean, std)
plt.plot(x_vals, p * len(x1) * (xmax - xmin) / 20, 'k--', linewidth=2, label='Normal PDF')

# 11. Show everything
plt.tight_layout()
plt.show()


#################################################################################
#Pie charts
#################################################################################

import matplotlib.pyplot as plt
import numpy as np
#By default the plotting of the first wedge starts from the x-axis and moves counterclockwise:
y = np.array([35, 25, 10, 15,15])

mylabels = ["Apple","Banana","Orange","Pineapple","Plums"]
myexplode = [0.2,0.3,0.4,0.5,0.6]
mycolors= ["skyblue",'hotpink','lightcoral','lightgreen','lightsalmon']
plt.pie(y,labels=mylabels,colors=mycolors,startangle=0,explode=myexplode,shadow=True)
plt.legend(title = "Five Fruits:", loc='upper right')
plt.show() 

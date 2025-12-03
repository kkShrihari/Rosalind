import numpy as np
import matplotlib.pyplot as plt


x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()

#Compare plots
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y, color ='b')
plt.scatter(y,x,color='r')
plt.show()


# adding more colors (each point one color)
x = np.array([1,2,3,4,5])
y = np.array([0,1,2,3,4])

colors = np.array(['red','blue','green','black','orange'])

plt.scatter(x,y,color=colors)
plt.show()


#color mapss
#give color in range from 0(purple) to 100(yellow)
x = np.array([1,2,3,4,5])
y = np.array([0,1,2,3,4])

#value of colormap
colors = np.array([10,30,50,70,90])

plt.scatter(x,y,c=colors,cmap='winter')

plt.colorbar() #shows intensity label
plt.show()

# Available ColorMaps
# You can choose any of the built-in colormaps:

# Name		 	Reverse	
# Accent		 	Accent_r	
# Blues		 	Blues_r	
# BrBG		 	BrBG_r	
# BuGn		 	BuGn_r	
# BuPu		 	BuPu_r	
# CMRmap		 	CMRmap_r	
# Dark2		 	Dark2_r	
# GnBu		 	GnBu_r	
# Greens		 	Greens_r	
# Greys		 	Greys_r	
# OrRd		 	OrRd_r	
# Oranges		 	Oranges_r	
# PRGn		 	PRGn_r	
# Paired		 	Paired_r	
# Pastel1		 	Pastel1_r	
# Pastel2		 	Pastel2_r	
# PiYG		 	PiYG_r	
# PuBu		 	PuBu_r	
# PuBuGn		 	PuBuGn_r	
# PuOr		 	PuOr_r	
# PuRd		 	PuRd_r	
# Purples		 	Purples_r	
# RdBu		 	RdBu_r	
# RdGy		 	RdGy_r	
# RdPu		 	RdPu_r	
# RdYlBu		 	RdYlBu_r	
# RdYlGn		 	RdYlGn_r	
# Reds		 	Reds_r	
# Set1		 	Set1_r	
# Set2		 	Set2_r	
# Set3		 	Set3_r	
# Spectral		 	Spectral_r	
# Wistia		 	Wistia_r	
# YlGn		 	YlGn_r	
# YlGnBu		 	YlGnBu_r	
# YlOrBr		 	YlOrBr_r	
# YlOrRd		 	YlOrRd_r	
# afmhot		 	afmhot_r	
# autumn		 	autumn_r	
# binary		 	binary_r	
# bone		 	bone_r	
# brg		 	brg_r	
# bwr		 	bwr_r	
# cividis		 	cividis_r	
# cool		 	cool_r	
# coolwarm		 	coolwarm_r	
# copper		 	copper_r	
# cubehelix		 	cubehelix_r	
# flag		 	flag_r	
# gist_earth		 	gist_earth_r	
# gist_gray		 	gist_gray_r	
# gist_heat		 	gist_heat_r	
# gist_ncar		 	gist_ncar_r	
# gist_rainbow		 	gist_rainbow_r	
# gist_stern		 	gist_stern_r	
# gist_yarg		 	gist_yarg_r	
# gnuplot		 	gnuplot_r	
# gnuplot2		 	gnuplot2_r	
# gray		 	gray_r	
# hot		 	hot_r	
# hsv		 	hsv_r	
# inferno		 	inferno_r	
# jet		 	jet_r	
# magma		 	magma_r	
# nipy_spectral		 	nipy_spectral_r	
# ocean		 	ocean_r	
# pink		 	pink_r	
# plasma		 	plasma_r	
# prism		 	prism_r	
# rainbow		 	rainbow_r	
# seismic		 	seismic_r	
# spring		 	spring_r	
# summer		 	summer_r	
# tab10		 	tab10_r	
# tab20		 	tab20_r	
# tab20b		 	tab20b_r	
# tab20c		 	tab20c_r	
# terrain		 	terrain_r	
# twilight		 	twilight_r	
# twilight_shifted		 	twilight_shifted_r	
# viridis		 	viridis_r	
# winter		 	winter_r



#Examples with sizes
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
alphas = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1,1,1])
plt.scatter(x, y, c=sizes, cmap='viridis', s=sizes,alpha=alphas)
#or simply alpha=0.5
plt.show()


#combine color size and alpha
x = np.random.randint(100,size=(100))
y = np.random.randint(100,size=(100))
colors = np.random.randint(100,size=(100))
sizes = 10 * np.random.randint(100,size=(100))

plt.scatter(x,y,c=colors, s=sizes,alpha=0.5,cmap='nipy_spectral')
plt.colorbar()
plt.title("Color Bubbles",loc ='center')
plt.show()

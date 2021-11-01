import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

os.chdir('C:\\Users\deens\OneDrive\Documents\Career\DataScienceMachineLearning\Tools\git\springboard\springboard-data-science')

brf = pd.read_hdf('brfss.hdf5')

height = brf.HTM4
height_jitter = height + np.random.normal(0,2,size=len(brf))
#so this will change the height by adding to it randomly generated numbers from
#the normal distribution with mean=0 & standard deviation = 2. so that will break it up
#because each point will move a diff distance, BUT THEN DOESN'T THAT CHANGE THE DATA??
#or is this only for DISPLAY PURPOSES ONLY?!
#it will move the dots like +/-2, but it all evens out since the average is ZERO!!!
#so doesn't net change anything
#so this will blur the literal lines of separation that caused these to all form in formations
#because it's basically discrete - the heights were rounded to the nearest so there's only
#a finite range essentially. just like the jitter feature in seaborn, this gives some wiggle
#room to break these dots free out of/from the line formations and spread out a little bit to
#breathe. There's some wiggle room because since these are ROUNDED, and on top of that, these
#are rounded from INCHES, and one inch is 2.5 centimeters, so each one has wiggle room of about
#that, that's like the width of the margin / swimming "LANE" they can be within and still be
#representing the same info, just like categorical/discrete jittering
#so maybe that's why we made the mean/stdv as 0/2 so we can move around +/- 2, and it won't
#affect things first off cuz averages out to netzero, but also, since these were basically
#bucketized anyway, like they only did whole inches, so like 65 inches (5'5") was rounded to
#165cm. so now whatevers in/at that 165 bucket could get wiggled a little bit and still not
#change anything cuz it's not hopping into/overstepping its boundaries, cuz the next / 
#neighboring ones would be based off of 5'4" (~163cm) and 5'6" (~168cm), so you got like up
#to +/- 2cm wiggle room in each bucket / of a gap/width 
weight = brf.WTKG3
weight_jitter = weight + np.random.normal(0,2,len(brf))
#this will let us blurr the cross-stitch lines horizontally too to get a blended picture
#these weights were rounded from POUNDS, and 1 lb = 2.2kg, so similarly stdv of 2 to jitter
#would be appropriate
plt.plot(height_jitter, weight_jitter, 'o', alpha=.01, markersize=1)
plt.xlabel('Height in cm')
plt.ylabel('Weight in kg')

#Now let's STRETCH it out to again create some more space- as you can see, there's alot of
#empty, unused, wasted white space around the cluster, so let's "crop" it / "zoom in"
#Change the axis limits / boundaries
plt.axis([140,200, 30, 160])




brf.dropna(subset=['AGE', 'WTKG3'],inplace=True)

sns.violinplot(data=brf, x='AGE',y='WTKG3')


#sns.jointplot(data=brf,x='AGE',y='WTKG3')

#is there a way to do a 3D grid to show depth/concentration!?





age = brf['AGE'] + np.random.normal(0, 0.5, size=len(brf))
weight = brf['WTKG3'] + np.random.normal(0, 2, size=len(brf))
plt.plot(age, weight, 'o', markersize=1, alpha=0.2)


from scipy.stats import gaussian_kde
x=brf.AGE
y=brf.WTKG3

xy = np.vstack([x,y])
z = gaussian_kde(xy)(xy)

fig, ax = plt.subplots()
ax.scatter(x, y, c=z, s=100)
plt.show()








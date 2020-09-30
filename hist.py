import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import curve_fit as curve_fit
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.colors as mcolors
import matplotlib.patheffects as PathEffects
import matplotlib.gridspec as gridspec
import pandas as pd
import numpy as np

width = 512.11743/72.2
font = 9
mpl.rc('text', usetex=True)
mpl.rc('font', family = 'serif')
mpl.rcParams['xtick.labelsize']=font-1
mpl.rcParams['ytick.labelsize']=font-1

mpl.rcParams['text.latex.preamble'] = [
    r'\usepackage{amsmath}',
    r'\usepackage{amssymb}']


#====================================================================================

#data = pd.read_csv("customReport3.sed.csv")

#xray = data.loc[(data['experimentalTechnique'] == 'X-RAY DIFFRACTION') & (data['publicationYear'] < 2012)]

#print(xray['structureMolecularWeight'].shape)

xray = np.load("xray.npy")
nmr = np.load("nmr.npy")

fig=plt.figure(figsize=(1,1))
fig.set_figheight((np.sqrt(5.0)-1.0)/2. * width/2)
fig.set_figwidth(width/2)
gs1 = gridspec.GridSpec(1,1)
gs1.update(wspace=0, hspace=0)

#ax1 = plt.subplot(gs1[0])
#ax1.hist(xray, 15, range = (0,300), rwidth = 0.5)

#plt.xlabel(r"Molecular Weight (kDa)", fontsize=font)
#plt.ylabel(r"Number of Molecules", fontsize=font)
#plt.title(r'X-RAY', fontsize=font)
#plt.savefig("xray.pdf",bbox_inches='tight')
#plt.close()

ax1 = plt.subplot(gs1[0])
ax1.hist(nmr, 15, range = (0,100), rwidth = 0.5)

plt.xlabel(r"Molecular Weight (kDa)", fontsize=font)
plt.ylabel(r"Number of Molecules", fontsize=font)
plt.title(r'NMR', fontsize=font)
plt.savefig("nmr.pdf",bbox_inches='tight')
plt.close()

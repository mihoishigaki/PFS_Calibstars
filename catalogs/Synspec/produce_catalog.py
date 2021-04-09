import numpy as np
import pandas as pd

stars = {"K-giant": \
         [4800., 1.6, 195.4684554018686, +29.1883153466994, 11.50, 9.049], \
         "G-dwarf": \
         [6000., 4.5, 156.8510260053169, +01.4000534041333, 11.10, 9.595]}

fehgrid = np.arange(-2.5, 0.0, 0.5)
alphagrid = [0.0] * len(fehgrid)



starnames = ()
ras = ()
decs = ()
vmags = ()
kmags = ()


teffs = ()
loggs = ()
fehs = ()
alphas = ()


for i, star in enumerate(stars.keys()):
    teff = stars[star][0]
    logg = stars[star][1]
    ra = stars[star][2]
    dec = stars[star][3]
    vmag = stars[star][4]
    kmag = stars[star][5]

    
    for j, feh in enumerate(fehgrid):

        alpha = alphagrid[j]

        starname = star + "_teff%.0f-logg%.1f-feh%.1f-alpha%.1f"%\
            (teff, logg, feh, alpha)

        
        starnames = np.append(starnames, starname)
        ras = np.append(ras, ra)
        decs = np.append(decs, dec)
        vmags = np.append(vmags, vmag)
        kmags = np.append(kmags, kmag)
        
        teffs = np.append(teffs, teff)
        loggs = np.append(loggs, logg)
        fehs = np.append(fehs, feh)
        alphas = np.append(alphas, alpha)
        



data = { "starname": starnames, "ra": ras, "dec": decs, \
         "Vmag": vmags, "Kmag": kmags, \
         "teff": teffs, "logg": loggs, "feh": fehs, "alphas": alphas}

df = pd.DataFrame(data)

df.to_csv("catalog_Synspec.csv", index = False)


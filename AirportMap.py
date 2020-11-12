import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.feature as cfeature

fig = plt.figure()
ax = fig.add_axes([0, 0, 5, 5],projection = ccrs.Mercator())

states_provinces = cfeature.NaturalEarthFeature(
                   category='cultural',
                   name='admin_1_states_provinces_lines',
                   scale='10m',
                   facecolor='none')

gl = ax.gridlines(linewidth=0.4, color='black', alpha=0.5, linestyle='-', draw_labels=True)

ax.set_extent([-107, -93, 25, 37], ccrs.PlateCarree())

ax.add_feature(states_provinces, edgecolor='0.2',linewidth=1.5)
ax.add_feature(cfeature.LAND,linewidth=1.5)
ax.add_feature(cfeature.OCEAN,linewidth=1.5)
ax.add_feature(cfeature.COASTLINE,linewidth=1.5)
ax.add_feature(cfeature.RIVERS,linewidth=0.5)
ax.add_feature(cfeature.BORDERS, linestyle='-', edgecolor='0.2', linewidth=1.5)

# Easterwood Airport (College Station)
ax.scatter(-96.3666,30.5937,s=500,
         color='darkred', marker='*',edgecolor = 'k',
          transform = ccrs.PlateCarree(),
         )
# George Bush Intercontinental Airport (IAH)
ax.scatter(-95.3368,29.9902,s=500,
         color='blue', marker='*',edgecolor = 'k',
          transform = ccrs.PlateCarree(),
         )
# Austin-Bergstrom International Airport
ax.scatter(-97.6664,30.1975,s=500,
         color='orange', marker='*',edgecolor = 'k',
          transform = ccrs.PlateCarree(),
         )
# Dallas/Fort Worth International Airport
ax.scatter(-97.0403,32.8998,s=500,
         color='green', marker='*',edgecolor = 'k',
          transform = ccrs.PlateCarree(),
         )

ax.legend(['CLL', 'IAH', 'AUS', 'DFW'],loc =  'upper left', edgecolor = 'k', markerscale = 1)
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
gl.right_labels = False
gl.top_labels = False

plt.rcParams.update({'font.size': 15})
plt.title('Airport Locations')

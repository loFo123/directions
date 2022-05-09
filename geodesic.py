from geographiclib.geodesic import Geodesic
geod = Geodesic.WGS84
g = geod.Inverse(10.426689, 76.330303, 10.425771, 76.319124)
print ("The initial direction is {:.3f} degrees.".format(g['azi1']))
print(g)

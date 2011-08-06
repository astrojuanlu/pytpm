# Convert HIPPARCOS data using SLALIB. The output files can then be
# used to compare with PyTPM.
import math
from pyslalib import slalib
import read_data
from read_data import get_hipdata

tab = get_hipdata()

# sla_fk524.
# Convert HIP FK5 J2000 coordinates as given by Vizier to B1950
# coordinates using SLALIB function fk524, which takes proper motion
# as well. This is NOT a transformation to HIPPARCOS frame. I just use
# the coordinates given by Vizier to compare proper motion conversions
# using PyTPM and SLALIB.
#raj = [math.radians(i) for i in tab['raj2']]
#decj = [math.radians(i) for i in tab["decj2"]]
## Milli-arcsec/Jul. year *cos(dec) into rad/Jul year.
#pmaj = [math.radians(i / 1000.0 / math.cos(j) / 3600.0)
#        for i, j in zip(tab['pma'], decj)]
#pmdj = [math.radians(i / 1000.0 / 3600.0)
#        for i in tab['pmd']]
#pxj = [i / 1000.0 for i in tab['px']]  # milli-arcsec to arc-sec.
#rvj = list(0.0 for i in range(len(pxj)))
#
#rab = []
#decb = []
#pmab = []
#pmdb = []
#pxb = []
#rvb = []
#
#for r, d, px, pa, pd, rv in zip(raj, decj, pxj, pmaj, pmdj, rvj):
#    r1, d1, pa1, pd1, px1, rv1 = slalib.sla_fk524(r, d, pa, pd, px, rv)
#    rab.append(math.degrees(r1))
#    decb.append(math.degrees(d1))
#    # rad/trop. year to milli-arcsec/trop. year.
#    pmab.append(math.degrees(pa1) * 3600.0 * 1e3)
#    pmdb.append(math.degrees(pd1) * 3600.0 * 1e3)
#    pxb.append(px1 * 1e3)  # arc-sec to milli-arc-sec
#    rvb.append(rv1)
#
#with open("slalib_hip_fk524.txt", "w") as f:
#    f.write("# RAB1950 RAJ1950 PX PMAB1950 PMDB1950 RV\n")
#    f.write(
#        "# deg deg milli-arcs milli-arcs/trop.yr milli-arcs/trop.yr km/s\n")
#    for r, d, px, pa, pd, rv in zip(rab, decb, pxb, pmab, pmdb, rvb):
#        # Formats are generous.
#        # degrees, miili-arc, milli-arcsec/trop. year, km/s.
#        s = "%14.9f %14.9f %10.4f %10.4f %10.4f %6.4f\n"
#        f.write(s % (r, d, px, pa, pd, rv))

# sla_eqecl.
# Convert J2000.0 FK5 equatorial coordinates to IAU 1980 ecliptic
# coordinates at J2000.0
#raj2 = (math.radians(i) for i in tab['raj2'])
#decj2 = (math.radians(i) for i in tab['decj2'])
# 
#ecl_lon = []
#ecl_lat = []
# 
#for r, d in zip(raj2, decj2):
#    x, y = slalib.sla_eqecl(r, d, 51544.5)
#    ecl_lon.append(math.degrees(x))
#    ecl_lat.append(math.degrees(y))
# 
#with open("slalib_hip_eqecl.txt", "w") as f:
#    f.write("# ECL_LON_J2000(deg) ECL_LAT_J2000(deg)\n")
#    for i, j in zip(ecl_lon, ecl_lat):
#        # The format is very generous. The data are never this
#        # accurate. .9 => ~1e-5 arc-sec.
#        s = "%14.9f %14.9f \n"
#        f.write(s % (i, j))

#sla_ecleq.
#Convert IAU 1980 J2000 ecliptic coordinates to FK5 J2000 equatorial
#coordinates.
#ecl_lon = (math.radians(i) for i in tab['elon2'])
#ecl_lat = (math.radians(i) for i in tab['elat2'])
# 
#raj2 = []
#decj2 = []
# 
#for r, d in zip(ecl_lon, ecl_lat):
#    x, y = slalib.sla_ecleq(r, d, 51544.5)
#    raj2.append(math.degrees(x))
#    decj2.append(math.degrees(y))
# 
#with open("slalib_hip_ecleq.txt", "w") as f:
#    f.write("# RAJ2000(deg) DECJ2000(deg)\n")
#    for i, j in zip(raj2, decj2):
#        # The format is very generous. The data are never this
#        # accurate. .9 => ~1e-5 arc-sec.
#        s = "%14.9f %14.9f \n"
#        f.write(s % (i, j))

# sla_eqgal.
# Convert FK5 J2000.0 equatorial coordinates to galactic.
#raj2 = (math.radians(i) for i in tab['raj2'])
#decj2 = (math.radians(i) for i in tab['decj2'])
# 
#gal_lon = []
#gal_lat = []
# 
#for r, d in zip(raj2, decj2):
#    x, y = slalib.sla_eqgal(r, d)
#    gal_lon.append(math.degrees(x))
#    gal_lat.append(math.degrees(y))
# 
#with open("slalib_hip_eqgal.txt", "w") as f:
#    f.write("# GAL_LON(deg) GAL_LAT(deg)\n")
#    for l, b in zip(gal_lon, gal_lat):
#        # The format is very generous. The data are never this
#        # accurate. .9 => ~1e-5 arc-sec.
#        s = "%14.9f %14.9f \n"
#        f.write(s % (l, b))

#sla_galeq.
# Convert galactic coordinates to FK5 J2000 coordinates.
#gal_lon = (math.radians(i) for i in tab['glon'])
#gal_lat = (math.radians(i) for i in tab['glat'])
# 
#raj2 = []
#decj2 = []
# 
#for l, b in zip(gal_lon, gal_lat):
#    x, y = slalib.sla_galeq(l, b)
#    raj2.append(math.degrees(x))
#    decj2.append(math.degrees(y))
# 
#with open("slalib_hip_galeq.txt", "w") as f:
#    f.write("# RAJ2000(deg) DECJ2000(deg)\n")
#    for r, d in zip(raj2, decj2):
#        # The format is very generous. The data are never this
#        # accurate. .9 => ~1e-5 arc-sec.
#        s = "%14.9f %14.9f \n"
#        f.write(s % (r, d))

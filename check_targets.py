"""
check_targets.py
Check which TESS sectors have 2-minute light curves for each target star.
"""
import lightkurve as lk

TARGETS = ["LHS 3844", "L 98-59", "LHS 1140", "TOI-700"]

for name in TARGETS:
    # Search the MAST archive for TESS light curves of this star.
    # author="SPOC": only the official TESS pipeline products
    # exptime=120:   only 2-minute cadence data
    results = lk.search_lightcurve(name, mission="TESS", author="SPOC", exptime=120)

    # Each row in the results is one light curve; the "mission" column
    # says which sector it came from, e.g. "TESS Sector 03".
    sectors = sorted(set(results.table["mission"]), key=lambda s: int(s.split()[-1]))

    print(f"{name}: {len(results)} light curves")
    for s in sectors:
        print("   ", s)
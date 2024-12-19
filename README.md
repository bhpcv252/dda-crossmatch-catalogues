# Crossmatching Catalogues

This project performs crossmatching between the AT20G Bright Source Catalogue and the SuperCOSMOS All-Sky Catalogue using the Haversine formula.

---
This project aims to facilitate astrophysical studies by providing an efficient method for crossmatching celestial sources between radio and optical catalogues.

## Datasets

1. **AT20G Bright Source Catalogue**
   - Source: [MNRAS/384/775](https://cdsarc.u-strasbg.fr/viz-bin/Cat?J/MNRAS/384/775)
   - Description: A catalogue of bright radio sources in the Southern Hemisphere observed at 20 GHz.

2. **SuperCOSMOS All-Sky Catalogue**
   - Source: [SuperCOSMOS All-Sky Catalogue](http://ssa.roe.ac.uk/allSky)
   - Description: A photographic sky survey providing optical data for sources across the entire sky.

## Implementation

1. **Data Ingestion**:
   - Parse the AT20G Bright Source Catalogue and the SuperCOSMOS All-Sky Catalogue into a structured format.

2. **Preprocessing**:
   - Convert celestial coordinates (RA, Dec) from degrees to radians for compatibility with trigonometric functions.

3. **Crossmatching**:
   - For each source in the AT20G catalogue, compute the angular distance to all sources in the SuperCOSMOS catalogue using the Haversine formula.
   - Match sources that fall within a specified angular distance threshold.

4. **Output**:
   - Generate a list of matched pairs with the following fields:
     - Source ID (AT20G)
     - Source ID (SuperCOSMOS)
     - Angular Distance (arcseconds)

   - Generate a list of not matched rows:
     - Source ID (AT20G)


## References

- [Haversine Formula](https://en.wikipedia.org/wiki/Haversine_formula)
- [AT20G Bright Source Catalogue](https://cdsarc.u-strasbg.fr/viz-bin/Cat?J/MNRAS/384/775)
- [SuperCOSMOS All-Sky Catalogue](http://ssa.roe.ac.uk/allSky)


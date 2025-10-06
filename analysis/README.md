## Purpose:
The purpose of this directory is to do nothing more than to sort a collection of data files that were used to compare various codes that compute the BKM10 cross-section.

The number of combinations we needed to match across is determined by, of course, the settings of the kinematics and the CFFs. But assuming those values are fixed and match across all the codes, the number of possible settings we need to match is determined by the number of valid answers to the following questions:

1. Are the WW-relations on or off? (2 options)
2. Are we comparing the BH, DVCS, or Interference contributions? (3 options)
3. Is the target unpolarized, positively-polarized longitudinally, or negatively-polarized longitudinally? (3 options)
4. Is the beam unpolarized, positiviely polarized, or negatively polarized? (3 options)

There are some additional checks we ran which increased the total number of options: Do we compare against data contained in the plots in a paper; do we perform comparison over one or more kinematic settings; and so on. I do not currently remember all of the possible configurations we have run or not run. Please stand by for updates.

## Notes:

1. If a given directory does *not* contain plots with the comparison, then it means we have *technically not yet done the comparison* at those settings yet. It is like that we did do the comparison in the past, but the checking with the most recent version of the code has not yet been done.

2. We intend to perform those final checks, but we will have to do it at a later time.

3. The plots (`.png` files) that are currently each directory were generated with the file called `analysis_script.py`. *If you try to run `analysis_script.py` as it stands it will not generate the same plots. There have been some updates to the codebase that have rendered replication impossible as of now. Please stand by for future updates.*
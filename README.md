#===================================================================#
# README      for Fastq_compare                                     #
#                                                                   #
# Code by T. Coudrat, P. Moncuquet and A. Nemri [pySickle_team3]    #
# https://github.com/thomascoudrat/pySickle_team3                   #
# Please report bugs at adnane.nemri@csiro.au                       #
#===================================================================#

This script generates a report on a single end fastq file before and after changes were made to it, eg
by a quality trimming software. For the comparison to be meaningful, the second file should be inherited from the first one.

dependencies: BioPython

usage: python Fastq_compare.py <fastq_before> <fastq_after> -out <outfile>





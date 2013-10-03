============================================================================
 README for fastq_compare                                                   
                                                                            
 Code contributed by T. Coudrat, P. Moncuquet and A. Nemri [pySickle_team3] 
 https://github.com/thomascoudrat/pySickle_team3                            
 Please report bugs at adnane.nemri@csiro.au                                
 Licence: GNU General public licence version 3                              
============================================================================

This script generates a report on a single end fastq file before and after changes were made to it, eg
by a quality trimming software. For the comparison to be meaningful, the second file should be inherited from the first one.
The output is stored in a file specified by the user.

Note: the program does not read fastq files of paired-end reads.

dependencies: BioPython

usage: `python fastq_compare.py <quality_coding> <fastq_before> <fastq_after> <outfile>`



options:
   quality_coding         phred33 for Sanger and Illumina reads produced with CASAVA 1.8+
                          phred64 for Illumina reads produced with CASAVA 1.3+
                          solexa for Solexa reads

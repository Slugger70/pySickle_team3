#!/usr/bin/env python


from __future__ import division
import sys
import Bio.SeqIO


def read_fastq(fastqFile, qFormat):
    """
    Read the fastq file given as argument
    Calculate average base quality score
    Output the number of reads in that file, the average 
    base quality score of those sequences,
    and their average length
    """

    readScores = []
    readLengths = []

    for readNumber, read in enumerate(Bio.SeqIO.parse(fastqFile, qFormat)):
        
        readID = read.id
        readSeq = read.seq
        
        # If the sequence is of length 0, skip to next sequence in file
        if len(readSeq) == 0:
            continue

        readScoreList = read.letter_annotations["phred_quality"]
        # Get the average base quality score for this sequence
        readScoreAvg = sum(readScoreList) / len(readScoreList)
        
        readScores.append(readScoreAvg)
        readLengths.append(len(readSeq))

        #print readID, len(readSeq), readScoreAvg

    avgScore = sum(readScores) / len(readScores)
    avgLength = sum(readLengths) / len(readLengths)
    
    return str(readNumber + 1), str(round(avgScore, 2)), str(round(avgLength, 2))


def write_report(in_data, out_data, reportPath):
    """
    Takes the path of the report to be written
    Takes the data from input and output read of FASTQ files
    Write that data to the report file
    """
    
    # test
    reportFile = open(reportPath, 'w')
    
    in_readNum, in_avgScore, in_avgLength = in_data
    out_readNum, out_avgScore, out_avgLength = out_data

    reportFile.write("FASTQ trimming report\n\n")
    reportFile.write("FastqFile \t Read# \t AvgScore \t AvgLength\n")
    reportFile.write("Before \t" + in_readNum + " \t " + in_avgScore + " \t " + in_avgLength + "\n")
    reportFile.write("After \t" + out_readNum + " \t " + out_avgScore + " \t " + out_avgLength + "\n")
    reportFile.close()

#
# Run the script
#
if len(sys.argv) == 5:
    # fastq file path before trim
    before_fastq = sys.argv[1]
    # fastq file path after trim
    after_fastq = sys.argv[2]
    # format of the fastq file
    fastqFormat = sys.argv[3]
    # path of the log file to be written
    reportPath = sys.argv[4]

    # Allowed fastq format, and the corresponding code to give to SeqIO
    allowedFormats = {'phred33' : 'fastq',
                      'phred64' : 'fastq-illumina',
                      'solexa' : 'fastq-solexa'}

    # Make sure the format is known
    try:
        assert fastqFormat in allowedFormats
    except AssertionError as e:
        print "The format type has to be one of the following", allowedFormats
        print e
        
    #in_readNum, in_avgScore, in_avgLength =  read_fastq(in_fastq)
    #out_readNum, out_avgScore, out_avgLength = read_fastq(out_fastq)

    # The function read_fastq() is called on the BEFORE and AFTER trim fastq files
    # and the path of the output is also given 
    write_report(read_fastq(before_fastq, allowedFormats[fastqFormat]),
                 read_fastq(after_fastq, allowedFormats[fastqFormat]),
                 reportPath)
else:
    print "usage: `python fastq_compare.py BEFORE.fq AFTER.fq <quality_coding> <outfile>`"
    print "options for quality_coding:"
    print "phred33 : Sanger and Illumina reads produced with CASAVA 1.8+"
    print "phred64 : Illumina reads produced with CASAVA 1.3+"
    print "solexa  : Solexa reads"


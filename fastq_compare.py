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
    in_fastq = sys.argv[1]
    out_fastq = sys.argv[2]
    fastqFormat = sys.argv[3]
    reportPath = sys.argv[4]

    allowedFormats = {'phred33' : 'fastq',
                      'phred64' : 'fastq-illumina',
                      'solexa' : 'fastq-solexa'}

    try:
        assert fastqFormat in allowedFormats
    except AssertionError as e:
        print "The format type has to be one of the following", allowedFormats
        print e
        
    #in_readNum, in_avgScore, in_avgLength =  read_fastq(in_fastq)
    #out_readNum, out_avgScore, out_avgLength = read_fastq(out_fastq)

    write_report(read_fastq(in_fastq, allowedFormats[fastqFormat]),
                 read_fastq(out_fastq, allowedFormats[fastqFormat]),
                 reportPath)
else:
    print "usage: `python fastq_compare.py BEFORE.fq AFTER.fq <quality_coding> <outfile>`"

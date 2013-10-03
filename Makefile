# %  : the variable name
# $< : the input file
# $@ : the output file

# Rule 'all' which is a make keyword
# wildcard: look for anything .fasta in the directory
# 	for each of those .fasta files, create a NAME.png
#	file
all: $(patsubst %.fasta, %.png, $(wildcard *.fasta))

# Keeps all the intermediate files generated in the process,
# and not only the 
.PRECIOUS: %.fasta %.fasta.aln %.phy

# Another keyword, used to 
clean:
	echo "CLEAN the directory\n"
	rm -f *.aln *.phy *.reduced *.new *.png

# Step1: Run the alignment
%.fasta.aln: %.fasta
	echo "STEP 1\n"
	muscle -in $< -out $@

# Step2: Convert from fasta alignment to phy alignment
%.phy: %.fasta.aln
	echo "STEP 2\n"
	python -c "import Bio.AlignIO; Bio.AlignIO.convert('$<', 'fasta', '$@', 'phylip-relaxed')"

# Step3: create the newick tree
%.new: %.phy
	echo "STEP 3\n"
	rm -f RAxML_*
	raxmlHPC -m GTRCAT -n $< -p 10000 -s $<
	mv RAxML_result.$< $@

# Step4: Create an .png image
%.png: %.new draw_tree.py
	echo "STEP 4\n"
	python draw_tree.py $< $@

# Automated BLAST Search Tool
# This Python script performs a BLAST search using BioPython.
# It sends a DNA sequence to the NCBI BLAST server and retrieves the top matching sequences.
# The program displays important information such as accession number, organism name,alignment length, and E-value for the best matches.
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Import module to run BLAST search from NCBI
from Bio.Blast import NCBIWWW

# Import module to read and parse BLAST result files
from Bio.Blast import NCBIXML

# Import SeqIO to read biological sequence files like FASTA
from Bio import SeqIO

# Read the DNA sequence from a FASTA file named sequence.fasta
record = SeqIO.read("sequence.fasta", "fasta")
# Store the DNA sequence in a variable
sequence = record.seq

# Print message to indicate BLAST search is starting
print("Running BLAST search... Please wait")

# Send the DNA sequence to NCBI BLAST server
# "blastn" = nucleotide BLAST
# "nt" = nucleotide database
result_handle = NCBIWWW.qblast("blastn", "nt", sequence)


# Create a file named blast_result.xml to store BLAST results
with open("blast_result.xml", "w") as out_handle:
    
    # Write the BLAST result data into the XML file
    out_handle.write(result_handle.read())


# Close the connection to the BLAST result
result_handle.close()

# Open the saved BLAST result XML file
result_handle = open("blast_result.xml")

# Parse the XML file to extract BLAST information
blast_record = NCBIXML.read(result_handle)

# Print heading for output results
print("\nTop 5 Matches:\n")

# Loop through the first 5 alignments (best matches)
for alignment in blast_record.alignments[:5]:

    # Print accession number of the matched sequence
    print("Accession Number:", alignment.accession)

    # Print organism name or description of the matched sequence
    print("Organism / Description:", alignment.hit_def)

    # Print the length of the matched sequence
    print("Alignment Length:", alignment.length)

    # Print a line separator for readability
    print("----------------------------------")

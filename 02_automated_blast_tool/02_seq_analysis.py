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
record = SeqIO.read("mycobact.fasta", "fasta")
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


#-------------------------------------------------------------------------------------------------------------------
#example output:
# Running BLAST search...

# Top Matches:

# Accession Number: PQ879405
# Organism: Homo sapiens clone I3464_MOG_3_kappa_3-15_light immunoglobulin kappa light chain mRNA, complete cds
# Length: 1182
# --------------------------------
# Accession Number: AB064131
# Organism: Homo sapiens IGK mRNA for immunoglobulin kappa light chain VLJ region, partial cds, clone:K90
# Length: 781
# --------------------------------
# Accession Number: MW176761
# Organism: Homo sapiens isolate A7_7_SR-4_LA_P2S23_Light immunoglobulin variable region mRNA, partial cds; and IGKV3-15*01, IGKJ2*01, and IGKC mRNAs, complete sequence
# Length: 642
# --------------------------------
# Accession Number: MW176709
# Organism: Homo sapiens isolate A2_2_CI-3_LA_P12S3_2_Light immunoglobulin variable region mRNA, partial cds; and IGKV3-15*01, IGKJ2*01, and IGKC mRNAs, complete sequence
# Length: 648
# --------------------------------
# Accession Number: MW176951
# Organism: Homo sapiens isolate C8_32_CI-7_LA_P9S3_9_Light immunoglobulin variable region mRNA, partial cds; and IGKV3-15*01, IGKJ2*01, and IGKC mRNAs, complete sequence
# Length: 651
# --------------------------------

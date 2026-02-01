# Import SeqIO module from Biopython
# SeqIO is used to read sequence files like FASTA
from Bio import SeqIO

# Import Counter from collections module
# Counter helps count how many times each amino acid appears
from collections import Counter


# SeqIO.parse reads the FASTA file record by record
# "sequence.fasta" → input file name
# "fasta" → file format
for record in SeqIO.parse("sequence.fasta", "fasta"):

    # Convert the sequence object into a string
    # This makes it easy to count amino acids
    seq = str(record.seq)

    # Calculate the length of the protein sequence
    length = len(seq)

    # Print total length of the sequence
    print("Length:", length)

    # Count occurrence of each amino acid in the sequence
    # Example: {'A':10, 'G':5, 'L':8}
    aa_count = Counter(seq)

    # Print protein ID (taken from FASTA header)
    print("Protein ID:", record.id)

    # Heading for amino acid composition output
    print("\nAmino Acid Composition:")

    # Loop through amino acids in alphabetical order
    for aa in sorted(aa_count):

        # Calculate percentage of each amino acid
        # (count of AA / total length) × 100
        percent = (aa_count[aa] / length) * 100

        # Print amino acid and its percentage
        print(f"{aa}: {percent:.2f}%")

# sample output:
# Length: 109
# Protein ID: AAA40590.1

# Amino Acid Composition:
# A: 7.34%
# C: 5.50%
# D: 2.75%
# E: 6.42%
# F: 1.83%
# G: 7.34%
# H: 2.75%
# I: 2.75%
# K: 0.92%
# L: 15.60%
# M: 3.67%
# N: 6.42%
# P: 4.59%
# Q: 8.26%
# R: 4.59%
# S: 5.50%
# T: 2.75%
# V: 5.50%
# W: 1.83%
# Y: 3.67%



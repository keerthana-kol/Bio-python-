# Import SeqIO module from Biopython
# Used to read and process FASTA sequence files
from Bio import SeqIO


# Parse the FASTA file record by record
# "sequence.fasta" → input protein sequence file
# "fasta" → file format
for record in SeqIO.parse("sequence.fasta", "fasta"):

    # Convert the sequence object to string format
    seq = str(record.seq)

    # Calculate total length of the protein sequence
    length = len(seq)


    # ---------- Condition 1: Sequence length check ----------
    # If the sequence length is less than 100 amino acids,
    # it is considered too short for reliable analysis
    if length < 100:
        print(record.id, "Removed: Too short")
        continue   # Skip this sequence and move to the next one


    # ---------- Condition 2: Ambiguous residue check ----------
    # Count how many times 'X' appears in the sequence
    # 'X' represents unknown or ambiguous amino acids
    x_percent = (seq.count("X") / length) * 100

    # If ambiguous residues are more than 5%,
    # the sequence is considered low quality
    if x_percent > 5:
        print(record.id, "Removed: Too many ambiguous residues")
        continue   # Skip this sequence


    # If the sequence passes all validation checks,
    # it is suitable for further analysis like BLAST
    print(record.id, "Suitable for downstream analysis")

# _________________________________________
#   sample output:1
# AAA40590.1 Suitable for downstream analysis
#    sample output:2



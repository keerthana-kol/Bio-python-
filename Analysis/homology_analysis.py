# Loop through the top 5 BLAST alignments
# blast_record.alignments[:5] → selects first 5 homologs
for alignment in blast_record.alignments[:5]:

    # Select the first HSP (High Scoring Pair) for each alignment
    # HSP contains alignment details like identity, e-value, matches
    hsp = alignment.hsps[0]

    # hit_def contains the full description of the matched protein
    title = alignment.hit_def


    # ---------- Organism name extraction ----------
    # Organism name is usually written inside square brackets [ ]
    # Example: protein kinase [Homo sapiens]

    start = title.find("[")   # Find position of '['
    end = title.find("]")     # Find position of ']'

    # If both '[' and ']' are found, extract organism name
    if start != -1 and end != -1:
        organism = title[start+1:end]   # Extract text inside brackets
        organisms.append(organism)      # Store organism name in list
    else:
        organism = "Unknown"             # If organism not found


    # ---------- Identity calculation ----------
    # identities → number of matching residues
    # align_length → total alignment length
    # Identity (%) = (identities / alignment length) × 100
    identity = (hsp.identities / hsp.align_length) * 100


    # ---------- Printing BLAST result ----------
    print("Protein:", title)
    print("E-value:", hsp.expect)        # Lower E-value = better match
    print("Identity:", identity, "%")
    print("---------------------------")


# ==================================================
# CONSERVED REGION ANALYSIS (Top hit only)
# ==================================================

print("\n===== CONSERVED REGION =====\n")

# Select the best alignment (top BLAST hit)
top_alignment = blast_record.alignments[0]

# Select the first HSP from the top alignment
top_hsp = top_alignment.hsps[0]

# Print first 60 residues of:
# query sequence, match line, and subject sequence
# This shows conserved regions visually
print(top_hsp.query[0:60])
print(top_hsp.match[0:60])
print(top_hsp.sbjct[0:60])


# ==================================================
# EVOLUTIONARY HINT BASED ON ORGANISM DIVERSITY
# ==================================================

print("\n===== EVOLUTIONARY HINT =====\n")

# Count number of unique organisms found in top BLAST hits
unique_count = len(set(organisms))

print("Number of different organisms found:", unique_count)

# Interpret evolutionary conservation based on organism diversity
if unique_count >= 5:
    print("The protein is highly conserved across multiple species.")
elif unique_count >= 3:
    print("The protein shows conservation among related species.")
else:
    print("The protein may be species specific.")



# ===== CLOSEST HOMOLOGS =====

# Protein: hypothetical protein SPAB_05093 [Salmonella enterica subsp. enterica serovar Paratyphi B str. SPB7]
# E-value: 0.0
# Identity: 100.0 %
# ---------------------------
# Protein: multiphosphoryl transfer protein 2 [Salmonella enterica subsp. enterica serovar Dublin str. CT_02021853] >gb|EDZ11505.1| multiphosphoryl transfer protein 2 [Salmonella enterica subsp. enterica serovar Saintpaul str. SARA29] >gb|PQB14623.1| Phosphoenolpyruvate-protein phosphotransferase of PTS system [Salmonella enterica subsp. enterica serovar Muenchen] >emb|VGM89195.1| Phosphoenolpyruvate-protein phosphotransferase of PTS system [Salmonella enterica subsp. enterica serovar Stanley]
# E-value: 0.0
# Identity: 99.87937273823884 %
# ---------------------------
# Protein: phosphoenolpyruvate--protein phosphotransferase [Salmonella enterica] >gb|EAA3946719.1| phosphoenolpyruvate--protein phosphotransferase [Salmonella enterica subsp. enterica serovar Paratyphi B var. L(+) tartrate +] >gb|EDU8716872.1| phosphoenolpyruvate--protein phosphotransferase [Salmonella enterica subsp. enterica] >gb|MBJ4718743.1| phosphoenolpyruvate--protein phosphotransferase [Salmonella enterica subsp. enterica serovar Anatum] >gb|MKZ21772.1| phosphoenolpyruvate--protein phosphotransferase [Salmonella enterica subsp. enterica serovar Enteritidis] >tpg|HCC0126039.1| phosphoenolpyruvate--protein phosphotransferase [Salmonella enterica subsp. enterica serovar Paratyphi B]
# E-value: 0.0
# Identity: 99.87937273823884 %
# ---------------------------
# Protein: General PTS family, enzyme I [Salmonella enterica subsp. enterica serovar Paratyphi C str. RKS4594]
# E-value: 0.0
# Identity: 99.75874547647769 %
# ---------------------------
# Protein: multiphosphoryl transfer protein 2 [Salmonella enterica subsp. enterica serovar Newport str. SL317]
# E-value: 0.0
# Identity: 99.75874547647769 %
# ---------------------------

# ===== CONSERVED REGION =====

# MEFTCELPNGVHARPASHVETLCNTFTSQIEWHNLRTDRKGSAKSALALIGTDTLAGDHC
# MEFTCELPNGVHARPASHVETLCNTFTSQIEWHNLRTDRKGSAKSALALIGTDTLAGDHC
# MEFTCELPNGVHARPASHVETLCNTFTSQIEWHNLRTDRKGSAKSALALIGTDTLAGDHC

# ===== EVOLUTIONARY HINT =====

# Number of different organisms found: 5
# The protein is highly conserved across multiple species.

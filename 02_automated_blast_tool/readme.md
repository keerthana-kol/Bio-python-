Automated BLAST Search Tool:
Project Overview:

This project is a Python-based tool that performs an automated sequence similarity search using the Basic Local Alignment Search Tool (BLAST) provided by the National Center for Biotechnology Information.
The program reads a DNA sequence from a FASTA file, sends it to the NCBI BLAST server, and retrieves the top matching sequences from the nucleotide database.
The results include important information such as accession number, organism name, and alignment details.

Features:

Reads DNA sequence from a FASTA file
Performs BLAST search automatically
Retrieves top sequence matches
Displays accession number
Displays organism name / sequence description
Saves BLAST results as XML file

Technologies Used:

Python
BioPython
NCBI BLAST database

Project Structure
blast_project/
│
├── blast_script.py      # Python script for running BLAST search
├── sequence.fasta       # Input DNA sequence file
├── blast_result.xml     # BLAST output file
├── README.md            # Project documentation
└── requirements.txt     # Required Python libraries

How to Run the Project:

Install BioPython
pip install biopython

Place your DNA sequence in sequence.fasta

Run the Python script

python blast_script.py

The program will perform the BLAST search and display the top matches.

Output:
The program displays:

Accession Number
Organism / Description
Alignment Length

The complete BLAST result is saved in blast_result.xml.

Learning Outcome:

This project demonstrates:
Basic bioinformatics sequence analysis
Accessing biological databases programmatically

Using BioPython for biological data processing

Automating BLAST searches using Python

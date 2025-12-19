# FASTA Analyzer

A Python script to analyze DNA sequences from FASTA files.  
It validates sequences, calculates their length, base composition (A, T, G, C), and GC content percentage.  
Results are saved into a CSV file for easy viewing and downstream analysis.

---

## Features
- Reads multi‑sequence FASTA files
- Validates sequences using regex (`^[ATGC]+$`)
- Calculates:
  - Sequence length
  - Base composition (A, T, G, C counts)
  - GC content percentage
- Outputs results into a clean CSV file

---

## Project Structure
FASTA-Analyzer/ 
│ 
├── sequence_multi.fasta   # Example FASTA input file
├── fasta_analyzer.py      # Main Python script 
├── sequence_multi.csv     # Output CSV file 
|── README.md              # Project documentation


---

## 🛠️ Requirements
- Python 3.x
- No external libraries required (uses built‑in `re` and `csv` modules)

---

## Usage
1. Clone the repository:
   bash
   git clone https://github.com/pijushrkmvm-spec/FASTA-Analyzer.git
   cd FASTA-Analyzer
   
2. Run the script
   python fasta_analyzer.py

---

## Learning GoalsThis project was part of my Python learning pathway:
 
- Practicing file handling
- Using regex for validation
- Working with lists and CSV output
- Applying bioinformatics concepts (GC content)

---

## Future Improvements- Add motif search (e.g., ATG start codon, TATA box) (Upcoming...)
- Support protein FASTA files
- Build a simple command‑line interface (CLI)

---

## AuthorPijush Chakraborty
M.Sc. Bioinformatics student | Python learner | Interested in bioinformatics tools and automation

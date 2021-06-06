from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import translate
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import argparse
import io
import os

#translate a batch of CDS in fasta format.  This script takes an argument -- gene name -- and formats it to receive the output from his blast pipeline (genename.seq.tblastn.blastdb.fa) and outputs a translated fasta

parser = argparse.ArgumentParser()
parser.add_argument("entry", help="name of gene given to original blast scripts")
parser.add_argument("database")
parser.add_argument("addseq")
args = parser.parse_args()
cwd = os.getcwd()

print("add_translations.py script is using {} as entry".format(args.entry))
print("add_translations.py script is using {} as database".format(args.database))
filename = cwd + "/genomes/" + str(args.database)

output = cwd + "/" + str(args.entry) + "/" + str(args.entry) + ".parse.merged.fa"
print(output)

output2 = cwd + "/" + str(args.entry) + "/merged_coding.txt"
print(output2)


for seq_record in SeqIO.parse(filename, "fasta"):
	if args.addseq == seq_record.id:
		save_file = open(output, 'a')
		save_file.write('>')
		save_file.write(seq_record.id)
		save_file.write('\n') #line break
		save_file.write(str((translate(seq_record.seq))))
		save_file.write('\n')
		save_file = open(output2, 'a')
		save_file.write('\n')
		save_file.write(seq_record.id)
		save_file.write('\t')
		save_file.write(args.database)
		print("Found add_seq! " + args.addseq)
		print(seq_record.description)
		print(seq_record.translate())
		exit()
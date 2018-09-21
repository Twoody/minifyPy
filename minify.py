import sys
import re

def minify(mFile, nFile):
	nLines = ""
	with open(nFile, 'w') as outfile, open(mFile, 'r', encoding='utf-8') as infile:
		for line in infile:
			line = line.replace('\n', ' ').replace('\r', '').replace('\t', ' ')
			line = re.sub(r'\s+', ' ', line)
			line = line.strip()
			if line == " ":
				continue
			nLines += line
		outfile.write(nLines)
	print("\t***** minify.py  *****")
	print("\tCREATED NEW FILE:")
	print("\t\t" + nFile)
	print("\t**********************")
	return True

if __name__ == "__main__":
	mFile = sys.argv[1] 		#Get file target from cmd line
	nFile = mFile + '.new'	#New file we will write to
	minify(mFile, nFile)

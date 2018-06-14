import argparse

parser = argparse.ArgumentParser(description='Process log file, generate and plot csv file')

#functions
parser.add_argument('-c', action='store_true', help='generate processed csv file')#generate csv
parser.add_argument('-g', action='store_true', help='generate graph')#generate graph

#files
parser.add_argument('-i', dest='log', type=argparse.FileType('r'), help='log file')#, required=True)#open log file as read
parser.add_argument('-o' , dest='csv', type=argparse.FileType('r+'), help='csv file', required=True)#open csv file as read + write (prevents wipe file)
#parser.add_argument('-t', type=argparse.FileType('r+'))

#program version
parser.add_argument('-version', action='version', version='%(prog)s 0.20')

args = parser.parse_args()
#print(args)

#functions definition
def generateGraph(csvFile):
	print('received file to generate graph: ' + str(csvFile))
	'''print('--- file begin --- ')
	with csvFile as csv:
		print csv.read()
		#csv.write('\n  new')
	print('--- file end ---')'''
	return

def generateCsv(logFile, csvFile):
	print('received files to generate csv: '+ str(logFile) + str(csvFile))
	
	'''print('--- file begin --- ')
	with logFile as log:
		print log.read()
	print('--- file end ---')'''

	'''print('--- file begin --- ')
	with csvFile as csv:
		print csv.read()
		#csv.write('\n  new')
	print('--- file end ---')'''
	return

#functions
if(args.c):#generate csv file
	if((args.log) and (args.csv)):
		generateCsv(args.log, args.csv)

if(args.g):#generate graph
	if(args.csv):
		if(args.csv.closed):#reopens csv file if closed by previous function
			with open(args.csv.name) as args.csv:
				generateGraph(args.csv)
		else:#if file is open
			generateGraph(args.csv)

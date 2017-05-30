#!/usr/bin/env python

import sys
import sam2gfa
import sys,getopt,      \
csv,time         

__title__ = 'SAM2GFA'
__version__ = '1.0'
__description__ = "SAM to GFA converter"
__author__ = 'Hamza Khan'
__license__ = 'MIT License,'
__author_email__ = "hamza.khan@alumni.ubc.ca"

epi = "By %s, %s <%s>\n\n" % (__author__,
__license__,
__author_email__)
__doc__ = "\n***********************************************\
************************************\
\n %s v%s - %s \n**********************************\
***********************************************\
**\n%s" % (__title__,
__version__,
__description__,
epi)


def usage():
    print("\nUsage: python dga.py\
 -i <inputfile> \n")
    sys.exit(2)


def main(argv):
    
   #Checking if no input has been provided 
   if(len(argv)==0):
        print('\nERROR!:No input provided\n')
        usage()

   
   #Try and Catch block for handling input errors
   try:
      opts, args = getopt.getopt(argv,"h:i:",["help=","ifile="])
      
   except getopt.GetoptError:
      print(__doc__)
      usage()

   #Check whether the mandatory files are given as inputs  
   short_opts = [i[0] for i in opts]
   if(('-i') not in short_opts):
       print ("ERROR: Missing inputs. Please provide -i .")
       usage()
   
   #Reading user inputs
   for opt, arg in opts:
      if opt == '-h':
         print(__doc__)
         usage()

      elif opt in ("-i", "--ifile"):
         inputfile = arg

                
   print(__doc__,'Input file is %s\n' \
 %( inputfile))
   print( '----------------------------------------\nRunning Script\n--------------\
--------------------------\n')
   
   #Variable to record time 
   start_time = time.time() 


   f = sam2gfa.sam_parser(inputfile)   
   success = f.read_sam_file()  
    
   if(success):
       print ('Done! Time elapsed: %.4f seconds' % (time.time() - start_time))


if __name__ == "__main__":
   main(sys.argv[1:])

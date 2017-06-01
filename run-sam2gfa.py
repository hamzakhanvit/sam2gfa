#!/usr/bin/env python

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


try:
    import sys
    import sam2gfa
    import sys,getopt,      \
    csv,time

except ImportError:
    print ('One of the required packages is not installed. Check pre-reqs')


def usage():
    print("\nUsage: python run-sam2gfa.py\
 -i <SAMfile> \n\n Extra Options:\n\n -d --detail\tDetailed GFA. Contains sequences as well.\
\n\n -h --help\tHelp option\n\n -r --ref\tReference FASTA. Recommend when using the --detail option\n\n\
-s --sub\tSubject FASTA file. Recommended when using the --detail option\n")
    sys.exit(2)


def main(argv):
    
   #Checking if no input has been provided 
   if(len(argv)==0):
        print('\nERROR!:No input provided\n')
        usage()

   
   #Try and Catch block for handling input errors
   try:
      opts, args = getopt.getopt(sys.argv[1:],'h:i:r:s:d',['help=','ifile=','ref=','sub=','detail',])
      
   except getopt.GetoptError:
      print(__doc__)
      usage()

   #Check whether the mandatory files are given as inputs  
   short_opts = [i[0] for i in opts]

   if(('-i') not in short_opts and ('--ifile') not in short_opts):
       print ("ERROR: Missing inputs. Please provide -i .")
       usage()
   
   if (('-d') in short_opts or ('--detail') in short_opts) and ((('-s') not in short_opts and ('--sub') \
not in short_opts) or (('-r') not in short_opts) and ('--ref') not in short_opts):
       print ('Please provide reference and subject FASTA files when using --detail option\n')
       usage()

   detail=False
   reference=''
   subject=''
   
   #Reading user inputs
   for opt, arg in opts:
      if opt in ("-h", "--help"):
          print(__doc__)
          usage()
 
      elif opt in ("-d", "--detail"):
          detail = True

      elif opt in ("-i", "--ifile"):
          inputfile = arg

      elif opt in ("-r", "--ref"):
          reference = arg

      elif opt in ("-s", "--sub"):
          subject = arg

                
   print(__doc__,'Input file is %s\n' \
 %( inputfile))
   print( '----------------------------------------\nReading inputs\n--------------\
--------------------------\n')
   
   #Variable to record time 
   start_time = time.time() 
   f = sam2gfa.sam_parser(inputfile,detail, reference, subject) 
   #success = f.read_sam_file()  
   success = f.write_gfa_file()
    
   if(success):
       print ('Done! Time elapsed: %.4f seconds' % (time.time() - start_time))


if __name__ == "__main__":
   main(sys.argv[1:])

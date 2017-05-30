import gfapy, pysam

class sam_parser(object):

     def __init__(self, filename):
         self.filename = filename
         
     
     def read_sam_file(self):
         '''
         Reads a SAM file
         '''
         samfile = pysam.AlignmentFile(self.filename, "r")

         print ("\tAll query names:\n===================\n")
         #Print all query names in the SAM file
         #print(samfile.query_name()) 

         return 1          
    

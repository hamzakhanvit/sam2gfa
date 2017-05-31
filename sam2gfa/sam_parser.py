import gfapy
from collections import defaultdict
from simplesam import Reader, Writer

class sam_parser(object):

     def __init__(self, filename):
         self.filename = filename
         
     
     def read_sam_file(self):
         '''
         Reads a SAM file
         '''
         in_file = open(self.filename, 'r')
         in_sam = Reader(in_file)
         sam_dict = defaultdict(dict)         

         print ("\tAll query names:\n===================\n")
         #Print all query names in the SAM file
         for x in in_sam:
             sam_dict[x.qname]['rname'] = x.rname
             sam_dict[x.qname]['pos'] = x.pos
             sam_dict[x.qname]['seq'] = x.seq
             sam_dict[x.qname]['qual'] = x.qual
             sam_dict[x.qname]['cigar'] = x.cigar
             sam_dict[x.qname]['gapped_seq'] = x.gapped('seq')
             sam_dict[x.qname]['flag'] = x.flag
             sam_dict[x.qname]['mapped'] = x.mapped
             sam_dict[x.qname]['duplicate'] = x.duplicate
             sam_dict[x.qname]['secondary'] = x.secondary
             sam_dict[x.qname]['tags'] = x.tags

             #print("x.qname=",x.qname)
             #print("x.rname=",x.rname)
             #print("x.pos=",x.pos)
             #print("x.seq=",x.seq)
             #print("x.qual=",x.qual)
             #print("x.cigar=",x.cigar)
             #print("x.gapped('seq')=",x.gapped('seq'))
             #print("x.flag=",x.flag)
             #print("x.mapped=",x.mapped)
             #print("x.duplicate=",x.duplicate)
             #print("x.secondary=",x.secondary)
             #print("x.tags=",x.tags)
         #print(sam_dict)

         return sam_dict          


     def write_gfa_file(self):
         '''
         Write a GFA file for the given SAM file
         '''
         sam_dict = self.read_sam_file()
         print(sam_dict)
        
         out = open('output.gfa','w')
         out.write('H\tVN:Z:1.0')
         return 1 

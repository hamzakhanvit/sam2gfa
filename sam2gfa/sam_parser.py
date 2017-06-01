try:
    from Bio import SeqIO
    import gfapy, time
    from collections import defaultdict, OrderedDict
    from simplesam import Reader, Writer
    from .spinner import spinner
    from pprint import pprint

except ImportError:
    print ('One of the required packages is not installed. Check pre-reqs')

class sam_parser(object):

     def __init__(self, filename, detail, reference, subject):
         self.filename = filename
         self.detail = detail
         self.reference = reference
         self.subject = subject
         #self.segments = OrderedDict(dict)       
         self.segments={}        
         

     def read_sam_file(self):
         '''
         Reads a SAM file and constructs a dictionary out 
         of it
         (SAMfile)->(dict)
         '''
         in_file = open(self.filename, 'r')
         in_sam = Reader(in_file)
         sam_dict = defaultdict(dict)         
         self.segments = in_sam.header

         print ("\t\t\t\tProcessing\n\t\t\t===========================\n")
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
             sam_dict[x.qname]['length']=len(x.seq)
            
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
         #pprint(in_sam.header) 
         return sam_dict          


     def read_reference(self):
        '''
        Read reference fasta file and create ref_dict
        (file)->(dict)
        '''
        ref_dict = {}
        with open(self.reference, "rU") as handle:
            for record in SeqIO.parse(handle, "fasta"):
               id = record.id
               seq = record.seq.tostring()
               ref_dict[id]=seq
        return(ref_dict)

 
     def read_subject(self):
        '''
        Read subject fasta file and create sub_dict
        (file)->(dict)
        ''' 
        sub_dict={}
        with open(self.subject, "rU") as handle:
            for record in SeqIO.parse(handle, "fasta"):
               id = record.id
               seq = record.seq.tostring()
               sub_dict[id]=seq
        return(sub_dict)


     def write_gfa_file(self):
         '''
         Write a GFA file for the given SAM file
         '''
         sam_dict = self.read_sam_file()

         out = open('output.gfa','w')
         out.write('H\tVN:Z:1.0\n')

         if(self.detail):
            ref_dict = self.read_reference()
            sub_dict = self.read_subject()
            print("Generating detailed GFA")
            spin = spinner()
            spin.start()
            #some long-running operations
            #time.sleep(3) 
            
            #Write reference headers in GFA file
            for key in self.segments['@SQ']:
                temp = '\t'.join(self.segments['@SQ'][key])
                out.write("S\t%s\t%s\t%s\n"%(key[3:],ref_dict[key[3:]],temp))
               
            #Write subject headers in GFA file
            for key in sam_dict:          
                out.write("S\t%s\t%s\t%s\n"%(key,sub_dict[key],temp))
            
            #Write links in GFA
            for key in sam_dict:
                if(sam_dict[key]['flag']==0): flag_sub='+' 
                elif(sam_dict[key]['flag']==16): flag_sub='-'
                else: flag_sub='*'
                 
                out.write("L\t%s\t+\t%s\t%s\t%s\n"%(sam_dict[key]['rname'],key,flag_sub,sam_dict[key]['cigar']))    
            
            spin.stop()

         else:
            print("Generating GFA")
            spin = spinner()
            spin.start()
            #some long-running operations
            #time.sleep(3)

            #Write reference headers in GFA file
            for key in self.segments['@SQ']:
                temp = '\t'.join(self.segments['@SQ'][key])
                out.write("S\t%s\t*\t%s\n"%(key[3:],temp))

            #Write subject headers in GFA file
            for key in sam_dict:
                out.write("S\t%s\t*\tLN:i:%d\n"%(key,sam_dict[key]['length']))
              
            #Write links in GFA
            for key in sam_dict:
                if(sam_dict[key]['flag']==0): flag_sub='+'
                elif(sam_dict[key]['flag']==16): flag_sub='-'
                else: flag_sub='*'

                out.write("L\t%s\t+\t%s\t%s\t%s\n"%(sam_dict[key]['rname'],key,flag_sub,sam_dict[key]['cigar']))

            spin.stop()            


         return 1 

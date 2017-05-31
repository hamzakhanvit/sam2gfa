import sam2gfa, pkg_resources
from collections import defaultdict

def test_sam_parser():
     inputfile =  pkg_resources.resource_filename('sam2gfa', 'data/output.sam')
     f = sam2gfa.sam_parser(inputfile, False, '', '')   
     success = f.read_sam_file()
     #success = f.write_gfa_file() 
     assert type(success) is defaultdict


def test_gfa_writer():
     inputfile =  pkg_resources.resource_filename('sam2gfa', 'data/output.sam')
     f = sam2gfa.sam_parser(inputfile, False, '', '')
     success = f.write_gfa_file() 
     assert success == 1 


import sam2gfa, pkg_resources

def test_sam_parser():
     inputfile =  pkg_resources.resource_filename('sam2gfa', 'data/output.sam')
     f = sam2gfa.sam_parser(inputfile)   
     success = f.read_sam_file() 
     assert success == 1

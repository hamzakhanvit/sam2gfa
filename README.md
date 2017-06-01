# SAM2GFA
A tool to convert a SAM file to a GFA 1.0 file
        
 ![Build Status](https://travis-ci.org/hamzakhanvit/sam2gfa.svg?branch=master)
(Under development)
   
## Installation Instruction

```
git clone git@github.com:hamzakhanvit/sam2gfa.git
cd sam2gfa
python setup.py install
```    
      
## Getting Started
```       
Usage: run-sam2gfa.py [-i|--ifile SAMfile] [-d|--detail] [-r|--ref REF_FASTA] 
[-s|--sub SUB_FASTA] [-h| --help]
        
 Mandatory options:

 -i --ifile	Path to Input SAM file 
 

 Other options:

 -d --detail	Detailed GFA. Contains sequences as well.

 -h --help	Help option

 -r --ref	Reference FASTA. Recommend when using the --detail option

 -s --sub	Subject FASTA file. Recommended when using the --detail option
        
      
Output:
    
 output.gfa

```

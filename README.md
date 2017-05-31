# SAM2GFA
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
Usage: run-sam2gfa.py -i <SAMfile> 
        
 Mandatory option:

 -i --ifile	Input SAM file

 Extra Options:

 -d --detail	Detailed GFA. Contains sequences as well.

 -h --help	Help option

 -r --ref	Reference FASTA. Recommend when using the --detail option

 -s --sub	Subject FASTA file. Recommended when using the --detail option
        
      
Output:
    
 output.gfa

```

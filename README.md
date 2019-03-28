## **PhyloSignal (Literman and Schwartz, 2019)**  
#### This GitHub repo contains all the necessary scripts to run analyses from *Literman and Schwartz* (2019)

#### **Software Requirements** (Manuscript Version):
* Python3 (3.6.1)  
* Bowtie2 (2.3.4)  
* Samtools (1.3.1)  
* BBMap Suite (37.40)  
* Genome assembler of your choosing (Ray - 2.3.2-devel)  
* R (3.5.3)  
* FastQC (0.11.5)

#### **Data Requirements:**
1) Approximate genome size estimate for group  
* Note: If genome size estimates vary greatly within your group, use an estimate on the larger side    

2) Raw or Trimmed NGS reads for each taxa  
* SISRS default parameters require 3X depth to call a site, so higher per-taxa coverage is ideal. In the associated manuscript, we required 20X coverage per taxa. The pipeline can be run with less, but site recovery will become  reduced as coverage drops.
* All read files should be of the same 'type' (e.g. Don't mix DNA-seq + RNA-seq)
* Ensure high sequence data quality prior to analysis (low read quality and high sequence duplication levels are both red flags for analysis). Scripts are provided to run FastQC.


3) Reference genome (.fasta) with associated annotations (.bed)

#### **Instructions for Running Scripts**

##### 1) Clone Repo locally
```
cd /home
git clone https://github.com/BobLiterman/Literman_PhyloSignal.git
```
* Repo contains:  
  * All necessary scripts
  * Base folder architecture for a SISRS run and subsequent analyses
  * Empty Taxon ID file

##### 2) Set up folder structure using folder_setup.py
* In the main directory (e.g. /home/Literman_PhyloSignal/) edit the included blank text file (TaxonIDs), adding each of your taxon IDs on a new line.  
  * Note: Six-letter taxon IDs may be easier to work with (e.g. HomSap vs. Homo_sapiens)
* folder_setup.py will create taxon folders in the RawReads, TrimReads, and SISRS_Run directories

```
> cd /home/Literman_PhyloSignal
> cat TaxonIDs

AotNan
CalJac
ColAng
GorGor
HomSap
HylMol
MacMul
MacNem
PanPan
PanTro
PapAnu
PapCyn

> python scripts/folder_setup.py TaxonIDs
```

##### 3) If starting from raw (untrimmed) NGS reads, and trimming with our wrapper...  
Trimming can certainly be done using your preferred methods, but we provide a wrapper script for the BBDuk program (part of the BBMap Suite).  

If your reads are already trimmed, place all read files into the appropriate taxon folder in TrimReads.  

  * Multiple read files per taxon is fine, as are mixes of single-end and paired-end reads.

To use our wrapper:

* 1) Put all raw reads in (**.fastq.gz format**) in the appropriate taxon folder in RawReads.  
  * Multiple read files per taxon is fine, as are mixes of single-end and paired-end reads.
* 2) Run trim script, which will trim all reads in RawReads and output trimmed reads to the TrimReads directory (and runs FastQC on both sets)  

```
python scripts/read_trimmer.py
```  

##### !!! Data Check !!!
* Before continuing, **check FastQC output** for trimmed data. If using 'random' DNA-seq data, be especially wary of **high sequence duplication levels** which could indicate non-random sequencing.
* Data will eventually be pooled, so **best to remove low-quality data early** to prevent it from being incorporated into the genome assembly

##### 4) Once all trimmed data is in place and QC'd, samples are pooled and then subset for composite genome assembly. 

#!/bin/sh
python SCRIPT_DIR/get_alignment.py TWOTAXA SISRS_DIR COMPOSITE_DIR

python SCRIPT_DIR/filter_nexus_for_missing.py SISRS_DIR/alignment_bi.nex MISSING
python SCRIPT_DIR/filter_nexus_for_missing_nogap.py SISRS_DIR/alignment_bi.nex MISSING

grep -oe "SISRS_[^/]*" SISRS_DIR/alignment_bi_locs_mMISSING.txt | uniq -c | sort -k1 -nr | awk '{print $2}' > SISRS_DIR/alignment_bi_locs_mMISSING_Clean.txt
grep -oe "SISRS_[^/]*" SISRS_DIR/alignment_bi_locs_mMISSING_nogap.txt | uniq -c | sort -k1 -nr | awk '{print $2}' > SISRS_DIR/alignment_bi_locs_mMISSING_nogap_Clean.txt

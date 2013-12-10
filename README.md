transcriptionmatcher
====================

This is a little python script explicitly made for Notes from Nature transcription outputs. 
It will open Notes from Nature transcription output files provided in .csv format from Zooniverse, read the header, ask for a field, and then, for each "subject_id" (basically, for each image), look at all transcriptions for that image, and generate an average "matching score" (and standard deviation) for all pairwise comparisons.

Usage:  python transcriptionmatcher5.py

Outputs right now go to STDOUT but could easily be sent to an output file.

# Basic instructions

The scripts in this folder copy the files from an original Clevrer format dataset into a format
supported by DCL.

Requires: 
- Videos
- Questions and answers
- Annotations
- Objects masks and attributes => are used for the proposals

Command:

./prepare_dataset.sh original_clevrer_path dcl_clevrer_path


There are other modifications required:
- Download parsed_programs from https://drive.google.com/drive/folders/1dydkLN1A9GWTaMK8QaxpWs6Pt4Eszsaw?usp=sharing
 and correctly set --correct_question_path '../clevrer/parsed_program'\
- 
# iCn3D scrapper and annotator

This project is part of the [Protein Codeathon at ISMB 2022](https://sites.google.com/view/codeathonismb2022), and is mainly creating some useful python and/or node.js scripts to:- <br>
(i) annotate protein residue, including post-translational modifications (PTMs) and 3D domain; <br>
(ii) scrap the existing information, including the interactions and distance table 

Table of Contents
====================
- [Introduction](#introduction)
- [Methodology](#methodology)
- [Result](#result)
- [Next steps](#next-steps)
- [Team members](#team-members)

## Introduction
iCn3D is a web-based molecular structure visualizing interactive tool, which can also be accessed programmatically using NodeJS script. There are a few protein annotations available in the current version of iCn3D, such as SNPs, ClinVar, conserved domains, functional sites, 3D domains, interactions, disulfide bonds and cross linkages. In order to extracting the result for a large set of 3D structure, users can use either Python or Node.js scripts. Hence, we focus on creating some user-friendly python scripts to ease running a bulk analysis. Additionally, some novel annotations, 3D domain and post-translational modifications (PTMs) are now added to improve the protein annotation function in iCn3D. 

## Methodology
### Workflow 

### iCn3D scrapper for existing information - interactions and distance table
by Raphael Trevizani, Li Chuin Chong <br>
In order to download interactions and distance table automatically while dealing with large set of 3D structure, two python scripts are created using selenium and chromedriver.   

### Novel annotation to iCn3D - PTMs & 3D domain
by Sachendra Kumar, Jiyao Wang


## Result
### iCn3D scrapper for existing information - interactions and distance table
- Scrapper script for interactions: [download_interactions.py](https://github.com/hackathonismb/scripts-to-protein-residue-annotations/tree/main/interactions) <br>
  Example output: <br>
  For more details, please visit the [`interaction` sub-directory](https://github.com/hackathonismb/scripts-to-protein-residue-annotations/tree/main/interactions).
  
- Scrapper script for distance table: [iCn3D_scapper_forDistance.py] <br>
  Example output: <br>
  For more details, please visit the `distance-table` sub-directory.

### Novel annotation to iCn3D - PTMs & 3D domain
- Annotator script for PTMs: [PTMsite_annotation_inputfile_prep.py](https://github.com/hackathonismb/scripts-to-protein-residue-annotations/blob/main/PTM_annotation/PTMsite_annotation_inputfile_prep.py) <br>
  Example output:  <br>
  For more details, please visit the `PTM_annotation` sub-directory.
  
- Annotator script for 3D domain: [annotation.js](https://github.com/hackathonismb/scripts-to-protein-residue-annotations/blob/main/nodejs/annotation.js) <br>
  Example output: <br>
  For more details, please visit the `domain_annotation` sub-directory.

## Next steps 
Scrapper: expand this functionality to all other menus <br>
Annotator: 

## Team members
Jiyao Wang (Team Lead) <br>
Li Chuin Chong (Writer) <br>
Sachendra Kumar (Writer) <br>
Raphael Trevizani <br> 
David Enoma <br>
Jack Lin 

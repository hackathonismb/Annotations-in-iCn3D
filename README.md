# iCn3D scrapper and annotator

This project is part of the [Protein Codeathon at ISMB 2022](https://sites.google.com/view/codeathonismb2022), and is mainly creating some useful python and/or node.js scripts to:- <br>
(i) add annotatation of protein residue, especially post-translational modifications (PTMs); <br>
(ii) scrap the existing information, including the 3d domain, interactions and distance table 

Table of Contents
====================
- [Introduction](#introduction)
- [Methodology](#methodology)
- [Result](#result)
- [Next steps](#next-steps)
- [Team members](#team-members)

## Introduction
iCn3D is a web-based molecular structure visualizing interactive tool, which can also be accessed programmatically using NodeJS script. There are a few protein annotations available in the current version of iCn3D, such as SNPs, ClinVar, conserved domains, functional sites, 3D domains, interactions, disulfide bonds and cross linkages. In order to extracting the result for a large set of 3D structure, users can use either Python or Node.js scripts. Hence, we focus on creating some user-friendly python/node.js scripts to ease running a bulk analysis. Additionally, novel PTMs annotation is now added to improve the protein annotation function in iCn3D. 

## Methodology
### Workflow
Scrapper - From UI to Data

(i) 3d domain annotation <br>
![image](https://user-images.githubusercontent.com/51225708/178833917-0c725473-1be2-4c79-af95-8decc9cb1870.png)

(ii) interaction <br>
![image](https://user-images.githubusercontent.com/51225708/178836993-521c7348-394f-42b7-89c7-abf034584bd2.png)

(iii) distance table <br>
![image](https://user-images.githubusercontent.com/51225708/178837175-6a24bd4c-b2a4-4351-84ea-57ccc56f57a2.png)

Annotator - PTMs <br>
![image](https://user-images.githubusercontent.com/51225708/178837410-34b1128f-5f7a-4be9-bc5b-9d49967f7910.png)

### iCn3D scrapper for existing information - 3d domain, interactions and distance table
by Jiyao Wang, Raphael Trevizani, Li Chuin Chong <br>
In order to download 3d domain, interactions and distance table automatically from UI, a node.js is created for former annotation while two python scripts are created for latter annotations using selenium and chromedriver.   

### Novel annotation to iCn3D - PTMs
by Sachendra Kumar
The input PTMs files were prepared using the downloaded PTMs sites information for Acetylation, Methylation, Phosphorylations, Sumoylation, and Ubiquitination from PhosphoSitePlus database using python script. 
For example, Header: UniprotId,PTMaa,PTMpos,Metadata and its associated  data Data: Q12888,T,100,https://www.phosphosite.org/siteAction.action?id=31887780For proof of the concept, we did custom annotation for PTMs in iCn3D for user input based annotation.

## Result
### iCn3D scrapper for existing information - 3d domain, interactions and distance table
- Scrapper script for 3D domain: [annotation.js](https://github.com/hackathonismb/Annotations-in-iCn3D/blob/main/3d_domain_annotation/annotation.js) <br>
  Example output: <br>
  For more details, please visit the [`3d_domain_annotation` sub-directory](https://github.com/hackathonismb/Annotations-in-iCn3D/tree/main/3d_domain_annotation).
  
- Scrapper script for interactions: [download_interactions.py](https://github.com/hackathonismb/Annotations-in-iCn3D/blob/main/interactions/download_interactions.py) <br>
  Example output: [1enh_line_graph.json](https://github.com/hackathonismb/Annotations-in-iCn3D/blob/main/interactions/1enh_line_graph.json) <br>
  For more details, please visit the [`interaction` sub-directory](https://github.com/hackathonismb/scripts-to-protein-residue-annotations/tree/main/interactions).
  
- Scrapper script for distance table: [iCn3D_scapper_forDistance.py](https://github.com/hackathonismb/Annotations-in-iCn3D/blob/main/distance_table/iCn3D_scapper_forDistance.py) <br>
  Example output: [distance_table_7JMO.csv](https://github.com/hackathonismb/Annotations-in-iCn3D/blob/main/distance_table/distance_table_7JMO.csv) <br>
  For more details, please visit the [`distance_table` sub-directory](https://github.com/hackathonismb/Annotations-in-iCn3D/tree/main/distance_table).

### Novel annotation to iCn3D - PTMs & 3D domain
- Annotator script for PTMs: [PTMsite_annotation_inputfile_prep.py](https://github.com/hackathonismb/Annotations-in-iCn3D/blob/main/PTM_annotation/PTMsite_annotation_inputfile_prep.py) <br>
  Example output: [Processed_Phosphorylation.csv](https://github.com/hackathonismb/Annotations-in-iCn3D/blob/main/PTM_annotation/Processed_Phosphorylation.csv) <br>
  For more details, please visit the [`PTM_annotation` sub-directory](https://github.com/hackathonismb/Annotations-in-iCn3D/tree/main/PTM_annotation). <br>
  For the preliminary study, we processed PTMs annotation sites for Acetylation (48279), Methylation (20554), Phosphorylations (378481), Sumoylation (8832), and Ubiquitination (126051) to annotate in iCn3D using node.js script.

## Next steps 
Scrapper: expand this functionality to all other menus <br>
Annotator: implementing the PTMS annotation using node.js script and add novel annotations, such as somatic mutations (COSMIC database), PTMs Glycosylation, Succinylations, and automating using REST API interface.

## Team members
Jiyao Wang (Team Lead), National Center for Biotechnology Information (NCBI), USA <br>
Li Chuin Chong (Writer), TWINCORE GmbH, Germany <br>
Sachendra Kumar (Writer), Indian Institute of Science, India <br>
Raphael Trevizani, IEDB and Fiocruz, Brazil <br> 
Jack Lin

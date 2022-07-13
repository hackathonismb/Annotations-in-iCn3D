# Download interactions
### Developed by: Raphael Trevizani, Jiyao Wang
#### Please open any issues on Github


## How it works:
- Download interactions uses the selenium to automatically downloads the interactions from molecules loaded in iCn3D. You may run the headless version (using Firefox) or the non-headless version (using Google Chrome/Chromium).

## Requirements:
- Python 3 
- Headless: Firefox with geckodriver
- Non-headless: Chrome
- selenium
- webdriver-manager

## Instalation: 
- pip install selenium
- pip install webdriver-manager

## Usage:
### Input  
- Run:
```
python download_interactions.py
```
- Edit config.py accordingly. 
- You can set the following variables:
- headless: True of False. Headless mode uses Firefox and non-headless uses Chrome. E.g.:
```
headless = True
```
- pdb: PDB code of the molecule to be loaded. May be capitalized or not. E.g.:
```
pdb = '1enh'
```
- download_dir: Path of directory where the downloaded file will be saved. Must be the full path. E.g.:
```
download_dir = '/home/your_user_name/Downloads'
```
- select_first_set: Name of the molecule on the left menu. E.g.:
```
select_first_set  = 'proteins'
```
- select_first_set: Name of the molecule the right menu. E.g.:
```
select_second_set = 'water'
```
- file_format: Format of the output file. May be png, svg, json. E.g.:
```
file_format = 'png' 
```

Use the exact names of the molecules as they appear in the interactions menu (proteins, water, etc). If you do not input a valid path where to save the downloaded file, the system default will be used. Please, make sure to follow python syntax for strings, ie, use equal sign and quotes for the value (variable = 'value', except for headless, which must be True or False). 

- To download the interactions between pdb code: 1ENH and water in JSON format to your Downloads folder, the following config.py should be used:
```
pdb  = '1enh'
download_dir = '~/Downloads'
select_first_set  = 'proteins'
select_second_set = 'water'
file_format = 'json' 
```
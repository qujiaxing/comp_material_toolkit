# Computational Materials Toolkit

# AMSET parser
Prepare run.py files for transport calculations of [AMSET](https://hackingmaterials.lbl.gov/amset)

1. Have the input calculated properties ready, set in the folder tree of: 
  - Band gap: `densekp/material_folder/`
  - Elastic tensor: `elastic/material_folder/`
  - Electronic dielectric constant: `dielectric_electronic/material_folder/`
  - Ionic dielectric constant: `dielectric_ionic/material_folder/`
  - Effective phonon frequency: `phonon_frequency/material_folder/`
  - AMSET run set-up: `amset/material_folder`
  
2. For each material, copy `run_automate.py' to 'amset/material_folder'
3. Run AMSET calculations:
`python run_automate.py`

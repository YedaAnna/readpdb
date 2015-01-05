import os
import sys
import glob
global ligand
molecule_list=[]
molecule_list=glob.glob(os.getcwd() +'/*.pdb')# read all the molecules in a directory and adds them to a list
for index in molecule_list:
	print "start of molecule: " + os.path.basename(index)
	ligand=[]
	chain=[]
	lig_name=[]
	resolution=0
	ligand_file= open(index, 'r')
	for line in ligand_file:
		column = line.split()
    		if column[0] == "HET":
      			ligand.append(column[1])
      			chain.append(column[2])
    		if column[0] == "HETNAM":
			if column[1].isdigit()==False:
				name_part = column[2]			
			else:
				name_part_two = column[3]
				lig_name.append(name_part+name_part_two)
    		if column[0]=='REMARK':
			if column[1]=='2':
				if len(column)>2:
					if column[2] =='RESOLUTION.':
						resolution=column[3]	
	print "RESOLUTION of pdb is " + str(resolution) + " Angstroms"                
	print "list of ligands present:" + str(ligand)
	print "corresponding chains are:" + str(chain)
	print "Ligand name is " + str(lig_name)
	ligand_file.close()
	print "End of molecule: " + os.path.basename(index) +"\n\n"
print "End of program"

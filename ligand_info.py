# @filename:ligand_info.py
# @usage: python ligand_info.py >& ligand_info.txt
# @author: YedaAnna
# @description: Gives the list of ligands(Hetrogens) in a pdb file
# @tags:ligand, pdb
# @version: 1.0
# @date: Wed Jan 07 2015
import os
import glob
from collections import OrderedDict
import time
global ligand
start_time = time.time()


def HETROGEN():
    global unique_no, unique, pdb_file
    unique_no = 0
    pdb_file = open(index, 'r')
    for line in pdb_file:
        column = line.split()
        if column[0] == "HET":
            ligand.append(column[1])
            chain.append(column[2])
    print "list of ligands present:" + str(ligand)
    print "corresponding chains are:" + str(chain)
    unique = list(OrderedDict.fromkeys(ligand))
    unique_no = len(unique)
    print "List of unique ligands are : " + str(unique)
    pdb_file.close()


def RESOLUTION():
    global resolution
    resolution = 0
    pdb_file = open(index, 'r')
    for line in pdb_file:
        column = line.split()
        if column[0] == 'REMARK':
            if column[1] == '2':
                if len(column) > 2:
                    if column[2] == 'RESOLUTION.':
                        resolution = column[3]
    print "RESOLUTION of pdb is " + str(resolution) + " Angstroms"
    pdb_file.close()


def LIGAND_NAME():
    pdb_file = open(index, 'r')
    for line in pdb_file:
        column = line.split()
        if column[0] == 'HETNAM':
            if column[1] in unique:
                global temp
                joined = ' '.join(column[2:])
                lig_name.append(joined)
                temp = column[2]
            else:
                if column[1] == '3':
                    continue
                lig_name.remove(temp)
                joined2 = ' '.join(column[3:])
                temp2 = temp + joined2
                lig_name.append(temp2)
    print "Corresponding ligand name is : " + str(lig_name)
    pdb_file.close()


def basic_info():
    HETROGEN()
    LIGAND_NAME()
    RESOLUTION()

molecule_list = []
# read all the molecules in a directory and adds them to a list
molecule_list = glob.glob(os.getcwd() + '/*.pdb')
for index in molecule_list:
    print "start of molecule: " + os.path.basename(index)
    ligand = []
    chain = []
    lig_name = []
    basic_info()
    print "End of molecule: " + os.path.basename(index) + "\n\n"
print "End of program"
print "time taken: " + str(time.time() - start_time) + "seconds"

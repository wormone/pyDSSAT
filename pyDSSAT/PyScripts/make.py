#!/usr/bin/env python

import os

# Compile DSSAT
os.system('rm ../src/*.o ../src/*.mod')
os.chdir('../src')
os.system('make -f Make_CSM046.MAK')

# Compile the fortran interface file Call_CSM.f90
os.system(' gfortran -fPIC -w -ffixed-form -fd-lines-as-comments -ffixed-line-length-none -c Call_CSM.f90')

# Create signature file
cmd = 'f2py Call_CSM.f90 -h example.pyf -m example --overwrite-signature'
os.system(cmd)

# Create driver library
cmd = 'f2py -c example.pyf *.o'
os.system(cmd)

os.system('mkdir ../../Test')
os.system('cp example.so ../../Test')
os.system('cp ../PyScripts/DSSAT_LIBRARY.py ../../Test')
os.system('cp ../PyScripts/DSSAT_GUI.py ../../Test')
os.system('cp ../PyScripts/DSSAT_test.py ../../Test')

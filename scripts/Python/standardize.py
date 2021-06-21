# coding: utf-8
import pubchempy
import sys

with open(sys.argv[1]) as inhandle, open(sys.argv[1] + '_standardized', 'w') as success_handle, open(sys.argv[1] + '_failed', 'w') as fail_handle:
    for line in inhandle.readlines():
        id_, smiles = line.split('\t')
        try:
            c = pubchempy.get_compounds(smiles, 'smiles')[0]
            succ_out = '\t'.join([id_, c.isomeric_smiles]) + '\n'
            print('succ_out: ' + succ_out, end='')
            success_handle.write(succ_out)
        except Exception as e:
            fail_out = '\t'.join([id_, smiles, str(e)]) + '\n'
            print('fail_out: ' + fail_out, end='')
            fail_handle.write(fail_out)

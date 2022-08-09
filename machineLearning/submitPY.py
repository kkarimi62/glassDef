if __name__ == '__main__':
	
        import sys
	
        import os
	
        import numpy as np
	#---
	
        lnums = [ 31, 8 ]
        string=open('machineLearning.py').readlines() #--- python script
	#---
        times=np.arange(5,100,5)  #--- run GetFrames(lmpData,times=lmpData.coord_atoms_broken.keys())
        count = 0
        for itime in times:
	    
            inums = lnums[ 0 ] - 1
	    
            string[ inums ] = "\t\'6\':\'MlTrain/granular/itime%s',\n" % (itime) #--- change job name
	    
            inums = lnums[ 1 ] - 1
 	    
            string[ inums ] = "\tconfParser.set(\'parameters\',\'itime\',\'%s\')\n"%(itime)

	    
            sfile=open('junk%s.py'%count,'w');sfile.writelines(string);sfile.close()
	    
            os.system( 'python3 junk%s.py'%count )
	    
            os.system( 'rm junk%s.py'%count )
	    
            count += 1

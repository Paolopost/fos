import h5py
import sys
import os.path as op
from fos import *
import numpy as np

a=np.loadtxt(op.join(op.dirname(__file__), "..", "data", "rat-basal-forebrain.swc") )

pos = a[:,2:5].astype( np.float32 )
radius = a[:,5].astype( np.float32 ) * 4

# extract parent connectivity and create full connectivity
parents = a[1:,6] - 1
parents = parents.astype(np.uint32).T
connectivity = np.vstack( (parents, np.arange(1, len(parents)+1) ) ).T.astype(np.uint32)

#colors = np.random.random( ( (len(connectivity)/2, 4)) )
#colors[:,3] = 1.0

colors = np.random.rand( len(connectivity), 4, 500 ).astype( np.float32 )

colors[:,3] = 1.0

w = Window( dynamic = True )

scene = Scene( scenename = "Main" )
act = DynamicSkeleton( name = "Neuron",
                vertices = pos,
                connectivity = connectivity,
                connectivity_colors=colors) #, radius = radius)

scene.add_actor( act )
w.add_scene( scene )
w.refocus_camera()

act.play()
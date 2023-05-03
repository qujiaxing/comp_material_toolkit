from pymatgen.io.vasp.outputs import Outcar, Vasprun
import json

class parse():

    def __init__(self):
        #self.dir = dir
        self.settings = {'scattering_type': ['IMP', 'ADP', 'POP'],
                        'doping': [-100000000000000.0,
                        -1000000000000000.0,
                        -1e+16,
                        -5e+16,
                        -1e+17,
                        -5e+17,
                        -1e+18,
                        -2.5e+18,
                        -5e+18,
                        -7.5e+18,
                        -1e+19,
                        -2.5e+18,
                        -5e+19,
                        -7.5e+19,
                        -1e+20,
                        -2.5e+20,
                        -5e+20],
                        'temperatures': [800],
                        'bandgap': 0,
                        'interpolation_factor': 10,
                        'deformation_potential': 'deformation.h5',
                        'elastic_constant': [[0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0]],
                        'high_frequency_dielectric': [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                        'static_dielectric': [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                        'pop_frequency': 0,
                        'write_mesh': True}
        

    def get_elastic_constant(self, dir):
        
        outcar_elastic = Outcar(dir +'OUTCAR')
        outcar_elastic.read_elastic_tensor()
        elastic_tensor = outcar_elastic.data['elastic_tensor']
        self.settings['elastic_constant'] = elastic_tensor
    
    def get_high_frequency_dielectric(self, dir):
        outcar_dielectric = Outcar(dir +'OUTCAR')
        high_frequency_dielectric = outcar_dielectric.as_dict()['dielectric_tensor']
        self.settings['high_frequency_dielectric'] = high_frequency_dielectric
    
    def get_static_dielectric(self, dir1,dir2):
        outcar_dielectric = Outcar(dir1 +'OUTCAR')
        ep1 = outcar_dielectric.as_dict()['dielectric_tensor']
        outcar_ionic = Outcar(dir2 +'OUTCAR')
        ep2 = outcar_ionic.as_dict()['dielectric_ionic_tensor']

        static_dielectric = [[ep1[i][j] + ep2[i][j]  for j in range(len(ep1[0]))] for i in range(len(ep2))]

        self.settings['static_dielectric'] = static_dielectric

    def get_bandgap(self, dir):
        vasprun = Vasprun(dir +'vasprun.XML')
        self.settings['bandgap'] = vasprun.eigenvalue_band_properties[0]

    def get_phonon_frequency(self, dir):
        fo = open(dir + "/output", "r")
        line = fo.readlines()
        self.settings['phonon_frequency'] = frequency = line[-1].split(" ")[1]

    












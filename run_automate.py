import warnings
import sys
from amset.core.run import Runner
from amset.plot.rates import RatesPlotter

warnings.simplefilter("ignore")

sys.path.append('../../../')

import parse_property

file_dir = '../../../'

# change directory containing OUTCAR
composition = 'Bi2Pt'
setting_parser = parse_property.parse()


# update high_frequency_dielectric
setting_parser.get_high_frequency_dielectric(file_dir+'dielectric-electronic/{}/'.format(composition))
print('dielectric-electronic parsed')

# update static_frequency_dielectric
#setting_parser.get_static_dielectric(file_dir+'dielectric-electronic/{}/'.format(composition),
#                                     file_dir+'dielectric-ionic/{}/'.format(composition))
#print('dielectric-static parsed')


# update bandgap 
setting_parser.get_bandgap(file_dir+'densekp/{}/'.format(composition))
print('band gap parsed')



# update phonon frequecy
setting_parser.get_phonon_frequency(file_dir+'phonon_frequency/{}/'.format(composition))
print('phonon_frequency parsed')



# update elastic_constant
setting_parser.get_elastic_constant(file_dir+'elastic/{}/'.format(composition))
print('elastic_constant parsed')





if __name__ == "__main__":
    runner = Runner.from_vasprun("vasprun.xml.gz", setting_parser.settings)
    amset_data = runner.run()

    plotter = RatesPlotter(amset_data)
    plt = plotter.get_plot()
    plt.savefig("rates.png", bbox_inches="tight", dpi=400)

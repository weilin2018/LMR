

from datetime import datetime, timedelta

# =============================================================================
# Section 1: High-level parameters of reconstruction experiment
# =============================================================================

# Name of reconstruction experiment
#nexp = 'p1_CCSM4_LastMillenium_ens100_allAnnualProxyTypes_pf0.5'
#nexp = 'p1_CCSM4_PiControl_ens100_allAnnualProxyTypes_pf0.5'
#nexp = 'p1_CCSM4_PiControl_ens50_allAnnualProxyTypes_pf0.5'
#nexp = 'p1_MPIESMP_LastMillenium_ens100_allAnnualProxyTypes_pf0.5'
#nexp = 'p1_20CR_ens100_allAnnualProxyTypes_pf0.5'
#nexp = 'p1_ERA20C_ens100_allAnnualProxyTypes_pf0.5'
#nexp = 'ReconMultiState_CCSM4_PiControl_ens500_allAnnualProxyTypes_pf0.5'
nexp = 'test'

# set the absolute path the experiment (could make this cwd with some os coding)
#LMRpath = '/home/chaos2/wperkins/data/LMR'
LMRpath = '/home/disk/ekman/rtardif/kalman3/LMR'

# set clean_start to True to delete existing files in the outpout directory (otherwise they will be used as the prior!)
clean_start = True
#clean_start = False

# Reconstruction period (years)
#recon_period = [1500,2000]
#recon_period = [1850,2000]
recon_period = [1800,2000]
#recon_period = [1000,2000]

# Ensemble size
#Nens = 50
Nens = 100
#Nens = 500

# Fraction of available proxy data (sites) to assimilate 
# (=1.0 for all, 0.5 for half etc.)
#proxy_frac = 0.1
#proxy_frac = 0.25
#proxy_frac = 0.5
proxy_frac = 0.75
#proxy_frac = 1.0

# Number of Monte-Carlo iterations
iter_range = [0,100]

# Localization radius for DA (in km)
locRad = None
#locRad = 2000.0
#locRad = 10000.0

# =============================================================================
# Section 2: PROXIES
# =============================================================================

# Proxy data directory & file
datadir_proxy    = LMRpath+'/data/proxies'
datafile_proxy   = 'Pages2k_DatabaseS1-All-proxy-records.xlsx'
dataformat_proxy = 'CSV'

#regions = ['Arctic','Europe','Australasia']
#regions = ['Europe']
regions = ['Antarctica','Arctic','Asia','Australasia','Europe','North America','South America']

# Define proxies to be assimilated
# Use dictionary with structure: {<<proxy type>>:[... list of all measurement tags ...]}
# where "proxy type" is written as "<<archive type>>_<<measurement type>>"
# DO NOT CHANGE FORMAT BELOW
proxy_assim = {
    '01:Tree ring_Width': ['Ring width','Tree ring width','Total ring width','TRW'],
    '02:Tree ring_Density': ['Maximum density','Minimum density','Earlywood density','Latewood density','MXD'],
    '03:Ice core_d18O': ['d18O'],
    '04:Ice core_d2H': ['d2H'],
    '05:Ice core_Accumulation':['Accumulation'],
    '06:Coral_d18O': ['d18O'],
    '07:Coral_Luminescence':['Luminescence'],
    '08:Lake sediment_All':['Varve thickness','Thickness','Mass accumulation rate','Particle-size distribution','Organic matter','X-ray density'],
    '09:Marine sediment_All':['Mg/Ca'],
    '10:Speleothem_All':['Lamina thickness'],
    }

# Proxy temporal resolution (in yrs)
#proxy_resolution = [1.0,5.0]
proxy_resolution = [1.0]

# Source of calibration data (for PSM)
datatag_calib = 'GISTEMP'
#datatag_calib = 'HadCRUT'
#datatag_calib = 'BerkeleyEarth'
datadir_calib = LMRpath+'/data/analyses'

# Threshold correlation of linear PSM 
PSM_r_crit = 0.2

# =============================================================================
# Section 3: MODEL (PRIOR)
# =============================================================================

# Prior data directory & model source
prior_source     = 'ccsm4_last_millenium'
datafile_prior   = '[vardef_template]_CCSM4_past1000_085001-185012.nc'

#prior_source     = 'ccsm4_preindustrial_control'
#datafile_prior   = '[vardef_template]_CCSM4_piControl_080001-130012.nc'

#prior_source     = 'mpi-esm-p_last_millenium'
#datafile_prior   = '[vardef_template]_MPI-ESM-P_past1000_085001-185012.nc'

#prior_source     = '20cr'
#datafile_prior   = '[vardef_template]_20CR_185101-201112.nc'

#prior_source     = 'era20c'
#datafile_prior   = '[vardef_template]_ERA20C_190001-201212.nc'


datadir_prior    = LMRpath+'/data/model/'+prior_source
dataformat_prior = 'NCD'

# Define variables in state vector (will be updated by assimilation)
#state_variables = ['tas_sfc_Amon']
#state_variables = ['tas_sfc_Amon', 'zg_500hPa_Amon']
state_variables = ['tas_sfc_Amon', 'zg_500hPa_Amon', 'AMOCindex_Omon']

# =============================================================================
# Section 4: OUTPUT
# =============================================================================

# Run time output
#datadir_output  = '/home/disk/kalman3/rtardif/LMR/output/wrk'
#datadir_output  = '/home/disk/ekman/rtardif/nobackup/LMR/output'
datadir_output  = '/home/disk/ice4/hakim/svnwork/python-lib/trunk/src/ipython_notebooks/data'
#datadir_output = '/home/chaos2/wperkins/data/LMR/output/working'

# Archive directory
#archive_dir = '/home/disk/kalman3/rtardif/LMR/output'
archive_dir = '/home/disk/kalman3/hakim/LMR/'
#archive_dir = '/home/chaos2/wperkins/data/LMR/output/archive'
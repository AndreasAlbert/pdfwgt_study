from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = '@NAME'
config.General.workArea = '/afs/cern.ch/work/a/aalbert/public/2019-08-15_vht_crab/wdir/1'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '@PSET'

config.Data.outputPrimaryDataset = '@NAME'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 4000
NJOBS = 250  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/mc/vht' % (getUsernameFromSiteDB())
config.Data.publication = False 
config.Data.outputDatasetTag = 'RunIIFall17'

config.Site.storageSite = 'T2_CH_CERNBOX'
config.JobType.numCores = 1
config.JobType.allowUndistributedCMSSW = True
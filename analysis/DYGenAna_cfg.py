#import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("Test")

# setup 'analysis'  options
options = VarParsing.VarParsing ('analysis')

# setup any defaults you want
options.outputFile = 'analyzed.root'
options.inputFiles = 'file:step0.root'
options.maxEvents = -1

# get and parse the command line arguments
options.parseArguments()


process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.MessageLogger.cerr.threshold = 'INFO'
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.load("PhysicsTools.HepMCCandAlgos.genParticles_cfi")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    generator = cms.PSet(
        initialSeed = cms.untracked.uint32(123456789),
        engineName = cms.untracked.string('HepJamesRandom')
    )
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string(options.outputFile)
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )

process.source = cms.Source("PoolSource")
process.source.fileNames = cms.untracked.vstring(options.inputFiles)


import FWCore.ParameterSet.Config as cms

process.genZBoson = cms.EDFilter("CandViewShallowCloneProducer",
  src = cms.InputTag("genParticles"),
  cut = cms.string(" abs(pdgId)==23 && (status==3 || status==62) ")
)

process.genLeptons = cms.EDFilter("CandViewShallowCloneProducer",
  src = cms.InputTag("genParticles"),
  cut = cms.string(" ( (11==abs(pdgId)) | (abs(pdgId) == 13)) && status==1")
)


process.dilepton = cms.EDProducer("CandViewShallowCloneCombiner",
     decay = cms.string("genLeptons@+ genLeptons@-"),
    #  checkCharge = cms.bool(True),
     cut = cms.string("60.0 < mass < 120.0"),
     roles = cms.vstring('lep1', 'lep2')
)


process.plotGenZBoson= cms.EDAnalyzer(
    "CandViewHistoAnalyzer",
    src = cms.InputTag("genZBoson"),							   
    histograms = cms.VPSet(
        cms.PSet(
            min = cms.untracked.double(0.0),
            max = cms.untracked.double(1000.0),
            nbins = cms.untracked.int32(100),
            name = cms.untracked.string("z_pt"),
            description = cms.untracked.string("Z p_{T} (GeV)"),
            plotquantity = cms.untracked.string("pt")
        ),
        cms.PSet(
            min = cms.untracked.double(0.0),
            max = cms.untracked.double(200.0),
            nbins = cms.untracked.int32(100),
            name = cms.untracked.string("z_mass"),
            description = cms.untracked.string("Z mass (GeV)"),
            plotquantity = cms.untracked.string("mass")
        ),
    )
)

process.plotDilepton= cms.EDAnalyzer(
    "CandViewHistoAnalyzer",
    src = cms.InputTag("dilepton"),							   
    histograms = cms.VPSet(
        cms.PSet(
            min = cms.untracked.double(0.0),
            max = cms.untracked.double(1000.0),
            nbins = cms.untracked.int32(100),
            name = cms.untracked.string("dilepton_pt"),
            description = cms.untracked.string("dilepton p_{T} (GeV)"),
            plotquantity = cms.untracked.string("pt")
        ),
        cms.PSet(
            min = cms.untracked.double(0.0),
            max = cms.untracked.double(200.0),
            nbins = cms.untracked.int32(100),
            name = cms.untracked.string("dilepton_mass"),
            description = cms.untracked.string("dilepton mass (GeV)"),
            plotquantity = cms.untracked.string("mass")
        ),
        cms.PSet(
            min = cms.untracked.double(-2.5),
            max = cms.untracked.double(2.5),
            nbins = cms.untracked.int32(5),
            name = cms.untracked.string("dilepton_charge"),
            description = cms.untracked.string("Dilepton charge"),
            plotquantity = cms.untracked.string("charge")
        ),
        cms.PSet(
            min = cms.untracked.double(-2.5),
            max = cms.untracked.double(2.5),
            nbins = cms.untracked.int32(5),
            name = cms.untracked.string("dilepton_charge"),
            description = cms.untracked.string("Dilepton charge"),
            plotquantity = cms.untracked.string("charge")
        ),
        cms.PSet(
            min = cms.untracked.double(-2.5),
            max = cms.untracked.double(2.5),
            nbins = cms.untracked.int32(5),
            name = cms.untracked.string("dilepton_daughter1_pdg"),
            description = cms.untracked.string("Dilepton daugher 1 PDG"),
            plotquantity = cms.untracked.string("daughter(0).pdgId")
        ),
        cms.PSet(
            min = cms.untracked.double(-2.5),
            max = cms.untracked.double(2.5),
            nbins = cms.untracked.int32(5),
            name = cms.untracked.string("dilepton_daughter2_pdg"),
            description = cms.untracked.string("Dilepton daugher 2 PDG"),
            plotquantity = cms.untracked.string("daughter(1).pdgId")
        ),
    )
)




analysis = cms.Sequence(
    process.genZBoson *
    process.genLeptons *
    process.dilepton *
    process.plotGenZBoson *
    process.plotDilepton
)

process.p = cms.Path(
    process.genParticles *
    analysis
    )

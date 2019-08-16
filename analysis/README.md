# Gen-level Z plotter

Easy-to-use plotter configuration for studying gen-level Z candidates. Will produce plots both based on `pdgid==23` gen candidates, as well as for dilepton candidates formed from `status==1` electrons and muons.

To run, use:

```sh
 cmsRun DYGenAna_cfg.py inputFiles=file:/path/to/file;
```

The output histograms will be in `analyzed.root`.
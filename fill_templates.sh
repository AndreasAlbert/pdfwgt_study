GPDIR=/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.4.2/DYJets_Test_pdfwgt/


for GP in $GPDIR/*HT*nopdfwgt*.xz; do
    NAME=$(basename $GP | sed 's|_slc6.*||')_$(echo $GP | grep -oE 'CMSSW_[0-9]*_[0-9]*_[0-9]*')
    echo $NAME
    mkdir -p $NAME;
    pushd $NAME;
    cp ../crab_mc_template.py ./crab_${NAME}.py
    cp ../B2G-Run3Summer19wmLHEGS-00017_1_cfg.py ./${NAME}_cfg.py
    sed -i "s|@NAME|${NAME}|" ./crab_${NAME}.py
    sed -i "s|@NAME|${NAME}|" ${NAME}_cfg.py
    sed -i "s|@PSET|$(pwd)/${NAME}_cfg.py|" ./crab_${NAME}.py
    sed -i "s|@GRIDPACK|${GP}|" ${NAME}_cfg.py
    popd
done



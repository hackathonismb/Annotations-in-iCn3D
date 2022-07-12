/*
Please install the following three packages in your directory with the file interaction.js
npm install three
npm install jquery
npm install icn3d

npm install axios
npm install querystring
*/

// https://github.com/Jam3/three-buffer-vertex-data/issues/2
global.THREE = require('three');
let jsdom = require('jsdom');
global.$ = require('jquery')(new jsdom.JSDOM().window);

let icn3d = require('icn3d');
let me = new icn3d.iCn3DUI({});

let https = require('https');
let axios = require('axios');
let qs = require('querystring');

//let utils = require('./utils.js');

let myArgs = process.argv.slice(2);
if(myArgs.length != 2) {
    // annotation types: 
    // 1: SNPs
    // 2: ClinVar
    // 3: Conserved Domains
    // 4: Functional Sites
    // 5: 3D Domains
    // 6: Interactions
    // 7: Disulfide Bonds
    // 8: Cross-Linkages
    console.log("Usage: node annotation.js [PDB ID] [annotation type as an integer]");
    return;
}

let pdbid = myArgs[0].toUpperCase(); //'6jxr'; //myArgs[0];
let annoType = myArgs[1];

let baseUrlMmdb = "https://www.ncbi.nlm.nih.gov/Structure/mmdb/mmdb_strview.cgi?v=2&program=icn3d&b=1&s=1&ft=1&bu=0&complexity=2&uid=";

let urlMmdb = baseUrlMmdb + pdbid;

https.get(urlMmdb, function(res1) {
    let response1 = [];
    res1.on('data', function (chunk) {
        response1.push(chunk);
    });

    res1.on('end', function(){
        let dataStr1 = response1.join('');
        let dataJson = JSON.parse(dataStr1);

        me.setIcn3d();
        let ic = me.icn3d;

        ic.bRender = false;
        ic.mmdbParserCls.parseMmdbData(dataJson);

        let result = ic.showAnnoCls.showAnnotations_part1();
        let nucleotide_chainid = result.nucleotide_chainid;
        let chemical_chainid = result.chemical_chainid;
        let chemical_set = result.chemical_set;        

        let chnidBaseArray = $.map(ic.protein_chainid, function(v) { return v; });
        let url2 = "https://www.ncbi.nlm.nih.gov/Structure/vastdyn/vastdyn.cgi?chainlist=" + chnidBaseArray;

        https.get(url2, function(res1) {
            let response1 = [];
            res1.on('data', function (chunk) {
                response1.push(chunk);
            });

            res1.on('end', function(){
                let dataStr = response1.join('');
                let dataJson = JSON.parse(dataStr);

                ic.chainid_seq = dataJson;
                ic.showAnnoCls.processSeqData(ic.chainid_seq);

                ic.showAnnoCls.showAnnoSeqData(nucleotide_chainid, chemical_chainid, chemical_set);

                // output annotations
                if(annoType == 5 || annoType == 6 || annoType == 7 || annoType == 8) {
                    // 5: 3D Domains
                    // 6: Interactions
                    // 7: Disulfide Bonds
                    // 8: Cross-Linkages
                    if(annoType == 5) {
                        ic.annoDomainCls.showDomainAll();
        
                        console.log(JSON.stringify(ic.domain2resid));
                    }
                    else if(annoType == 6) {
        
                    }
                    else if(annoType == 7) {
        
                    }
                    else if(annoType == 8) {
        
                    }
                }
                else {
                    // 1: SNPs
                    // 2: ClinVar
                    // 3: Conserved Domains
                    // 4: Functional Sites
                    let url3 = '';
        
                    https.get(url3, function(res1) {
                        let response1 = [];
                        res1.on('data', function (chunk) {
                            response1.push(chunk);
                        });
        
                        res1.on('end', function(){
                        let dataStr = response1.join('');
                        let dataJson = JSON.parse(dataStr);
                        //console.log("dataJson: " + dataJson.length);
        
                        
                        });
                    }).on('error', function(e) {
                        console.error("Error 2: no Epitope data...");
                    });
                }
            });
        }).on('error', function(e) {
            console.error("Error 2: no Epitope data...");
        });
    });
}).on('error', function(e) {
    console.error("Error: " + pdbid + " has no MMDB data...");
});

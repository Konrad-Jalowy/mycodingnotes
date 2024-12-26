let fs = require('fs'); 

  
fs.rm('./somefile.txt',  (err) => { 
    if(err){ 
        console.error(err.message); 
        return; 
    } 
    console.log("File deleted successfully"); 
}) 
fs.rm('./emptydir', {recursive: true},  (err) => { 
    if(err){ 
        console.error(err.message); 
        return; 
    } 
    console.log("Empty dir deleted successfully"); 
});
fs.rm('./fulldir',{recursive: true},  (err) => { 
    if(err){ 
        console.error(err.message); 
        return; 
    } 
    console.log("Full dir deleted successfully"); 
});
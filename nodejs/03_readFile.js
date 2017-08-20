var fs = require('fs');

//异步
fs.readFile('readFile_test.txt','utf-8',function(error,data) {
	console.log("异步data：",data);
});
console.log("frist \n  因为异步哦");

//同步
var data = fs.readFileSync('readFile_test.txt','utf-8');
console.log("同步data:",data);
console.log('同步要等诶');


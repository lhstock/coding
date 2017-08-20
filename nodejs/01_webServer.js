var http = require("http");
http.createServer(function(request,response) {
	response.writeHead(200,
		{
			'Content-Type':'text/html', 
			'accept-intercepted-requests':1 

		});
	response.write('<h1>this\'s a nodejs_Web </h1>')
	response.end('<p>Hello World</p>');
	}).listen(8081);
	console.log("Server running at http://127.0.0.1:8081/");
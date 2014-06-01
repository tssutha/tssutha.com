### A Quick Guide to Jump Start with NodeJs 

As I am planning to attend the [NodeSchool Singapore][link7] event next week, 15th June 2014, I have a very short period to learn and prepare something on Node.Js before the event.

I googled for some quick guide and found some great materials for an absolute beginner and I would like to share with you all. 

Here is the list of items I am working on and hope it will be helpful for others to jump start with Node.Js

1. [Node.js Succinctly][link1]
	A small 100 page e-book by SyncFusion, written in simple and easy to understand way. It leads through the fundamentals of using Node.Js, including the some flavor with express.js, socket.io and SqlLite. It won't take more than an hour to go throught every page of the book. 

2. [Nodejs.org][link2]
	Well this is an absolute minimum, every nodejs developer must have checked the home of Node.Js. Download and install the Node.Js, Will not take much time, just 5 minutes to setup.

3. Start with First Example, 
	Node.Js Succinctly book provides many basic examples to get familier with the language syntax and concepts, I guess it won't be a problem for anyone who has some previous experience with javascript or C or any other programming language. So I directly jump to first web application.
	
	
	<pre class="Dark"><code >
		//Load the Http Module
		var http = require('http');
	
	/\*
		Create the Web Server and get the request (req) and response(res) objects 
		Handle the request and response from the client 
		Call end() to close sending the response to the client 
		Call listen() with a port number to activate the listing process
	\*/
		
	http.createServer(function(req,res){
			res.writeHead(200, {'Content-Type': 'text/plain'});
			res.write('Welcome to NodeSchool Singapore');
			res.end('Hello NodeJs World\n');
		}).listen(8084,'127.0.0.1');
		
	console.log('Server Running @ http://127.0.0.1:8084/');

	</pre></code>
	
	Save as example.js and run the following command on commandline or terminal 
	
	<pre><code>
		node example.js
	</pre></code>
	
	check the output in your browser. Open the browser and type the address
	<pre><code>
		http://localhost:8084/
	</pre></code>
	
4. Handling page requests
	Extending the previous example to handle different page request from client. Check the url attribute of request object and handling the page routing accordingly.
	<pre><code>
	http.createServer(function(req,res){
	res.writeHead(200, {'Content-Type': 'text/plain'});	console.log(req.url);
	if(req.url == '/')
	{
		res.write('Welcome to NodeSchool Singapore\n');
		res.end('Hello NodeJs World\n');
	}
	else if(req.url == '/about')
	{
		res.write('This page gives everything about NodeSchool Singapore Event\n');
		res.end('Hello NodeJs World\n');
	}
	else if(req.url == '/admin')
	{
		res.write('Welcome to Admin Page\n');
		res.end('Hello NodeJs World\n');
	}
	else
	{
		res.write('Page not found\n');
		res.end('Hello NodeJs World\n');
	}
}).listen(8084,'127.0.0.1');
console.log('Server Running @ http://127.0.0.1:8084/');
	</pre></code>
	
 	To kill the server 
 <pre><code>
 	Enter Ctrl-C (Ctrl + C) in terminal
 </pre></code>
 
4. Follow these two tutorials by [Jason][link5] to extend the knowledge on Node.Js, Express.js and MongoDB
 	1. [A Sample App with Node.js, Express and MongoDB – Part 1][link3]
 	2. [A Sample App with Node.js, Express and MongoDB – Part 2][link4]
 	
 	 	
5. Here we go finally, GREAT Node.Js resource collections for beginners. Thanks to @rockbot for this great compilation. 
	[https://github.com/rockbot/node-for-beginners][link6]

[link1]: http://www.syncfusion.com/resources/techportal/ebooks/nodejs
[link2]: http://nodejs.org/
[link3]: http://blog.ijasoneverett.com/2013/03/a-sample-app-with-node-js-express-and-mongodb-part-1/

[link4]: http://blog.ijasoneverett.com/2013/04/a-sample-app-with-node-js-express-and-mongodb-part-2/
[link5]: http://blog.ijasoneverett.com/author/ijason/
[link6]: https://github.com/rockbot/node-for-beginners
[link7]: http://www.meetup.com/Singapore-JS/events/174971982/


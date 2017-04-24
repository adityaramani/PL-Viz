	var express = require('express'),
	    app = express()
			path = require('path')
			bodyParser = require('body-parser');

	var spawn = require("child_process").spawn;


	app.use(bodyParser.urlencoded({
	    extended: true
	}));
	app.use(bodyParser.json());

	app.use(express.static(path.join(__dirname, 'public')));

	app.get('/', function(request, response) {
	    response.sendFile(__dirname + '/public/html/index.html');
	    // body...
	});

	app.post('/info', function(req, res) {

			id = req.body.id
			var process = spawn('python',["summary.py" ,id]);

			process.stdout.on('data', function (data){
				jdata = JSON.parse(data.toString('utf8'))

				res.send(jdata)

			});
	})

	app.listen(8081, function() {
	    console.log("Server Running")

	})

const logger 	= require('../utils/logger');
const mongoose 	= require('mongoose');
const User 		= require('../models/user');


module.exports = async function(){

	// Override mongoose's default promise library
	mongoose.Promise = global.Promise;

	// Connect to database
	logger.verbose('Configuring database connection');
	await mongoose.connect('mongodb://127.0.0.1:27017/Fusion', {
		useMongoClient: true,
	});  

	// Log any connection errors
	mongoose.connection.on('error', (err) => {
		logger.error(err);
	});

}();
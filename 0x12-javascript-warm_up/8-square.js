#!/usr/bin/node
// prints a square

if (isNaN(process.argv[2])) {
	console.log('Missing size');
} else {
	for (let i = 0; i < parseInt(process.argv[2]); i++) {
		console.log('X'.repeat(parseint(process.argv[2])));
	}
}

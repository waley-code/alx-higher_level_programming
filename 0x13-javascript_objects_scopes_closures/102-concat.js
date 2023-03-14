#!/usr/bin/node
const fs = require('fs');

// Get the file paths from the command-line arguments
const [,, sourceFile1, sourceFile2, destFile] = process.argv;

// Read the contents of the source files
const contents1 = fs.readFileSync(sourceFile1);
const contents2 = fs.readFileSync(sourceFile2);

// Concatenate the contents
const concatenated = Buffer.concat([contents1, contents2]);

// Write the concatenated contents to the destination file
fs.writeFileSync(destFile, concatenated);

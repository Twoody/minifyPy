Tanner Lee Woody
Tanner.L.Woody@gmail.com
20180921

Running from commandline `python3 minify.py test.txt`
Output file will be `test.txt.new`.

Supports paths and will place shrunk file in same dir as input file.
For example, if we have /test/dir/foo.txt and run:
	`python3 minify.py test.txt`
, we will now have /test/dir/foo.txt.new


TODO:
	1.
		Thoughtful support on second argument for destination, that support path.
	2.
		Argument to enable spacing between lines if file is actually text file.
		For example: "This\nis\na\nsentence." --> "This is a sentence." instead of
			"thisisasentence".
	

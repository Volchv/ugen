# Testing_Skills - ugen

Whole program consist of 3 python files:
<ul>
	<li>Ugen.py – main program</li>
	<li>Testunit.py – unittests</li>
	<li>Test.py – test for main program which take test_data.txt with different scenarios as input.</li>
</ul>

<p>There are also input files needed which contains: ID, forename, middle
  name (optional), surname and department. Items in the line are separated by colons. </p>

<i>1234:Jozef:Miloslav:Hurban:Legal<BR>
4567:Milan:Rastislav:Stefanik:Defence<BR>
4563:Jozef::Murgas:Development</i>

Test_data.txt is needed for testing purposes. Format is: "input", "expected result" amd "note" divided by tab (\t) 

<i>1:John:Alan:Doe:Sales	1:jadoe:John:Alan:Doe:Sales	Good Example with middle name<BR>
1234:Mary::Smith:IT	1234:msmith:Mary::Smith:IT	Good example without middle name</i>

<b>Ugen.py</b> 
<p>Can be launch via command line : 
<i>python3 ugen.py --output my_output.txt input_file1.txt input_file3.txt</i><BR>
Accept optional parameter for output file (-o ,--output). If not provided , default file is output_file.txt.
Another parameter is Input files,  this is mandatory , it can be more than one.</p>

<b>testunit.py</b>
<p>Can be launch via command line : 
<i>python3 testunit.py</i><BR>
It will run tests on defs in ugen.py . It generate HTML report. </p>

<b>test.py</b>
<p>Can be launch via command line :
<i>python3 test.py ugen.py test_data.txt</i><BR>test_data.txt is described in first part of this document. 
Results are information about tests on differend input cases provided in test_data.txt</p>


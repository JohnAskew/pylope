# pylope (Documentation in progress)
Python log opener, parse and extract search strings

# usage: 
python pylope.py

# description: 
Primary tool searches files for a search string. Can also search a tar.gz file for a search string, as it first extracts it into its own directory and then searches the contents for the search string. If a match is found on the search string, then a report is presented showing the directory searched, which file containing the search string, and the line number within the file. Each entry on the "found search string" report is a link, which if right clicked, will open the file and allow you to search the file for every occurrance of the search string. See below under section, "How to read the search string report" for additional details.

Secondary purpose will open tar and gzipped (gz) files. Simply clicking the "Clear Search" checkbox remove the search term from the search text box and will enable the search functionality (making 2 search buttons turn green and become enabled). It will only extract the tar or gz file and list the contents. The purpose is simply to check the contents of a directory by filename, or the contents of a tar.gz file. A simple report is produced of any files found in that current working directory. It's generally for windows, when doing a tar -tvf is not intuitive to the casual window's user.

(Test phase only) Tertiary purpose will open all gz files in a directory, regardless of how many levels deep the subdirectories span.

## Start Here to search files for a string.
(Assuming you have launched the application).
1. Click the green button >> "Click to ENTER a search string"
2. Enter your search string and click "OK". Note: This is a literal search. See line 3.
3. Optionally, you can check the button >> "Any Case" to make the search case insensitive.
4. At this point, 2 more buttons become green:
<ul>
<li>button >> "Open Directory to search"</li>
<li>button >> "Open & Extract tar.gz to search"</li>
</ul>

## To search all the files in one directory:
Choose the "Open Directory to search" button and you will be guided to select your directory

## To search a tar.gz file:
Choose the "Open & Extract tar.gz to search" button. It will unzip and untar the file into a new directory and then search that directory for the search string.

## How to read the search string report.
(Providing the search string was found).
<ul>
<li>First line is the rundate and time</li>
<li>Second line is the path that was searched</li>
<li>Third line is the search string and the number of occurrences in the directory</li>
</ul>

Past the DETAIL LINE are the files and line number where the search term was found.

## Using the search report to open a particular file.
Click on the desired line of the search report to set the focus. Then Right click the same line, to launch the file open wizard. A python Viewpad will open and present the file, complete with option (at the bottom of the Viewpad) to find every occurrence of the search string.

### Using the ViewPad.
Once the ViewPad presents the open file, there are two buttons at the bottom:
<ul>
<li>Accept search term</li>
<li>Search</li>
</ul>
<p>Choose "Accept search term" button to use the search string populated in the text box.</p>
If you wish to use a different string, returning back to the search report, click anywhere on the report to break the ViewPad focus. Now return to the ViewPad and enter whatever you want in the text box to search on. When satisfied, click on the button >> "Accept search term". The report will jump to the first occurrence of the search string inside the text box.
<p></p>
<p>Click "Search" button to precede with the remaining search.</p>
The report will start over after you have reached the last occurrence.

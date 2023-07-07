# assign2Matching_Specific_String
A regular expression is a sequence of characters that define a search pattern. It is mainly used for string pattern matching.

ach01_.png


Regular expressions are extremely useful in extracting information from text such as: code, log files, spreadsheets, documents, etc.

We can match a specific string  in a test string  by making our regex pattern . This is one of the simplest patterns. However, in the coming challenges, we'll see how well we can match more complex patterns and learn about their syntax.

Task

You have a test string . Your task is to match the string hackerrank. This is case sensitive.

Note

This is a regex only challenge. You are not required to write code.
You only have to fill in the regex pattern in the blank (_________).

Regex_Pattern = r'_________'	# Do not delete 'r'.
r = r"i"

g= "hello i is no i go i reg"
match = re.findall(r,g)
len(match)
import re

Test_String = raw_input()

match = re.findall(Regex_Pattern, Test_String)

print "Number of matches :", 

Input (stdin)
The hackerrank team is on a mission to flatten the world by restructuring the DNA of every company on the planet. We rank programmers based on their coding skills, helping companies source great programmers and reduce the time to hire. As a result, we are revolutionizing the way companies discover and evaluate talented engineers. The hackerrank platform is the destination for the best engineers to hone their skills and companies to find top engineers.
Expected Output
Number of matches : 2

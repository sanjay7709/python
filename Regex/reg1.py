'''
Regular expressions
====================

module ---> (re)

purpose:
=======
> It is used for data validation andbuild robust applications in project development
> program lang independent

Realtime
========
>> Allkinds of electronic circuits
>> all kinds of protocols (http,smtp,nmtp,pop,pop2..etc)
>> all typesof operating system
>> search patterns

definition
===========
Regex of search pattern( combination of alphabets, symbols, digits,special chars) which is used 
to search inthe given data , matching and obtaiig the result

Pre-defined module (re):
=======================
>>search()
>>findall()
>>finditer()
>>start()
>>end()
>>group()


Programmer defined character classin regex
========================================
Syntax === >  "[<search-pattern>]"
Search Pattern
===============
>>> [abc] --> searches for either a, b, or c
>>> [abcABC]----> searches for either a, b, or c,A,B,C
>>> [^abc]---> searches for all except these 3 --a,b,c
>>> [a-z]  --> searches for all small/lowercase alphabets
>>> [^a-z]---->searches for all except lower case alpha
>>> [A-Z]---> searches for all capital alphabets
>>> [^A-Z]----> searches for all except upper case alphabets
>>> [0-9]---> searches for digits b/w 0 to 9
>>> [^0-9]--- searches for other than digits 
>>> [a-zA-Z] --> upper and lower case only
>>> [^a-zA-Z]---> all except upper and lowercase alphabets  {digits and spcial symbols category}
>>> [0-9a-zA-z]----> {alphabets+digits} --alnumeric
>>> [^0-9a-zA-z]---> {special symbols}

Pre-defined chars in regex
==========================
syntax ====> "\<search-pattern>"

chars
======
>>> \s--> searches for space chars
>>> \S ---> Searches all except space chars
>>> \d --> searhes fro digits only
>>> \D --> seacrches fro alle xcept digits hint: (alpha+special symbols)
>>> \w-->  searches for word chars except special symabols hint: [a-zA-Z0-9]
>>> \W --> searches for all except alpha numeric --> hint: special symbols :[^A-Za-z0-9]
>>> \. -->  

Quantifiers in python
======================
quantifiers in regex is used for searching number of occurences of specified search patterns in given
data and obtain the result
They are:
>>> . --> it searches for all
>>> * --> zero , one or more
>>> + --> one or more
>>> ? --> zero or one only

    ex:
        k --> searches only one k at a time
        k+--> one k or more than one k's
        k* --> zero, one or more than one 
        k?--> zero or one at a time

\ddd  or \d{3}
\ddd.dd  --> searches for 3 -integer and 2 decimal values
\w+ ---> one or more words
[A-Za-Z]w+ --> letter and words
\d{2,4}  --> searches for didgits min 2 number and max 4 didgit number
[A-Z][a-z]+ ===> searches for all capital letters and rest are lowercase ex: "Sanjay"



'''
str1='i love india'
newstr1=str1.replace('love','like') #replace of string
print(newstr1)
strNew='guru99'
strNew=strNew.replace('y99','newGuru99')   # will still return Guru99. This is because x.replace("Guru99","Python") returns a copy of X with replacements made
print(strNew)
strxy=str1.replace('i','newGuru99')
print(strxy)
str2="hey guru99"
print(str2.upper())    # convert string to uppercase
str4="they guru99"
print(str4.capitalize())    # convert first string to uppercase
str3="Hey Guru99"
print(str3.lower())    # convert string to lowercase
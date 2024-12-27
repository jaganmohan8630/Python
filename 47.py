# Write a program to accept a string , for each unique
#  character in a string print that character and number of
#  times it appeared in string in tuple format( char,
#  no_of_times
st="tarunbalu"
b=set(st)
for i in b:
    print(tuple([i,st.count(i)]))
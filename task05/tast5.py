st = input( "Введите предложение:" )
#Поешь ещё этих сладких, французских булочек, а потом еще поешь булочек с корицей - они не хуже французских...
st = st.lower()
st = st.replace('ё','е')
e = ',:@.-()/?!;'
for i in range(len(e)):
    st = st.replace(e[i], "")
st = st.split()
st.sort()
w = len(st)
result={}
for i in st:
    result[i]=st.count(i)

print (result)
print (w)


    

   
    


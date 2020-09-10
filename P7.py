def get_company_name(mail):
    st_index = 0
    for i in range(len(mail)):
        if mail[i] == '@':
            st_index = i+1
        elif mail[i] == '.':
            return mail[st_index:i]
    return -1

print(get_company_name("username@companyname.com"))


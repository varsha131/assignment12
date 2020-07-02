Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def listtodict(A,di):
    di=dict(A)
    return di
A=[("pavani",5),("rohini",10),("aruna",15),("murali",20)]
di={}
print("the dictionary is::>",listtodict(A,di))
the dictionary is::> {'pavani': 5, 'rohini': 10, 'aruna': 15, 'murali': 20}
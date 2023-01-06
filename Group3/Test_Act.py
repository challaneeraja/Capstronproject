import unittest
def keyv(dict,key):
    for key in dict.keys():
        return key
def mylist(l):
    for i in l:
        l.sort(reverse=True)
    return l
def mymin(l):
    mini=l[0]
    for i in l[0:]:
        if i<mini:
            mini=i

    return (mini)

class my_Test(unittest.TestCase):
    def test(self):
        dict={"chocolate":50,"pepsi":30}
        key="chocolate"
        r=keyv(dict,key)
        self.assertEqual(r,"chocolate")
    def test1(self):
        l=[89,23,44,99]
        r=mylist(l)
        self.assertEqual(r,[99,89,44,23])
    def test2(self):
        l=[76,23,34,56]
        r=mymin(l)
        self.assertEqual(r,23)

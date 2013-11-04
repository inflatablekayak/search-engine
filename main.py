from crawler import crawl_web
from search import search
import pickle

def main():
    print "Testing..."
    fname = 'udacity.pkl'
    try:
        with open(fname, 'r') as fout:
            website = pickle.load(fout)
            print "Succesfully read my_site from " + fname
    except:
        website = crawl_web('http://udacity.com/cs101x/urank/index.html')
        try:
            with open(fname, 'w') as fout:
                pickle.dump(website, fout)
                print "Succesfully wrote my_site to " + fname
        except IOError, e:
            print "Cannot write out my_site: " + str(e)

    kathleen = 'http://udacity.com/cs101x/urank/kathleen.html'
    nickel = 'http://udacity.com/cs101x/urank/nickel.html'
    arsenic = 'http://udacity.com/cs101x/urank/arsenic.html'
    hummus = 'http://udacity.com/cs101x/urank/hummus.html'
    indexurl = 'http://udacity.com/cs101x/urank/index.html'
    assert search(website, 'Hummus', 'lucky') == kathleen
    assert search(website, 'Hummus') == [kathleen, nickel, arsenic, hummus, indexurl] 
    assert search(website, 'the', 'lucky') == nickel
    assert search(website, 'the') == [nickel, arsenic, hummus, indexurl]
    assert search(website, 'babaganoush', 'lucky') == None
    assert search(website, 'babaganoush') == None
    print "Finished tests."

if __name__ == '__main__':
    main()

# import urllib
# use urllib.request to get data from url
# write function that takes a url
# returns a response
import urllib.request as urllib

def main(url):
    print("Checking Connectivity... ")

    response = urllib.urlopen(url)
    print("Connected to", url, "successfully")
    print("The response code was:", response.getcode())

print("This is a site connectivity checker program.")
input_url = input("Input the url you want to check: ")

main(input_url)
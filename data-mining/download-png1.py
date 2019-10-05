import urllib.request

url = "https://github.com/gwnuysw/PoliticsTrendDM/blob/master/capture2/1545453729898.jpg?raw=true"
savename = "test.png"

urllib.request.urlretrieve(url, savename)

print("저장되었습니다...!")

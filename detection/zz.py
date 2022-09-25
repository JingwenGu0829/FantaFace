import concurrent.futures
import urllib.request

data = [1,2,3,4,5]
value=[]
# Retrieve a single page and report the URL and contents
def load_url(a):
    print(a)
    return a
# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url): url for url in data}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            value += [future.result()]
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            pass       
    print(value)
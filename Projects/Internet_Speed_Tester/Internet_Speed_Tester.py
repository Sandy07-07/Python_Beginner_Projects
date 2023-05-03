import speedtest

test = speedtest.Speedtest()  # It creates the Speedtest object
print("Loading Server List......")
test.get_servers()  # It gets a list of servers which can be used to test the speed
print("Getting the Best Server......")
best = test.get_best_server()  # It is used to get the best server for testing the speed
print("Name :- " + best['name'])  # Name of the best server
print("Country :- " + best['country'])  # Country of the best server
print("CC :- " + best['cc'])  # Code of the best server
print("Sponsor :- " + best['sponsor'])  # Sponsor of the best server
print("ID :- " + best['id'])   # ID of the vest server
print("D :- " + str(best['d']))  # Download speed of the best server
print("Latency :- " + str(best['latency']))  # Latency of the best server
print("Performing Download Test......")
downloader = test.download()  # To calculate the time to download a file of know size
print(f"Download speed: {downloader/1024/1024: .2f} Mbit/s")  # The download speed is returned in bits per second (bps).
print("Performing Upload Test.......")
uploader = test.upload()  # To calculate the time to upload a file of know size
print(f"Upload speed: {uploader/1024/1024: .2f} Mbit/s")  # The upload speed is returned in bits per second (bps)
print("Performing Ping Test........")
pings = test.results.ping  # To calculate time taken for a signal for computer to server and back
print(f"Ping: {pings} ms")  # The ping time is calculated in milliseconds

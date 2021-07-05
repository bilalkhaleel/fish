import webbrowser, glob, os, time
os.chdir("assets")

# for each file in 'assets' folder, launch fish_tracker.html with video src in the URL parameter
# then wait 20 seconds and move to the next file

for file in glob.glob("*"):
    print(file)
    url = 'http://localhost:8000/fish_tracker.html?video=assets/'+file
    webbrowser.open(url, new=1, autoraise=True)
    time.sleep(20)

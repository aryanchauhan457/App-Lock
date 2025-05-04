import psutil

for proc in psutil.process_iter(['name']):
    print(proc)
    
git commit -m "Initial commit"

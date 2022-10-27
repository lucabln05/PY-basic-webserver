#this script write a log file for the server

def log_file_write(console_output):

    import time  # https://pynative.com/python-current-date-time/#:~:text=Get%20Current%20Time%20in%20Python,-There%20are%20many&text=time()-,Use%20the%20time.,the%20current%20time%20in%20seconds.
    import os #https://www.geeksforgeeks.org/create-a-directory-in-python/
        #read system time
    time = time.localtime(time.time())


    #try to create a new folder (Year,Month,Day) and save all requests in files, except the folder is create befor, it open folder and save all requests in files
    try:
        #create folder
        folder_name = f"{time.tm_year}{time.tm_mon}{time.tm_mday}"
        path = os.path.join("Logs/", folder_name)
        folder = os.makedirs(path)

        #create and open file
        logfile = f"{time.tm_year}_{time.tm_mon}_{time.tm_mday}_{time.tm_hour}_{time.tm_min}_{time.tm_sec}.txt"
        open(f"Logs/{folder_name}/{logfile}", "wb")
        log_f = open(f"Logs/{folder_name}/{logfile}", "r+")

        #write config text
        log_f.write(console_output)

    except Exception as err:

        #create and open file
        logfile = f"{time.tm_year}_{time.tm_mon}_{time.tm_mday}_{time.tm_hour}_{time.tm_min}_{time.tm_sec}.txt"
        open(f"Logs/{folder_name}/{logfile}", "wb")
        log_f = open(f"Logs/{folder_name}/{logfile}", "r+")

        #write config text
        log_f.write(console_output)

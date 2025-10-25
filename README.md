# Website Blocker

#### A script developed to block access to specified websites during specified hours.


* Normally, we would have to run the Python script manually each time. To avoid this, I created a task scheduler script using PowerShell. This PowerShell script ensures the Python script runs in the background every time the computer session starts.

* You can also create a scheduled task by following the steps of the PowerShell script using Windows' own scheduled tasks settings, without running the PowerShell script itself.


### Defining Websites and Hours to Block
* Within the ***websiteBlocker.pyw*** file, the desired websites to be blocked are added to the **website_liste** list.

* The start and end times for blocking the specified websites are written to the **baslangicSaati** and **bitisSaati** variables.



### Example Usage

* As an example, I will block **Google** between *08:00 AM* and *06:00 PM*.

* I am creating a scheduled task by running the **zamanlanmisGorev.ps1** file I created with PowerShell.

* After creating the scheduled task, the Python script will run in the background every time a session starts. </br></br>
![zamanlanmisgorev](https://user-images.githubusercontent.com/25087769/51472328-2ed64f00-1d8a-11e9-85c5-778b28372331.PNG)

* Upon the next session login, *webBlocker* activated.
* As the time was *02:06:09 PM (14:06:09)*, **https://www.google.com**, **google.com**, and **www.google.com** addresses were added to the hosts file.


 ### Hosts file

![hosts_dosyasi](https://user-images.githubusercontent.com/25087769/51473466-80cca400-1d8d-11e9-8f0d-0372355502e0.PNG)


 ### Google
![engellenen site2](https://user-images.githubusercontent.com/25087769/51472877-ce481180-1d8b-11e9-9300-a644c2dbac0e.png)


* When the time was *09:06:26 PM (21:06:26)*, **https://www.google.com**, **google.com**, and **www.google.com** addresses were removed from the hosts file.

 ### Hosts file
![hosts_dosyasi2](https://user-images.githubusercontent.com/25087769/51473195-bc1aa300-1d8c-11e9-89ba-4b6d1311e517.PNG)

 ### Google
![engellenmemis site](https://user-images.githubusercontent.com/25087769/51473202-c2a91a80-1d8c-11e9-8749-8368c06abacf.PNG)

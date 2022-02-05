# movie-downloader

Automated movie-downloader using IMDBpy, YIFY API, shell-script and cron-jobs.

#### Requirements:

1. ProtonVPN or any other VPN with CLI enabled.
2. Cinemagoer or IMDBpy (Python Package).
3. Homebrew (in case of Mac).

#### Implementation: 

Finding the right movie links are very frustrating and have to deal with a whole barrage of ads. 

1. Create a txt file with the name **toDownloadMovies.txt** and enter the movie(s) name in that one by one. 
2. You can either choose to run the python file directly to get the magnet link directly or choose to automate the process by running the shell-script present in the repository.
3. If you choose to automate, set-up a CLI VPN (I have used ProtonVPN).
4. Set up a cron-job by the inbuilt cron-job (in Mac) by the command `crontab -e`.
5. [Crontab Guru](https://crontab.guru) is a good place to learn and test job scheduling.

# ITSC-4155-project8 - (Mosaic Music)
Mosaic Music is A beta music-based social application oriented around Users who are enthusiastic about Categorizing and sharing songs with others. It utilizes the Deezer API to fetch music data for users to search for songs to like and add to their playlists, as well as to their recommended pages.

- Like, Listen to, and Search for songs, artists, and albums using the Deezer API
- Create an account, edit your account information, and upload a profile picture
- Create a playlist, as well as add songs to the playlist
- Like songs, and have Artists and songs recommended to you based on those likes in the recommended page
- View other user profiles on the site 



### Group 4 
&nbsp;&nbsp;&nbsp;&nbsp;**Scrum Master**
    - Jasmine Kingg

&nbsp;&nbsp;&nbsp;&nbsp;**Product Owner**
    - Sanjana Bansal

&nbsp;&nbsp;&nbsp;&nbsp;**Developers**
    - Aaloki Patel
    - Ruthvika Kosuri
    - Lilian Camacho
    - Jasmine Kingg
    - Sanjana Bansal


# [DEMONSTRATION VIDEO](https://drive.google.com/file/d/1ZWmh6B0bx4pjwfdL8kMhY4asbDbSCyK8/view?usp=sharing)



# [Installation] Instructions
**Needed materials:**
> vscode
> python installed on your device

Download the repo if you havent already.

## 1. Open your Terminal
 - `cd mosaicmusic`
 - `python -m venv venv`
 - if prompted to select the file for the work terminal in VSCODE, select yes
      - `source venv/Scripts/activate` (for windows)
      - `source venv/bin/activate` (for macOS)
 - `pip install -r requirements.txt`

## 2. Create an .env file in the same folder.
- In the .env file, copy and paste the following:
     
       SECRET_KEY=demo  
       DATABASE_URL=postgresql://mm_db_ac69_user:D4juXBSUgP9nECMDiBIeqFhn0o7fL3Fa@dpg-comphj4f7o1s73f8f4h0-a.oregon-postgres.render.com/mm_db_ac69
- This URL lets your application connect to a remote database to view preloaded data.


## 3. Run the Application in the terminal
     flask --app app run


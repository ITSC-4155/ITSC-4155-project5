
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
       DATABASE_URL=postgres://mm_db_ac69_user:D4juXBSUgP9nECMDiBIeqFhn0o7fL3Fa@dpg-comphj4f7o1s73f8f4h0-a.oregon-postgres.render.com/mm_db_ac69
- This URL lets your application connect to a remote database to view preloaded data.

## 3. Run the Application in the terminal
     flask --app app run

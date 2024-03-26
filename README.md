# ITSC-4155-project7 - (Mosaic Music)

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

# Instructions
**Needed materials:**
> pgadmin4 client
> 
> vscode
> 
> python installed on your device


## 1. Download and Install pgAdmin4
Download on the OS of your choice
https://www.postgresql.org/download/
1. When downloaded. Click Servers. Choose the PostgresSql server version you have been provided
![step 1](https://imgur.com/DndDxmB.png)
2. Under servers, create a new database

![step 2](https://imgur.com/dGOMLYg.png)

4. Name the database. _(The example has been named testdb for clarity in this tutorial. )_
   - You can leave the owner's name as **postgres**.
   - You will be prompted to create a password. Make it something simple that you can remember for the sake of this test

 ## 2. Enter VSCode 
1. clone the repository if you haven't already.
2. In the `mosaicmusic` folder (but outside of the app folder), create a file named **.env**

4. Copy and paste the contents of `.env.sample` file into the **.env** file. DATABASE_URL should be filled out based on your database information, without the brackets.

6. Open your Terminal
     - `python -m venv venv`
     - if prompted to select the file for the work terminal in VSCODE, select yes
     - `source venv/Scripts/activate` (for windows)
     - `source venv/bin/activate` (for macOS)
     - `cd mosaicmusic`
     - `pip install -r requirements.txt`

7. while that is installing, return to PgAdmin 4 database .
   - under Schemas > Tables, Right click and open the "Query Tool"
   - ![step 8](https://imgur.com/cS1EIph.png)
   - Copy and paste the contents of `mosaic_schema.sql` into the query, and hit play at the top to initialize the current tables
   - ![step 7](https://imgur.com/33KpLkK.png)
  
## 8. Return to the VScode Terminal
9. type `flask --debug run`, and open the instructed development server link.
![step 9](https://imgur.com/fQnK4US.png)


11. Click the login link, and redirect to the registration page.
12. Fill out the information. If successful, you should see the information displayed in pgadmin under the table view.

![Step 12](https://imgur.com/op9qSxG.png)



13. Log In with the entered information. If successful you should be redirected to the home page with your chosen username.
![step 13](https://imgur.com/snjASNP.png)

You did it!

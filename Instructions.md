# POKEDEX Project Instructions:


## Getting started
1. To run the Flask App in development, inside the `flask-backend` directory.


2. Install dependencies

      ```bash
      pipenv install -r requirements.txt
      ```

3. Create a **.env** file based on the example with proper settings for your
   development environment

4. Make sure the SQLite3 database connection URL is in the **.env** file

5. Get into your pipenv, migrate your database, seed your database, and run your Flask app

   ```bash
   pipenv shell
   ```

   ```bash
   flask db upgrade
   ```

   ```bash
   flask seed all
   ```

   ```bash
   flask run
   ```

6. To run the React App in development, inside the `frontend` directory.

   ```bash
   npm install
   ```

   ```bash
   npm start
   ```

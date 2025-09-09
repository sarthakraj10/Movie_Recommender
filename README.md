
# Movie Recommender system

This project is a Movie Recommendation Website designed to suggest five movies similar to the one the user likes. By selecting a movie from the list, the website will analyze the user's choice using a machine learning model and display five related movies. Each recommendation comes with a poster image and a link to the movie's IMDb page, allowing users to explore more about the suggested films


## Features

- **User-Friendly Interface**: Built with Streamlit, offering an intuitive and easy-to-navigate design
- **Movie Selection**: Users can select a movie they like from a predefined list.
- **Visual Display**: Each recommended movie is presented with its poster for a visually engaging experience.
- **Interactive Links**: Users can click on the movie posters to be redirected to the IMDb page for more detailed information.


## Screenshots

![App Screenshot](https://github.com/user-attachments/assets/9a2a654d-8dff-46e9-a093-5a14861380ba)


## Run Locally

#### Tech Stack needed
- Python3
- pip3

#### 1. Clone the project
- First, clone the GitHub repository to their local machine using the following command:

```bash
  git clone https://github.com/Pradipram/movie-recommendation.git
```
### 2. Navigate to the Project Directory
- Move into the project directory
```bash
  cd movie-recommendation
```
### 3. Set Up a Virtual Environment
- Create a virtual environment (optional but recommended):
```python
python -m venv .venv
```
- Activate the virtual environment
    - On Windows:
    ```bash
    .venv\Scripts\activate
    ```
    - On macOS/Linux
    ```bash
    source .venv/bin/activate
    ```

### 4. Install Dependencies
- Install the required packages from `requirements.txt`

```bash
  pip install -r requirements.txt
```
### 5. Set Up the Environment Variables
- Create a .env file in the project directory and add the following line
```bash
tmdb_API_KEYS=your_tmdb_api_key
```
- Replace your_tmdb_api_key with an actual API key from The Movie Database (TMDb). They need to sign up at [TMDb](https://www.themoviedb.org/) to get an API key.

### 6. Run the Streamlit Application
- Run the Streamlit app using the following command
```python
streamlit run app.py
```

- This will start the local server, and the app will be accessible in the browser at `http://localhost:8501`.



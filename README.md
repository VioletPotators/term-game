# React + Flask Full-Stack Application

A full-stack web application with React frontend and Flask backend API.

## Project Structure

```
term-game/
├── backend/          # Flask backend
│   ├── app.py       # Flask application
│   └── requirements.txt
├── src/             # React frontend
│   ├── App.jsx
│   ├── App.css
│   ├── main.jsx
│   └── index.css
├── package.json     # React dependencies
├── vite.config.js   # Vite configuration with API proxy
└── index.html       # HTML entry point
```

## Setup Instructions

### Backend (Flask)

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the Flask server:
   ```bash
   python app.py
   ```
   The API will be available at `http://localhost:5000`

### Frontend (React)

1. Install dependencies:
   ```bash
   npm install
   ```

2. Start the development server:
   ```bash
   npm run dev
   ```

3. The React app will be available at `http://localhost:5173`

## Running Both Servers

You need to run both servers simultaneously:

1. **Terminal 1** - Start Flask backend:
   ```bash
   cd backend
   python app.py
   ```

2. **Terminal 2** - Start React frontend:
   ```bash
   npm run dev
   ```

The Vite dev server is configured to proxy `/api` requests to the Flask backend at `http://localhost:5000`.

## API Endpoints

- `GET /api/health` - Health check endpoint
- `GET /api/data` - Sample data endpoint
- `GET /api/about` - About information

## Build for Production

1. Build the React app:
   ```bash
   npm run build
   ```

2. The built files will be in the `dist/` directory, ready to be served by Flask or any static file server.


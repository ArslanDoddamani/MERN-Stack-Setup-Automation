# MERN Stack Project Setup Script

This project provides a Python script to automate the setup of a basic MERN (MongoDB, Express, React, Node.js) stack folder structure. The script initializes the frontend with React (using Vite) and TailwindCSS, and the backend with Express.js and essential Node.js modules.

---

## **Features**
- Creates a folder structure for a MERN stack application:
  - **Frontend**: React with Vite and TailwindCSS.
  - **Backend**: Express.js with commonly used dependencies.
- Automatically installs required dependencies.
- Configures TailwindCSS and basic backend files.
- Creates placeholder files for React components and backend logic.

---

## **Prerequisites**
Before running this script, ensure the following tools are installed on your system:

1. **Node.js** (v16 or higher)  
   [Download Node.js](https://nodejs.org/)
   
2. **npm** (Node Package Manager)  
   Installed automatically with Node.js.

3. **Python** (v3.6 or higher)  
   [Download Python](https://www.python.org/)

4. **Git** (optional, but recommended)  
   [Download Git](https://git-scm.com/)

---

## **How to Use**

### 1. **Clone or Download the Script**
Save the `mern_setup.py` script and supporting files (`indexCSS.txt`, `tailwindConfig.txt`, `.gitignore`, `.prettierignore`, `.prettierrc`) in the same directory.

### 2. **Navigate to the Script Directory**
Open a terminal or command prompt and navigate to the folder where the script is located:

```bash
cd /path/to/script
```

### 3. **Run the Script**
Execute the script using Python:
```bash
python mern_setup.py
```

### 4. **Provide the Root Folder Name**
When prompted, provide a name or path for your MERN stack project:
```bash
Enter the root folder name for your MERN stack project: my-mern-project:
```
The script will:
- Create a folder structure in the specified directory.
- Set up the frontend (client) and backend (server).
- Install all required dependencies.

### 5. **Run the Applications**
Frontend:

Navigate to the client folder and start the React application:
```bash
cd my-mern-project/client
npm run dev
```

Backend:
1. Navigate to the server folder:
```bash
cd my-mern-project/server
```

2. Add the following script to your package.json file under the scripts section:
```bash
"scripts": {
  "dev": "nodemon -r dotenv/config --experimental-json-modules src/index.js"
}
```

3. Start the backend:
```bash
npm run dev
```

## **Folder Structure**
After running the script, your project will look like this:
```bash
my-mern-project/
├── client/          # Frontend (React with Vite & TailwindCSS)
│   ├── src/
│   │   ├── index.css
│   │   ├── App.jsx
│   │   ├── App.css
│   ├── tailwind.config.js
├── server/          # Backend (Express.js)
│   ├── src/
│   │   ├── controllers/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── views/
│   │   ├── utils/
│   │   ├── db/
│   │   ├── app.js
│   │   ├── index.js
│   │   ├── constants.js
│   ├── .env
│   ├── .gitignore
│   ├── .prettierrc
│   ├── .prettierignore
```
## **Customization**
- Modify the templates for files like indexCSS.txt, tailwindConfig.txt, .gitignore, etc., to suit your project needs.
- Add additional dependencies or folders as required for your specific use case.

## **Contributing**
Feel free to fork this repository, submit issues, or create pull requests to enhance the functionality of the script.

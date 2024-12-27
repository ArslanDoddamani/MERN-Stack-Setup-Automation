import logging
import platform
import subprocess
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s ')

def isWindows():
    return platform.system() == 'Windows'

def runCommand(command):
    try:
        if isWindows():
            command = [cmd + '.cmd' if cmd in ['npm', 'npx'] else cmd for cmd in command]
        subprocess.run(command, check=True, shell=isWindows())
    except Exception as e:
        logging.error(f"Command failed: {' '.join(command)}\nError: {e}")
        exit(1)

def folderStructure(root_folder):
    try:
        os.makedirs(root_folder, exist_ok=True)

        frontendPath = os.path.join(root_folder, 'client')
        backendPath = os.path.join(root_folder,'server')

        os.makedirs(frontendPath, exist_ok=True)
        os.makedirs(backendPath, exist_ok=True)

        logging.info("Root folder and basic structure created.")
        return frontendPath, backendPath
    except Exception as e:
        logging.error(f"Error creating root folder: \n{e}")
        exit(1)

def setupFrontend(frontendPath):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))

        os.chdir(frontendPath)
        logging.info("Setting up frontend............")

        runCommand(['npm', 'create', 'vite@latest', '.', '--template', 'react'])
        runCommand(['npm', 'install'])

        logging.info("Setting up TailwindCSS.............")
        runCommand(['npm', 'install', '-D', 'tailwindcss', 'postcss', 'autoprefixer'])
        runCommand(['npx', 'tailwindcss', 'init', '-p'])

        with open(os.path.join(script_dir, 'indexCSS.txt'), 'r') as source_file:
            content = source_file.read() 
        
        with open(os.path.join(os.getcwd(), 'src', 'index.css'), 'w') as destination_file:
            destination_file.write(content)

        with open(os.path.join(script_dir, 'tailwindConfig.txt'), 'r') as source_file:
            content = source_file.read()
        
        with open(os.path.join(os.getcwd(), 'tailwind.config.js'), 'w') as destination_file:
            destination_file.write(content)

        with open(os.path.join(os.getcwd(),'src', 'App.jsx'), 'w') as destination_file:
            pass

        with open(os.path.join(os.getcwd(),'src', 'App.css'), 'w') as destination_file:
            pass
        
        os.chdir('../../')

        logging.info("Frontend setup complete with Vite React and Tailwind CSS.")
        
    except Exception as e:
        logging.error(f"Error setting up frontend: \n{e}")
        exit(1)

def setupBackend(backendPath):
    try:
        print(os.getcwd())
        script_dir = os.path.dirname(os.path.abspath(__file__))

        os.chdir(backendPath)
        logging.info("Setting up backend............")

        runCommand(['npm', 'init', '-y'])

        logging.info("initializing backend packages............")
        
        runCommand(['npm', 'install', 'express', 'cors', 'dotenv', 'mongoose', 'nodemon', 'prettier', 'bcrypt', 'cookie-parser', 'jsonwebtoken'])

        logging.info("setting up backend files............")

        with open(os.path.join(os.getcwd(), '.env'), 'w') as file:
            pass

        with open(os.path.join(script_dir, 'gitignore.txt'), 'r') as source_file:
            content = source_file.read()
        
        with open(os.path.join(os.getcwd(), '.gitignore'), 'w') as destination_file:
            destination_file.write(content)
        
        with open(os.path.join(script_dir, 'prettierignore.txt'), 'r') as source_file:
            content = source_file.read()
        
        with open(os.path.join(os.getcwd(), '.prettierignore'), 'w') as destination_file:
            destination_file.write(content)
        
        with open(os.path.join(script_dir, 'prettierrc.txt'), 'r') as source_file:
            content = source_file.read()
        
        with open(os.path.join(os.getcwd(), '.prettierrc'), 'w') as destination_file:
            destination_file.write(content)
        
        os.makedirs(os.path.join('src'), exist_ok=True)

        os.chdir(os.path.join(os.getcwd(),'src'))

        os.makedirs(os.path.join('models'), exist_ok=True)
        os.makedirs(os.path.join('views'), exist_ok=True)
        os.makedirs(os.path.join('utils'), exist_ok=True)
        os.makedirs(os.path.join('routes'), exist_ok=True)
        os.makedirs(os.path.join('controllers'), exist_ok=True)
        os.makedirs(os.path.join('db'), exist_ok=True)

        with open(os.path.join('app.js'), 'w') as file:
            pass

        with open(os.path.join('index.js'), 'w') as file:
            pass

        with open(os.path.join('constants.js'), 'w') as file:
            pass

        logging.info('Backend setup complete with structure and file System')

    except Exception as e:
        logging.error(f"Error setting up backend: \n{e}")
        exit(1)

def main():
    root_folder = input("Enter the root folder name for your MERN stack project: ").strip()

    try:
        runCommand(['node', '--version'])
        runCommand(['npm', '--version'])
    except Exception as e:
        logging.error("Node.js and npm are required but not installed.\nPlease install them first.")
        exit(1)
    
    frontendPath, backendPath = folderStructure(root_folder)

    setupFrontend(frontendPath)
    setupBackend(backendPath)

    logging.info("MERN stack folder structure and setup completed successfully.")
    print("\n\nTo run the Frontend\n")
    print(f"cd {frontendPath}\n\nnpm run dev")
    print("\n\nTo run the Backend\n")
    script = '"scripts": {"dev": "nodemon -r dotenv/config --experimental-json-modules src/index.js"},'
    print(f"add this script to packages.json file\n {script}")
    print(f"\ncd {backendPath}\n\nnpm run dev\n")

if __name__ == "__main__":
    main()


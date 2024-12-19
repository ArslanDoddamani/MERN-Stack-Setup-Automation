import os
import subprocess
import platform
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_windows():
    """Check if the operating system is Windows."""
    return platform.system() == 'Windows'

def run_command(command):
    """Run a shell command with cross-platform compatibility."""
    try:
        if is_windows():
            command = [cmd + '.cmd' if cmd in ['npm', 'npx'] else cmd for cmd in command]
        subprocess.run(command, check=True, shell=is_windows())
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {' '.join(command)}\nError: {e}")
        exit(1)

def create_folder_structure(root):
    try:
        # Create root folder
        os.makedirs(root, exist_ok=True)

        # Create frontend and backend folders
        frontend_path = os.path.join(root, 'frontend')
        backend_path = os.path.join(root, 'backend')

        os.makedirs(frontend_path, exist_ok=True)
        os.makedirs(backend_path, exist_ok=True)

        logging.info("Root folder and basic structure created.")
        return frontend_path, backend_path
    except Exception as e:
        logging.error(f"Error creating folder structure: {e}")
        exit(1)

def setup_frontend(frontend_path):
    try:
        # Navigate to frontend directory
        os.chdir(frontend_path)
        logging.info("Setting up frontend...")

        # Run Vite React setup
        run_command(['npm', 'create', 'vite@latest', '.', '--template', 'react'])

        # Install dependencies
        run_command(['npm', 'install'])

        # Install and configure Tailwind CSS
        run_command(['npm', 'install', '-D', 'tailwindcss', 'postcss', 'autoprefixer'])
        run_command(['npx', 'tailwindcss', 'init'])

        # Add Tailwind CSS configuration to CSS file
        with open(os.path.join(frontend_path, 'src', 'index.css'), 'w', encoding='utf-8') as css_file:
            css_file.write('''@tailwind base;\n@tailwind components;\n@tailwind utilities;''')

        logging.info("Frontend setup complete with Vite React and Tailwind CSS.")
    except Exception as e:
        logging.error(f"Error setting up frontend: {e}")
        exit(1)

def setup_backend(backend_path):
    try:
        # Navigate to backend directory
        os.chdir(backend_path)
        logging.info("Setting up backend...")

        # Initialize npm project
        run_command(['npm', 'init', '-y'])

        # Install backend dependencies
        run_command(['npm', 'install', 'express', 'cors', 'dotenv', 'mongoose'])

        # Create backend folder structure
        os.makedirs(os.path.join(backend_path, 'models'), exist_ok=True)
        os.makedirs(os.path.join(backend_path, 'views'), exist_ok=True)
        os.makedirs(os.path.join(backend_path, 'utils'), exist_ok=True)
        os.makedirs(os.path.join(backend_path, 'routes'), exist_ok=True)
        os.makedirs(os.path.join(backend_path, 'controllers'), exist_ok=True)

        logging.info("Backend setup complete with directory structure and necessary packages.")
    except Exception as e:
        logging.error(f"Error setting up backend: {e}")
        exit(1)

def main():
    # Define the root folder
    root_folder = input("Enter the root folder name for your MERN stack project: ").strip()

    # Check if node and npm are installed
    try:
        run_command(['node', '--version'])
        run_command(['npm', '--version'])
        logging.info("Node.js and npm are installed.")
    except Exception:
        logging.error("Node.js and npm are required but not installed. Please install them first.")
        exit(1)

    # Create folder structure
    frontend_path, backend_path = create_folder_structure(root_folder)

    # Setup frontend
    setup_frontend(frontend_path)

    # Setup backend
    setup_backend(backend_path)

    logging.info("MERN stack folder structure and setup completed successfully.")

if __name__ == "__main__":
    main()

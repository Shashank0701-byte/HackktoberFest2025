# Certificate Generator Frontend

![React](https://img.shields.io/badge/React-18.2.0-blue?style=for-the-badge&logo=react)
![Vite](https://img.shields.io/badge/Vite-7.1.9-646CFF?style=for-the-badge&logo=vite)
![Node.js](https://img.shields.io/badge/Node.js-18+-green?style=for-the-badge&logo=node.js)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

A modern React frontend application for the GDG Babcock Hacktoberfest 2025 Certificate Generator project. This application provides an intuitive interface for creating and managing certificates for event participants.

## 🚀 Features

- **Modern React 18** with Vite for fast development
- **Responsive Design** with clean, professional UI
- **Certificate Form** for easy certificate generation
- **Navigation Components** with modern styling
- **404 Error Handling** with custom error pages
- **ESLint Integration** for code quality

## 📋 System Requirements

Before you begin, ensure you have the following installed on your system:

- **Node.js** (version 18.0.0 or higher)
- **npm** (version 8.0.0 or higher) or **yarn** (version 1.22.0 or higher)
- **Git** for version control

### Verify Your Installation

```bash
# Check Node.js version
node --version

# Check npm version
npm --version

# Check Git version
git --version
```

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
# Clone the main repository
git clone https://github.com/GDGBabcockUniversity/gdg-babcock-hacktoberfest-2025.git

# Navigate to the project directory
cd gdg-babcock-hacktoberfest-2025
```

### 2. Navigate to Frontend Directory

```bash
cd frontend
```

### 3. Install Dependencies

```bash
# Using npm (recommended)
npm install

# Alternative: Using yarn
yarn install
```

### 4. Start the Development Server

```bash
# Using npm
npm run dev

# Alternative: Using yarn
yarn dev
```

### 5. Access the Application

Open your browser and navigate to:
- **Local Development**: `http://localhost:5173` (default Vite port)
- The exact URL will be displayed in your terminal after starting the server

## 📁 Project Structure

```
frontend/
├── public/
│   └── gdg-favicon.svg          # GDG favicon
├── src/
│   ├── assets/                  # Asset files (currently empty)
│   ├── components/
│   │   ├── Footer/              # Footer component
│   │   │   ├── Footer.css
│   │   │   └── Footer.jsx
│   │   └── Navbar/              # Navigation component
│   │       ├── Navbar.css
│   │       └── Navbar.jsx
│   ├── pages/
│   │   ├── CertCompletion/   # Certificate form page
│   │   │   ├── CertCompletion.css
│   │   │   └── CertCompletion.jsx
│   │   └── NotFound/            # 404 error page
│   │       ├── NotFounnd.css
│   │       └── NotFound.jsx
│   ├── App.css                  # Main app styles
│   ├── App.jsx                  # Main app component
│   ├── index.css                # Global styles
│   └── main.jsx                 # Application entry point
├── Dockerfile                   # Docker configuration
├── eslint.config.js             # ESLint configuration
├── index.html                   # HTML template
├── package.json                 # Dependencies and scripts
├── vite.config.js               # Vite configuration
└── README.md                    # This file
```

## 🎯 Available Scripts

| Script | Command | Description |
|--------|---------|-------------|
| **Development** | `npm run dev` | Starts the development server with hot reload |
| **Build** | `npm run build` | Creates a production build in `dist/` folder |
| **Preview** | `npm run preview` | Previews the production build locally |
| **Lint** | `npm run lint` | Runs ESLint to check code quality |

## 🐳 Docker Setup (Alternative)

If you prefer using Docker:

```bash
# Build the Docker image
docker build -t certificate-generator-frontend .

# Run the container
docker run -p 5173:5173 certificate-generator-frontend
```

## 🔧 Development Guidelines

### Code Style
- This project uses **ESLint** for code quality
- Follow React best practices and hooks guidelines
- Use functional components with hooks
- Maintain consistent naming conventions

### File Naming
- Components: PascalCase (e.g., `CertCompletion.jsx`)
- CSS files: PascalCase (e.g., `CertCompletion.css`)
- Use descriptive, meaningful names

### Component Structure
```jsx
// Example component structure
import React from 'react';
import './ComponentName.css';

const ComponentName = () => {
  return (
    <div className="component-name">
      {/* Component content */}
    </div>
  );
};

export default ComponentName;
```

## 🚨 Troubleshooting

### Common Issues

**Port Already in Use**
```bash
# Kill process on port 5173
npx kill-port 5173

# Or use a different port
npm run dev -- --port 3000
```

**Node Modules Issues**
```bash
# Clear npm cache and reinstall
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**ESLint Errors**
```bash
# Fix auto-fixable ESLint issues
npm run lint -- --fix
```

## 🤝 Contributing

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Before Contributing
- Read the [CONTRIBUTING.md](../CONTRIBUTING.md) file
- Check existing issues to avoid duplicates
- Follow the project's code style guidelines
- Test your changes thoroughly

## 📚 Tech Stack

- **Frontend Framework**: React 18.2.0
- **Build Tool**: Vite 7.1.9
- **Routing**: React Router DOM 7.9.4
- **Styling**: CSS3 with modern features
- **Code Quality**: ESLint with React plugins
- **Package Manager**: npm/yarn

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

## 🙏 Acknowledgments

- **GDG Babcock University** for organizing Hacktoberfest 2025
- **React Team** for the amazing framework
- **Vite Team** for the fast build tool
- All contributors who make this project possible

---

**Happy Coding! 🚀**

For more information about the project, visit the [main README](../README.md) or join our [GDG Babcock community](https://gdg.community.dev/gdg-on-campus-babcock-university-ilishan-remo-nigeria/).
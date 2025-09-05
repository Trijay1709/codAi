# 🚀 codai – AI Coding Assistant CLI

`codai` is a command-line coding assistant powered by Google Gemini that helps you write, debug, and manage code directly from your terminal.

## 📦 Installation

### Option 1: Install from GitHub (development mode)
Clone the repo and install with pip:

```bash
git clone https://github.com/Trijay1709/codai.git
cd codai
pip install -e .
```

The `-e` flag installs in "editable" mode, so changes to the source update immediately.

### Option 2: Install with uv
If you're using uv:

```bash
git clone https://github.com/Trijay1709/codai.git
cd codai
uv pip install -e .
```

## 🔑 API Key Setup

You need a Gemini API key. You can provide it in one of three ways:

1. **Environment variable (recommended):**
   ```bash
   export GEMINI_API_KEY="your_api_key_here"
   ```

2. **.env file in project root:**
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

3. **CLI flag:**
   ```bash
   codai "find hello.py" -k your_api_key_here
   ```

## ⚡ Usage

### Basic prompt
```bash
codai "find hello.py"
```

### Run in verbose mode
```bash
codai "list files" --verbose
```

### Specify working directory
```bash
codai "read app.py" --dir ./my_project
```

### Override API key
```bash
codai "run script.py" --key your_api_key_here
```

## Advanced Examples

### 1. Bug Fixing
Ask codai to find and fix a bug in your codebase:

```bash
codai "debug main.py, it throws a KeyError when parsing JSON" --dir ./my_project
```

codai will:
- Inspect main.py
- Suggest and apply a bug fix
- Show the updated code

### 2. Setting up a New Project
Quickly scaffold a Python project:

```bash
codai "create a new Flask project with routes for / and /health" --dir ./flask_app
```

codai will:
- Create the flask_app/ folder
- Write app.py with starter code
- Add a requirements.txt

### 3. Modify Existing Code
Update a function to add logging:

```bash
codai "add debug logging to the process_data function in utils.py" --dir ./my_project
```

### 4. Multi-File Task
Generate boilerplate for a FastAPI app:

```bash
codai "setup a FastAPI project with routes, models, and config files" --dir ./fastapi_service
```

### 5. Automated Testing
Create unit tests for an existing module:

```bash
codai "write pytest unit tests for calculator.py" --dir ./my_project
```
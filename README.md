<p align="center">
  <img src="https://raw.githubusercontent.com/getbindu/create-bindu-agent/refs/heads/main/assets/light.svg" alt="bindu Logo" width="200">
</p>

<h1 align="center">Writer Agent</h1>
<h3 align="center">AI-Powered Creative Writing Assistant</h3>

<p align="center">
  <strong>Autonomous agent for generating complete novels, books, and short story collections using the kimi-k2-thinking model</strong>
</p>

<p align="center">
  <a href="https://github.com/Paraschamoli/writer-agent/actions/workflows/main.yml?query=branch%3Amain">
    <img src="https://img.shields.io/github/actions/workflow/status/Paraschamoli/writer-agent/main.yml?branch=main" alt="Build status">
  </a>
  <a href="https://img.shields.io/github/license/Paraschamoli/writer-agent">
    <img src="https://img.shields.io/github/license/Paraschamoli/writer-agent" alt="License">
  </a>
  <img src="https://img.shields.io/badge/python-3.12+-blue.svg" alt="Python Version">
</p>

---

## 📖 Overview

The Writer Agent is an advanced AI-powered creative writing assistant that generates **complete, substantial** literary works. Built on the [Bindu Agent Framework](https://github.com/getbindu/bindu) with the Agno framework, it combines the power of the kimi-k2-thinking model with custom tools for project management and file organization.

**Key Capabilities:**
- � **Complete Novel Generation**: Creates full-length novels with proper structure and character development
- 📖 **Short Story Collections**: Generates themed collections with interconnected narratives
- 📝 **Book Creation**: Produces comprehensive guides and educational content
- 🗂️ **Project Management**: Organized folder structure with automatic file management
- 🔄 **Context Compression**: Handles long projects with intelligent memory management
- ⚡ **Real-time Generation**: Stream content creation with progress tracking

---

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) package manager
- API key for Moonshot AI or OpenRouter

### Installation

```bash
# Clone the repository
git clone https://github.com/Paraschamoli/writer-agent.git
cd writer-agent

# Create virtual environment
uv venv --python 3.12
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv sync

# Configure environment
cp .env.example .env
```

### Configuration

Edit `.env` and add your API keys:

| Key | Get It From | Required |
|-----|-------------|----------|
| `MOONSHOT_API_KEY` | [Moonshot AI Platform](https://platform.moonshot.cn/) | ✅ Recommended |
| `OPENROUTER_API_KEY` | [OpenRouter](https://openrouter.ai/keys) | ✅ Alternative |
| `MODEL_NAME` | Custom model name | Optional (default: kimi-k2-thinking) |
| `MEM0_API_KEY` | [Mem0 Dashboard](https://app.mem0.ai/dashboard/api-keys) | Optional |

**Model Options:**
- **Recommended**: `kimi-k2-thinking` with Moonshot API (best for creative writing)
- **Alternative**: Any OpenRouter model (e.g., `openai/gpt-4o`)

### Run the Agent

```bash
# Start the agent
uv run python -m writer_agent

# Agent will be available at http://localhost:3773
```

### Github Setup

```bash
# Initialize git repository and commit your code
git init -b main
git add .
git commit -m "Initial commit"

# Create repository on GitHub and push (replace with your GitHub username)
gh repo create Paraschamoli/writer-agent --public --source=. --remote=origin --push
```

---

## 💡 Usage

### Example Queries

```bash
# Novel Generation
"Create a mystery novel set in Victorian London with 10 chapters, featuring a detective solving a series of murders"

# Short Story Collection
"Write a collection of 5 sci-fi short stories about artificial intelligence and consciousness, each exploring different aspects"

# Educational Book
"Generate a comprehensive guide to Python programming with 15 chapters for absolute beginners"

# Romance Novel
"Create a romance novel set in modern Tokyo with 8 chapters about two people from different cultures finding love"

# Fantasy Series
"Write a fantasy novel about a young wizard discovering their powers, with 12 chapters and magical world-building"
```

### Input Formats

**Plain Text:**
```
Create a collection of 7 interconnected horror stories set in an abandoned asylum
```

**JSON:**
```json
{
  "messages": [
    {
      "role": "user", 
      "content": "Write a thriller novel with 8 chapters about a detective hunting a serial killer"
    }
  ]
}
```

### Output Structure

The agent generates organized writing projects:

```
output/your_project_name/
├── chapter_01.md          # Complete chapter (3,000-5,000 words)
├── chapter_02.md          # Next chapter
├── story_title.md         # Short stories (3,000-10,000 words)
├── table_of_contents.md   # Project overview
├── readme.md              # Project information
└── .context_summary_*.md  # Auto-saved context backups
```

**Content Characteristics:**
- **Substantial Length**: 3,000-10,000 words per major piece
- **Complete Narratives**: No summaries or placeholders
- **Rich Detail**: Full dialogue, descriptions, and scenes
- **Proper Structure**: Chapter divisions, character development, plot arcs

---

## 🔌 API Usage

The agent exposes a RESTful API when running. Default endpoint: `http://localhost:3773` 

### Quick Start

For complete API documentation, request/response formats, and examples, visit:

📚 **[Bindu API Reference - Send Message to Agent](https://docs.getbindu.com/api-reference/all-the-tasks/send-message-to-agent)**


### Additional Resources

- 📖 [Full API Documentation](https://docs.getbindu.com/api-reference/all-the-tasks/send-message-to-agent)
- 📦 [Postman Collections](https://github.com/GetBindu/Bindu/tree/main/postman/collections)
- 🔧 [API Reference](https://docs.getbindu.com)

---

## 🎯 Skills

### Creative Writing (v1.0.0)

**Primary Capability:**
- Generates complete, substantial creative writing projects including novels, books, and short story collections
- Produces polished, publication-ready content with proper narrative structure and character development

**Features:**
- **Project Management**: Creates organized folder structures with sanitized names
- **Substantial Content**: Writes 3,000-10,000 words per story/chapter with rich detail
- **Multiple Writing Modes**: Create new files, append existing content, or overwrite when needed
- **Context Compression**: Automatically manages long conversations with intelligent summarization
- **File Organization**: Proper naming conventions and logical structure for complex projects
- **Genre Flexibility**: Handles mystery, sci-fi, romance, fantasy, horror, educational content, and more

**Best Used For:**
- **Novel Writing**: Multi-chapter books with character arcs and plot development
- **Short Story Collections**: Themed anthologies with interconnected narratives
- **Educational Content**: Comprehensive guides and instructional books
- **Creative Projects**: Any substantial writing requiring organization and quality

**Not Suitable For:**
- Very short content or summaries (other tools may be more efficient)
- Technical documentation or API references
- Real-time chat or quick responses
- Code generation or programming tasks

**Performance:**
- Average processing time: ~15-30 seconds per chapter
- Max concurrent requests: 3
- Memory per request: 1GB
- Words per request: 3,000-10,000

---

## 🐳 Docker Deployment

### Local Docker Setup

```bash
# Build and run with Docker Compose
docker-compose up --build

# Agent will be available at http://localhost:3773
```

### Docker Configuration

The agent runs on port `3773` and requires:
- `MOONSHOT_API_KEY` environment variable (recommended)
- `OPENROUTER_API_KEY` environment variable (alternative)
- `MODEL_NAME` environment variable (optional)
- `MEM0_API_KEY` environment variable (optional)

Configure these in your `.env` file before running.

### Production Deployment

```bash
# Use production compose file
docker-compose -f docker-compose.prod.yml up -d
```

---

## 🌐 Deploy to bindus.directory

Make your agent discoverable worldwide and enable agent-to-agent collaboration.

### Setup GitHub Secrets

```bash
# Authenticate with GitHub
gh auth login

# Set deployment secrets
gh secret set BINDU_API_TOKEN --body "<your-bindu-api-key>"
gh secret set DOCKERHUB_TOKEN --body "<your-dockerhub-token>"
```

Get your keys:
- **Bindu API Key**: [bindus.directory](https://bindus.directory) dashboard
- **Docker Hub Token**: [Docker Hub Security Settings](https://hub.docker.com/settings/security)

### Deploy

```bash
# Push to trigger automatic deployment
git push origin main
```

GitHub Actions will automatically:
1. Build your agent
2. Create Docker container
3. Push to Docker Hub
4. Register on bindus.directory

---

## 🛠️ Development

### Project Structure

```
writer-agent/
├── writer_agent/
│   ├── tools/                      # Custom writing tools
│   │   ├── __init__.py
│   │   ├── project.py             # Project management tool
│   │   ├── writer.py              # File writing tool
│   │   └── compression.py         # Context management tool
│   ├── skills/
│   │   └── creative_writing/       # Updated skill configuration
│   │       └── skill.yaml
│   ├── __init__.py
│   ├── __main__.py
│   ├── main.py                     # Updated agent with kimi-k2-thinking
│   └── agent_config.json           # Updated configuration
├── tests/
│   └── test_main.py
├── .env.example
├── docker-compose.yml
├── Dockerfile.agent
├── pyproject.toml                 # Updated dependencies
└── output/                         # Generated projects (created during use)
```

### Running Tests

```bash
make test              # Run all tests
make test-cov          # With coverage report
```

### Code Quality

```bash
make format            # Format code with ruff
make lint              # Run linters
make check             # Format + lint + test
```

### Pre-commit Hooks

```bash
# Install pre-commit hooks
uv run pre-commit install

# Run manually
uv run pre-commit run -a
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature` 
3. Commit your changes: `git commit -m 'Add amazing feature'` 
4. Push to the branch: `git push origin feature/amazing-feature` 
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Powered by Bindu

Built with the [Bindu Agent Framework](https://github.com/getbindu/bindu)

**Why Bindu?**
- 🌐 **Internet of Agents**: A2A, AP2, X402 protocols for agent collaboration
- ⚡ **Zero-config setup**: From idea to production in minutes
- 🛠️ **Production-ready**: Built-in deployment, monitoring, and scaling

**Build Your Own Agent:**
```bash
uvx cookiecutter https://github.com/getbindu/create-bindu-agent.git
```

---

## 📚 Resources

- 📖 [Full Documentation](https://Paraschamoli.github.io/writer-agent/)
- 💻 [GitHub Repository](https://github.com/Paraschamoli/writer-agent/)
- 🐛 [Report Issues](https://github.com/Paraschamoli/writer-agent/issues)
- 💬 [Join Discord](https://discord.gg/3w5zuYUuwt)
- 🌐 [Agent Directory](https://bindus.directory)
- 📚 [Bindu Documentation](https://docs.getbindu.com)

---

<p align="center">
  <strong>Built with 💛 by the team from Amsterdam 🌷</strong>
</p>

<p align="center">
  <a href="https://github.com/Paraschamoli/writer-agent">⭐ Star this repo</a> •
  <a href="https://discord.gg/3w5zuYUuwt">💬 Join Discord</a> •
  <a href="https://bindus.directory">🌐 Agent Directory</a>
</p>

#   w r i t e r - a g e n t  
 
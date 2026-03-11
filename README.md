<p align="center">
  <img src="https://raw.githubusercontent.com/getbindu/create-bindu-agent/refs/heads/main/assets/light.svg" alt="bindu Logo" width="200">
</p>

<h1 align="center">Writer Agent</h1>
<h3 align="center">AI-Powered Creative Writing Assistant</h3>

<p align="center">
  <strong>AI agent for generating creative short stories and fiction using Moonshot AI or OpenRouter models</strong>
</p>

<p align="center">
  <a href="https://github.com/Paraschamoli/writer-agent/actions/workflows/build-and-push.yml?query=branch%3Amain">
    <img src="https://img.shields.io/github/actions/workflow/status/Paraschamoli/writer-agent/build-and-push.yml?branch=main" alt="Build status">
  </a>
  <a href="https://img.shields.io/github/license/Paraschamoli/writer-agent">
    <img src="https://img.shields.io/github/license/Paraschamoli/writer-agent" alt="License">
  </a>
  <img src="https://img.shields.io/badge/python-3.12+-blue.svg" alt="Python Version">
</p>

---

## 📖 Overview

The Writer Agent is an AI creative writing assistant built on the [Bindu Agent Framework](https://github.com/getbindu/bindu) using the Agno framework. It generates creative fiction and short stories with project organization and file management capabilities.

**Key Features:**
- ✍️ **Creative Story Generation**: Creates complete short stories with narrative structure
- 🗂️ **Project Management**: Organized folder structure with sanitized naming
- 📝 **Markdown File Writing**: Three modes (create, append, overwrite) for content management
- 🔄 **Context Compression**: Manages long conversations with automatic summarization
- 🧠 **Optional Memory**: Mem0 integration for persistent context
- ⚡ **Flexible Models**: Supports Moonshot AI (kimi-k2-thinking) or OpenRouter models

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
| `MOONSHOT_API_KEY` | [Moonshot AI Platform](https://platform.moonshot.cn/) | ✅ For kimi models |
| `OPENROUTER_API_KEY` | [OpenRouter](https://openrouter.ai/keys) | ✅ Alternative |
| `MODEL_NAME` | Custom model name | Optional (default: kimi-k2-thinking) |
| `MEM0_API_KEY` | [Mem0 Dashboard](https://app.mem0.ai/dashboard/api-keys) | Optional |

**Model Options:**
- **Recommended**: `kimi-k2-thinking` with Moonshot API
- **Alternative**: Any OpenRouter model (e.g., `openai/gpt-4o`)

### Run the Agent

```bash
# Start the agent
uv run python -m writer_agent

# Agent will be available at http://0.0.0.0:3773
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
# Science Fiction Story
"Write a complete science fiction short story set in the year 2150 where humanity survives in floating cities above Earth after environmental collapse. The story must have a mysterious tone and focus on atmospheric world-building. The protagonist is a young orbital engineer named Mira who discovers a hidden transmission inside an abandoned satellite suggesting Earth may still be recoverable. Include emotional character development, a clear narrative arc (beginning, rising conflict, climax, twist ending), and rich descriptions of technology and floating-city life. The story must be self-contained, approximately 1200 words, written in third-person perspective, and suitable for a general adult audience."

# Fantasy Story
"Write a fantasy short story about a hidden kingdom inside a massive mountain range discovered by a wandering cartographer named Elias. The tone must be adventurous and mysterious. Include detailed descriptions of the landscape, ancient architecture, and the culture of the hidden civilization. Structure the story with a clear beginning, conflict, climax, and resolution. The story should be written in third-person narrative style, approximately 1000 words long, suitable for fantasy readers, and contain vivid world-building and character dialogue."

# Mystery Story
"Create a mystery short story with a clear narrative arc and character development"
```

### Output Structure

The agent generates organized writing projects in the `output/` directory:

```
output/your_project_name/
├── story_title.md         # Complete story in markdown
├── chapter_01.md          # If multi-file project
├── readme.md              # Project information
└── .context_summary_*.md  # Auto-saved context (if needed)
```

**Content Characteristics:**
- Markdown-formatted output
- Complete narratives with proper structure
- Character development and dialogue
- Genre-appropriate tone and style

---

## 🔌 API Usage

The agent exposes a JSON-RPC 2.0 API when running. Default endpoint: `http://0.0.0.0:3773`

### Send Message to Agent

```bash
curl --location 'http://localhost:3773' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{api_key}}' \
--data '{
  "jsonrpc": "2.0",
  "method": "message/send",
  "params": {
    "message": {
      "role": "user",
      "kind": "message",
      "messageId": "51d7a210-5616-49ad-b187-d93cbb200001",
      "contextId": "51d7a210-5616-49ad-b187-d93cbb200002",
      "taskId": "51d7a210-5616-49ad-b187-d93cbb200003",
      "parts": [
        {
          "kind": "text",
          "text": "Write a complete science fiction short story..."
        }
      ]
    },
    "skillId": "creative-writing-v1",
    "configuration": {
      "acceptedOutputModes": ["application/json"]
    }
  },
  "id": "51d7a210-5616-49ad-b187-d93cbb200003"
}'
```

### Get Task Status

```bash
curl --location 'http://localhost:3773' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{api_key}}' \
--data '{
  "jsonrpc": "2.0",
  "method": "tasks/get",
  "params": {
    "taskId": "51d7a210-5616-49ad-b187-d93cbb200003"
  },
  "id": "51d7a210-5616-49ad-b187-d93cbb200004"
}'
```

### Additional Resources

- 📖 [Full API Documentation](https://docs.getbindu.com/api-reference/all-the-tasks/send-message-to-agent)
- 📦 [Postman Collections](https://github.com/GetBindu/Bindu/tree/main/postman/collections)
- 🔧 [API Reference](https://docs.getbindu.com)

---

## 🎯 Skills

### Creative Writing (v1.0.0)

**Primary Capability:**
- Generates creative writing content using AI models with project organization
- Supports project folder creation, markdown file writing, and context compression

**Features:**
- **Project Folders**: Creates organized directories with sanitized names in `output/`
- **File Writing**: Three modes - create new files, append to existing, or overwrite
- **Context Management**: Automatic compression for long conversations
- **Memory Integration**: Optional Mem0 support for persistent context
- **Genre Flexibility**: Handles sci-fi, fantasy, mystery, and other fiction genres

**Best Used For:**
- Generating creative short stories with specific requirements
- Writing fiction with structured narrative arcs
- Creating organized writing projects with multiple files
- Tasks requiring project folder management and file organization

**Not Suitable For:**
- Real-time chat or conversational interactions
- Code generation or technical documentation
- Tasks not requiring file output or project organization
- Very short content that doesn't need project structure

**Performance:**
- Average processing time: ~15 seconds
- Memory per request: 512MB
- Output: Markdown-formatted stories

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
- `MOONSHOT_API_KEY` or `OPENROUTER_API_KEY` environment variable
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
5. Deploy to Argo CD

---

## 🛠️ Development

### Project Structure

```
writer-agent/
├── writer_agent/
│   ├── tools/                      # Custom writing tools
│   │   ├── __init__.py
│   │   ├── project.py             # Project folder management
│   │   ├── writer.py              # Markdown file writing
│   │   └── compression.py         # Context compression
│   ├── skills/
│   │   └── creative_writing/       # Skill configuration
│   │       └── skill.yaml
│   ├── __init__.py
│   ├── __main__.py
│   ├── main.py                     # Agent implementation
│   └── agent_config.json           # Agent configuration
├── tests/
│   └── test_main.py
├── .env.example
├── docker-compose.yml
├── Dockerfile.agent
├── pyproject.toml
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

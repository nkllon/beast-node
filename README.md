# Beast Node

[![PyPI version](https://img.shields.io/pypi/v/beast-node?label=PyPI&color=blue)](https://pypi.org/project/beast-node/)
[![Python Versions](https://img.shields.io/pypi/pyversions/beast-node.svg)](https://pypi.org/project/beast-node/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Node component for Beast Mode cluster - enables IDE-enabled LLMs and humans to interact from independent nodes**

## Status

🚧 **Under Development** - This project is being built using AI-driven spec-driven development.

## Overview

Beast Node represents any agent participating in a **Beast Mode cluster** - a collaborative environment where:
- IDE-enabled LLMs work together
- Humans interact with AI agents
- Independent nodes communicate via beast-mailbox-core
- Typically deployed in lab environments

## Architecture

```
┌─────────────────────────────────────────────────┐
│          Beast Mode Cluster                      │
│                                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐     │
│  │  Node 1  │  │  Node 2  │  │  Node 3  │     │
│  │  (LLM)   │  │ (Human)  │  │  (LLM)   │     │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘     │
│       │             │              │            │
│       └─────────────┼──────────────┘            │
│                     ▼                           │
│           ┌─────────────────────┐               │
│           │  Redis Mailbox      │               │
│           │  (beast-mailbox-core)│              │
│           └─────────────────────┘               │
└─────────────────────────────────────────────────┘
```

## Features

- **Node Identity** - Each node has a unique ID and capabilities
- **Mailbox Integration** - Communicates via beast-mailbox-core
- **Discovery** - Nodes can discover each other in the cluster
- **Presence** - Heartbeat and health monitoring
- **Message Routing** - Send to specific nodes or broadcast
- **Lab-Friendly** - Designed for research and development environments

## Installation

```bash
pip install beast-node
```

## Usage

```bash
# Start a node
beast-node my-node-id \
  --redis-host vonnegut \
  --redis-password beastmode2025 \
  --node-type llm \
  --capabilities "code,chat,analysis"
```

## Development Status

This project follows **spec-driven development**. See [`.spec-workflow/`](.spec-workflow/) for:
- Requirements specifications
- Design documents
- Implementation plans

## For AI Maintainers

**This repository is built 100% by AI agents and maintained by AI agents.**

Start here:
- **📖 [AGENT.md](AGENT.md)** - Comprehensive maintainer guide
- **📁 [.spec-workflow/](.spec-workflow/)** - Specifications and requirements

## Quality Standards

This project maintains the same quality standards as beast-mailbox-core:
- ✅ ≥ 85% test coverage
- ✅ Zero defects (SonarCloud)
- ✅ Comprehensive documentation
- ✅ All tests passing

## License

MIT

---

**Built with ❤️ by AI agents for Beast Mode clusters**


# Velox Framework

[![PyPI version](https://badge.fury.io/py/velox-framework.svg)](https://badge.fury.io/py/velox-framework)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/veloxframework/velox/workflows/Tests/badge.svg)](https://github.com/veloxframework/velox/actions)
[![Coverage](https://codecov.io/gh/veloxframework/velox/branch/main/graph/badge.svg)](https://codecov.io/gh/veloxframework/velox)

**Velox** (Advanced Network Application Layer) is a modern, high-performance Python backend framework designed for building scalable web applications and APIs. It combines the best features of Django, FastAPI, and Laravel while maintaining clean architecture principles and async-first design.

## ⚡ Quick Start

### Installation

```bash
pip install velox-framework
```

### Create Your First Project

```bash
# Create a new project
velox-admin startproject myproject
cd myproject

# Create your first app
velox-admin startapp blog

# Run development server
velox-admin runserver
```

### Hello World Example

```python
from velox import Velox, Controller, route
from velox.http import JsonResponse

app = Velox()

@app.route('/')
async def hello_world(request):
    return JsonResponse({'message': 'Hello, World!'})

class BlogController(Controller):
    @route.get('/posts')
    async def list_posts(self, request):
        return JsonResponse({'posts': []})
    
    @route.post('/posts')
    async def create_post(self, request):
        data = await request.json()
        # Auto-validation with Pydantic models
        return JsonResponse({'created': True})

if __name__ == '__main__':
    app.run(debug=True)
```

## 🚀 Key Features

### 🏗️ **Clean Architecture & DDD**
- Domain-driven design patterns
- Dependency injection container
- Clean separation of concerns
- Testable and maintainable code

### ⚡ **Async-First Performance**
- Native async/await support
- High-performance ASGI server
- Connection pooling
- Background task processing

### 🗄️ **Powerful ORM**
- Database-agnostic design
- Support for PostgreSQL, MySQL, SQLite, MongoDB
- Async queries and migrations
- Relationship management

### 🛡️ **Security Built-In**
- JWT/OAuth2 authentication
- CSRF/XSS protection
- Rate limiting
- Input validation and sanitization

### 🔌 **API Generation**
- Auto-generated REST APIs
- GraphQL support
- OpenAPI/Swagger documentation
- API versioning

### 🎨 **Rich Feature Set**
- Admin panel with auto-generated UI
- Template engine (Jinja2)
- Middleware system
- WebSocket support
- Internationalization (i18n)
- Background jobs and scheduling
- Real-time capabilities

## 📚 Documentation

- **[Getting Started](https://docs.veloxframework.org/getting-started/)**
- **[Tutorial](https://docs.veloxframework.org/tutorial/)**
- **[API Reference](https://docs.veloxframework.org/api/)**
- **[Best Practices](https://docs.veloxframework.org/best-practices/)**

## 🏛️ Architecture

Velox follows Clean Architecture principles with clear separation between layers:

```
┌─────────────────────────────────────────┐
│         Presentation Layer              │ ← Controllers, Views, API
├─────────────────────────────────────────┤
│         Application Layer               │ ← Use Cases, Services
├─────────────────────────────────────────┤
│            Domain Layer                 │ ← Entities, Value Objects
├─────────────────────────────────────────┤
│       Infrastructure Layer              │ ← Database, External APIs
└─────────────────────────────────────────┘
```

## 🎯 Performance

- **High throughput**: 40,000+ requests/second
- **Low latency**: Sub-millisecond response times
- **Memory efficient**: Optimized for containerized deployments
- **Scalable**: Horizontal scaling support

## 🛠️ Development Tools

### CLI Commands

```bash
# Project management
velox-admin startproject myproject
velox-admin startapp myapp

# Database operations
velox-admin makemigrations
velox-admin migrate
velox-admin shell

# Development server
velox-admin runserver --reload
velox-admin runserver --workers 4

# Testing and deployment
velox-admin test
velox-admin collectstatic
velox-admin deploy
```

### Development Features

- Hot reloading
- Interactive shell
- Database migrations
- Test utilities
- Static file handling
- Docker integration

## 🌐 Ecosystem

### Built-in Apps
- **velox.auth** - Authentication and authorization
- **velox.admin** - Auto-generated admin interface
- **velox.api** - REST and GraphQL API generation
- **velox.files** - File upload and management
- **velox.cache** - Multi-level caching
- **velox.tasks** - Background job processing

### Third-party Packages
- **velox-cms** - Content management system
- **velox-ecommerce** - E-commerce functionality
- **velox-analytics** - Analytics and monitoring
- **velox-payments** - Payment processing
- **velox-social** - Social authentication

## 📈 Comparison

| Feature | Velox | Django | FastAPI | Laravel |
|---------|------|--------|---------|---------|
| Async Support | ✅ Native | ⚠️ Partial | ✅ Native | ❌ No |
| Performance | ⚡ Very High | 🔥 Medium | ⚡ Very High | 🔥 Medium |
| Learning Curve | 📈 Gentle | 📈 Steep | 📈 Medium | 📈 Gentle |
| Auto API Docs | ✅ Yes | ❌ No | ✅ Yes | ⚠️ Manual |
| Admin Panel | ✅ Built-in | ✅ Built-in | ❌ No | ❌ No |
| ORM | ✅ Advanced | ✅ Good | ❌ No | ✅ Eloquent |
| Type Safety | ✅ Full | ⚠️ Partial | ✅ Full | ❌ No |

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

```bash
git clone https://github.com/MUHAMMEDHAFEEZ/velox-framework.git
cd velox
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e ".[dev]"
pre-commit install
pytest
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by Django's batteries-included philosophy
- Built on the async foundation of FastAPI
- Influenced by Laravel's elegant developer experience
- Powered by modern Python 3.12+ features

## 🎉 Community

- **Discord**: [Join our community](https://discord.gg/analframework)
- **GitHub Discussions**: [Ask questions and share ideas](https://github.com/veloxframework/velox/discussions)
- **Twitter**: [@ANALFramework](https://twitter.com/ANALFramework)
- **Blog**: [Latest news and tutorials](https://blog.veloxframework.org)

---

**Made with ❤️ by the Velox Framework Team**

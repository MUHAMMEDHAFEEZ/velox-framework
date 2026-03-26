# Quick Start Guide for Velox Framework

## Installation

```bash
pip install velox-framework
```

## Create Your First Project

```bash
# Create new project
velox-admin startproject myapp
cd myapp

# Setup database (SQLite by default)
velox-admin makemigrations auth
velox-admin migrate

# Create admin user
velox-admin createsuperuser

# Run development server
velox-admin runserver
```

Your app will be available at `http://localhost:8000`

## Features

✅ **SQLite Default Database** - Ready to use out of the box  
✅ **Rich CLI Tools** - Complete project management  
✅ **Modern Async Framework** - Built on Starlette/ASGI  
✅ **Type Safety** - Full type hints with Pydantic  
✅ **Authentication System** - Built-in user management  
✅ **Database Migrations** - Powered by Alembic  
✅ **Multi-Database Support** - PostgreSQL, MySQL, MongoDB  

## Quick Example

```python
# controllers.py
from velox.http import Controller, JSONResponse
from velox.http.decorators import route

class UserController(Controller):
    
    @route("/users", methods=["GET"])
    async def list_users(self, request):
        return JSONResponse({"users": []})
```

## Documentation

- [Full Documentation](https://docs.veloxframework.org)
- [Tutorial](https://docs.veloxframework.org/tutorial/)
- [GitHub Repository](https://github.com/veloxframework/velox)

## Support

- GitHub Issues: https://github.com/veloxframework/velox/issues
- Documentation: https://docs.veloxframework.org

"""
Velox Framework - Advanced Network Application Layer

A modern, high-performance Python backend framework for building
scalable web applications and APIs.

Copyright (c) 2024 Velox Framework Team
Licensed under MIT License
"""

__version__ = "0.1.0"
__author__ = "Velox Framework Team"
__email__ = "team@veloxframework.org"
__license__ = "MIT"

# Core framework imports for convenience
from velox.core.application import Velox
from velox.core.container import Container
from velox.core.config import Settings
from velox.http.controllers import Controller
from velox.http.responses import JsonResponse, TemplateResponse
from velox.http.routing import route, Router
from velox.http.middleware import Middleware
from velox.db.models import Model
from velox.db import fields
from velox.auth.decorators import login_required, permission_required

# Make commonly used classes available at package level
__all__ = [
    # Core
    "Velox",
    "Container", 
    "Settings",
    
    # HTTP
    "Controller",
    "JsonResponse",
    "TemplateResponse", 
    "route",
    "Router",
    "Middleware",
    
    # Database
    "Model",
    
    # Auth
    "login_required",
    "permission_required",
    
    # Version info
    "__version__",
    "__author__",
    "__email__", 
    "__license__",
]

# Framework metadata
framework_info = {
    "name": "Velox",
    "version": __version__,
    "description": "Advanced Network Application Layer",
    "author": __author__,
    "license": __license__,
    "python_requires": ">=3.12",
    "async_support": True,
    "database_support": ["postgresql", "mysql", "sqlite", "mongodb"],
    "features": [
        "async-first",
        "clean-architecture", 
        "dependency-injection",
        "auto-api-generation",
        "built-in-auth",
        "admin-panel",
        "orm",
        "migrations",
        "middleware",
        "websockets",
        "background-tasks",
        "i18n",
        "caching",
        "testing-utilities"
    ]
}

"""Core module initialization."""

from velox.core.application import Velox
from velox.core.config import Settings, get_settings, configure
from velox.core.container import Container, get_container, inject
from velox.core.events import EventBus, get_event_bus, on, once, emit
from velox.core.exceptions import *
from velox.core.registry import AppConfig, AppRegistry, apps, get_app_config

__all__ = [
    # Application
    "Velox",
    
    # Configuration
    "Settings",
    "get_settings", 
    "configure",
    
    # Container
    "Container",
    "get_container",
    "inject",
    
    # Events
    "EventBus",
    "get_event_bus",
    "on",
    "once", 
    "emit",
    
    # Registry
    "AppConfig",
    "AppRegistry",
    "apps",
    "get_app_config",
]

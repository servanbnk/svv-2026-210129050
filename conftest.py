"""Pytest configuration and fixtures for SVV coursework.

Provides math_utils, text_utils, and business_utils fixtures dynamically loaded
from reference_lib (clean) or student_build/<id> (seeded) depending on the
TARGET_LIB environment variable.
"""
import os
import sys
import importlib.util
from pathlib import Path
import pytest

ROOT_DIR = Path(__file__).parent.resolve()

def _load_module(module_name: str):
    target = os.environ.get("TARGET_LIB")
    if target:
        module_path = ROOT_DIR / target / f"{module_name}.py"
    else:
        module_path = ROOT_DIR / "reference_lib" / f"{module_name}.py"

    if not module_path.exists():
        raise FileNotFoundError(f"Could not find module at {module_path}")

    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def business_utils():
    """Fixture providing the business_utils module."""
    return _load_module("business_utils")


@pytest.fixture
def math_utils():
    """Fixture providing the math_utils module."""
    return _load_module("math_utils")


@pytest.fixture
def text_utils():
    """Fixture providing the text_utils module."""
    return _load_module("text_utils")

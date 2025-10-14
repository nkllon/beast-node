"""Basic tests to verify setup."""

import beast_node


def test_version():
    """Test that version is defined."""
    assert hasattr(beast_node, "__version__")
    assert beast_node.__version__ == "0.1.0"


def test_import():
    """Test that package can be imported."""
    assert beast_node is not None


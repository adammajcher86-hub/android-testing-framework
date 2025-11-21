"""
PyTest configuration and fixtures for Android testing
"""

import pytest
import logging
from utils.driver_factory import DriverFactory

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def driver():
    """
    Fixture that provides Appium driver for each test

    Scope: function - creates new driver for each test
    """
    logger.info("Setting up driver for test")
    driver = DriverFactory.get_driver()

    yield driver  # Test runs here

    logger.info("Tearing down driver after test")
    DriverFactory.quit_driver()


@pytest.fixture(scope="session", autouse=True)
def test_session_setup():
    """Setup that runs once before all tests"""
    logger.info("=" * 80)
    logger.info("STARTING TEST SESSION")
    logger.info("=" * 80)

    yield

    logger.info("=" * 80)
    logger.info("TEST SESSION COMPLETE")
    logger.info("=" * 80)


@pytest.fixture(scope="function", autouse=True)
def test_info(request):
    """Log test information before each test"""
    logger.info(f"\n{'=' * 80}")
    logger.info(f"TEST: {request.node.name}")
    logger.info(f"{'=' * 80}\n")

    yield

    logger.info(f"\nTest '{request.node.name}' completed\n")

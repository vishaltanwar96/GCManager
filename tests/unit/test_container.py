import os
from unittest import TestCase

from kink.container import Container

from gcmanager.dependencies import build_dependency_container
from gcmanager.exceptions import ImproperlyConfigured


class TestDependencyContainer(TestCase):
    def test_raises_exception_when_required_env_variables_absent(self) -> None:
        os.environ["APP_ENV"] = "PROD"
        os.environ["MONGODB_PORT"] = "27017"
        os.environ["MONGODB_DBNAME"] = "gcmanager"
        os.environ["MONGODB_GC_COLLECTION_NAME"] = "giftcards"
        with self.assertRaises(ImproperlyConfigured):
            build_dependency_container()

    def test_returns_container_when_required_env_variables_present(self) -> None:
        os.environ["APP_ENV"] = "PROD"
        os.environ["MONGODB_USERNAME"] = "testing_user"
        os.environ["MONGODB_PASSWORD"] = "testing"
        os.environ["MONGODB_HOST"] = "localhost"
        os.environ["MONGODB_PORT"] = "27020"
        os.environ["MONGODB_DBNAME"] = "testdb"
        os.environ["MONGODB_GC_COLLECTION_NAME"] = "testcollection"
        self.assertIsInstance(build_dependency_container(), Container)

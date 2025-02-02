# coding=utf-8
from unittest import TestCase

from components.repositories_manager import RepositoriesManager


class TestRepositoriesManager(TestCase):
    def setUp(self):
        self.repositories_manager = RepositoriesManager('test.test_repositories')

    def test_get_existing_extractor(self):
        self.repositories_manager.get_extractor_instance('ValidExtractor')

    def test_attempt_to_get_non_existent_extractor(self):
        self.assertRaises(ImportError, self.repositories_manager.get_extractor_instance, 'NonExistentExtractorModule')

    def test_attempt_to_get_extractor_with_different_class_name(self):
        self.assertRaises(AttributeError, self.repositories_manager.get_extractor_instance, 'InvalidExtractor')

    def test_attempt_to_get_extractor_that_does_not_implement_the_interface(self):
        self.assertRaises(TypeError, self.repositories_manager.get_extractor_instance, 'InvalidExtractor2')

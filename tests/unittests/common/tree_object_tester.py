from dataclasses import dataclass
from typing import Any, Dict, List, Tuple

import pytest

from .compare import assert_allclose


@dataclass
class ObjectPropertiesToTest:
    read_write: List[Tuple[str, Any]]
    read_only: List[Tuple[str, Any]]


class TreeObjectTesterReadOnly:
    @staticmethod
    def test_collection_len(collection_test_data):
        """Test the ``len()`` method of the object collection."""
        object_collection, object_names, object_ids = collection_test_data
        assert len(object_collection) == len(object_names) == len(object_ids)

    @staticmethod
    def test_collection_values(collection_test_data):
        """Test the ``values()`` method of the object collection."""
        object_collection, object_names, _ = collection_test_data
        assert set(object_names) == {obj.name for obj in object_collection.values()}

    @staticmethod
    def test_collection_keys(collection_test_data):
        """Test the ``keys()`` method of the object collection."""
        object_collection, _, object_ids = collection_test_data
        assert set(object_ids) == set(object_collection) == set(object_collection.keys())

    @staticmethod
    def test_collection_contains(collection_test_data):
        """Test the ``__contains__()`` method of the object collection."""
        object_collection, _, object_ids = collection_test_data
        for id in object_ids:
            assert id in object_collection

    @staticmethod
    def test_collection_items(collection_test_data):
        """Test the ``items()`` method of the object collection."""
        object_collection, object_names, object_ids = collection_test_data
        object_names_fromitems = []
        object_ids_fromitems = []
        for key, value in object_collection.items():
            object_names_fromitems.append(value.name)
            object_ids_fromitems.append(key)
            assert key == value.id

        for name in object_names:
            assert name in object_names_fromitems
        for id in object_ids:
            assert id in object_ids_fromitems

    @staticmethod
    def test_collection_getitem(collection_test_data):
        """Test item access of the object collection."""
        object_collection, _, object_ids = collection_test_data
        ref_id = object_ids[0]

        assert object_collection[ref_id].id == ref_id
        assert object_collection.get(ref_id).id == ref_id

    @staticmethod
    def test_collection_getitem_inexistent(collection_test_data):
        """Test item access for keys that don't exist."""
        object_collection, _, _ = collection_test_data

        INEXISTENT_ID = "Inexistent ID"
        with pytest.raises(KeyError):
            object_collection[INEXISTENT_ID]
        assert object_collection.get(INEXISTENT_ID) is None


class TreeObjectTester(TreeObjectTesterReadOnly):
    COLLECTION_NAME: str
    DEFAULT_PROPERTIES: Dict[str, Any]
    CREATE_METHOD_NAME: str

    def test_create(self, parent_object):
        """Test the creation of objects."""
        create_method = getattr(parent_object, self.CREATE_METHOD_NAME)
        names = ["ObjectName.1", "ObjectName.1", "üñıçよð€"]
        for ref_name in names:
            new_object = create_method(name=ref_name)
            assert new_object.name == ref_name
            for key, val in self.DEFAULT_PROPERTIES.items():
                assert_allclose(
                    actual=getattr(new_object, key),
                    desired=val,
                    msg=f"Attribute {key} not set correctly. Expected {val}, got {getattr(new_object, key)}",
                ),

    @staticmethod
    def test_properties(tree_object, object_properties: ObjectPropertiesToTest):
        for prop, value in object_properties.read_write:
            setattr(tree_object, prop, value)
            assert_allclose(
                actual=getattr(tree_object, prop),
                desired=value,
            )

        for prop, value in object_properties.read_only:
            with pytest.raises(AttributeError):
                setattr(tree_object, prop, value)

        for prop, _ in object_properties.read_only + object_properties.read_write:
            assert f"{prop}=" in str(
                tree_object
            ), f"{prop} not found in object string: {str(tree_object)}"

    @staticmethod
    def test_collection_delitem(collection_test_data):
        """Test deleting items in the object collection."""
        object_collection, _, object_ids = collection_test_data
        # Use the last object, since it is definitely not locked.
        ref_id = object_ids[-1]

        del object_collection[ref_id]
        with pytest.raises(KeyError):
            object_collection[ref_id]


class NoLockedMixin:
    @pytest.fixture
    def collection_test_data(self, parent_object):
        object_collection = getattr(parent_object, self.COLLECTION_NAME)
        object_collection.clear()
        object_names = ["ObjectName.1", "ObjectName.1", "üñıçよð€"]
        object_ids = []
        for ref_name in object_names:
            new_object = getattr(parent_object, self.CREATE_METHOD_NAME)(name=ref_name)
            assert new_object.id not in object_ids  # check uniqueness
            object_ids.append(new_object.id)
        return object_collection, object_names, object_ids

    @staticmethod
    def test_collection_clear(collection_test_data):
        """Test clearing the object collection."""
        object_collection, _, _ = collection_test_data
        object_collection.clear()
        assert len(object_collection) == 0


class WithLockedMixin:
    INITIAL_OBJECT_NAMES: Tuple[str, ...]

    @pytest.fixture
    def collection_test_data(self, parent_object):
        object_collection = getattr(parent_object, self.COLLECTION_NAME)
        new_object_names = ["ObjectName.1", "ObjectName.1", "üñıçよð€"]
        object_ids = list(object_collection)
        for ref_name in new_object_names:
            new_object = getattr(parent_object, self.CREATE_METHOD_NAME)(name=ref_name)
            assert new_object.id not in object_ids  # check uniqueness
            object_ids.append(new_object.id)
        object_names = list(self.INITIAL_OBJECT_NAMES) + new_object_names
        return object_collection, object_names, object_ids

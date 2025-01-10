# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from dataclasses import dataclass
from typing import Any

import pytest

from .compare import assert_allclose


@dataclass
class PropertyWithConversion:
    """A class to store a property which is converted when set."""

    initial_value: Any
    converted_value: Any


@dataclass
class PropertyWithCustomComparison:
    """A class to store a property which is compared using a custom function."""

    initial_value: Any
    comparison_function: Any


@dataclass
class ObjectPropertiesToTest:
    read_write: list[tuple[str, Any]]
    read_only: list[tuple[str, Any]]
    # If create_args do not exist, the create method will use read-write properties
    # to create the object
    # Note: the read-write properties can contain the same property twice, with different values.
    # The last value will be used to create the object.
    # If create_args exists the create method will use the create_args dictionaries
    # to create the object. The object
    # will be created for each dictionary in the list.
    create_args: list[dict[str, Any]] | None = None


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

    @staticmethod
    def test_parent_access(collection_test_data, parent_object):
        """Test the parent access of the objects in the collection."""
        object_collection, _, object_ids = collection_test_data
        ref_id = object_ids[0]

        assert object_collection[ref_id].parent is parent_object


class TreeObjectTester(TreeObjectTesterReadOnly):
    COLLECTION_NAME: str
    CREATE_METHOD_NAME: str

    def test_create_with_default_arguments(self, parent_object, default_properties):
        """Test the creation of objects with default arguments."""
        create_method = getattr(parent_object, self.CREATE_METHOD_NAME)
        names = ["ObjectName.1", "ObjectName.1", "üñıçよð€"]
        for ref_name in names:
            new_object = create_method(name=ref_name)
            assert new_object.name == ref_name
            for key, val in default_properties.items():
                assert_allclose(
                    actual=getattr(new_object, key),
                    desired=val,
                    msg=f"Attribute {key} not set correctly. Expected {val}, got {getattr(new_object, key)}",
                ),

    def test_create_with_defined_properties(
        self, parent_object, object_properties: ObjectPropertiesToTest
    ):
        """Test the creation of objects with properties defined in object_properties."""

        def create_and_check(init_args: dict[str, Any]):
            create_method = getattr(parent_object, self.CREATE_METHOD_NAME)
            init_args_final = {
                key: getattr(val, "initial_value", val) for key, val in init_args.items()
            }

            new_object = create_method(**init_args_final)
            for key, val in init_args.items():
                if isinstance(val, PropertyWithCustomComparison):
                    assert val.comparison_function(getattr(new_object, key), val.initial_value)
                    continue
                if isinstance(val, PropertyWithConversion):
                    val = val.converted_value
                assert_allclose(
                    actual=getattr(new_object, key),
                    desired=val,
                    msg=f"Attribute {key} not set correctly. Expected {val}, got {getattr(new_object, key)}",
                ),

        if object_properties.create_args is None:
            # Note: The object_properties.read_write can contain the same property twice,
            # with different values. By converting it to a dictionary, we just keep the last value
            # that was set and use it to construct the object.
            init_args = {key: value for key, value in object_properties.read_write}
            create_and_check(init_args)
        else:
            assert object_properties.create_args is not None
            for init_args in object_properties.create_args:
                create_and_check(init_args)

    @staticmethod
    def test_properties(tree_object, object_properties: ObjectPropertiesToTest):
        for prop, value in object_properties.read_write:
            if isinstance(value, PropertyWithConversion):
                initial_value = value.initial_value
                converted_value = value.converted_value
            elif isinstance(value, PropertyWithCustomComparison):
                initial_value = converted_value = value.initial_value
            else:
                initial_value = converted_value = value
            setattr(tree_object, prop, initial_value)
            if isinstance(value, PropertyWithCustomComparison):
                assert value.comparison_function(getattr(tree_object, prop), converted_value)
            else:
                assert_allclose(
                    actual=getattr(tree_object, prop),
                    desired=converted_value,
                )

        for prop, value in object_properties.read_only:
            getattr(
                tree_object, prop
            ), f"Cannot get read-only property '{prop}' of object '{tree_object}'"
            with pytest.raises(AttributeError):
                setattr(tree_object, prop, value)

        string_representation = str(tree_object)
        for prop, _ in object_properties.read_only + object_properties.read_write:
            assert (
                f"{prop}=" in string_representation
            ), f"{prop} not found in object string: {string_representation}"

    @staticmethod
    def test_collection_delitem(collection_test_data):
        """Test deleting items in the object collection."""
        object_collection, _, object_ids = collection_test_data
        # Use the last object, since it is definitely not locked.
        ref_id = object_ids[-1]

        del object_collection[ref_id]
        with pytest.raises(KeyError):
            object_collection[ref_id]

    @staticmethod
    def test_unstored_parent_access_raises(collection_test_data):
        """Test that unstored objects raise an error when accessing the parent."""
        object_collection, _, object_ids = collection_test_data
        ref_id = object_ids[0]
        object = object_collection[ref_id].clone()
        with pytest.raises(RuntimeError) as exc:
            object.parent
        assert "unstored" in str(exc.value)
        assert "parent" in str(exc.value)


class NoLockedMixin(TreeObjectTester):
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


class WithLockedMixin(TreeObjectTester):
    INITIAL_OBJECT_NAMES: tuple[str, ...]

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

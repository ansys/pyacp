from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Callable

if TYPE_CHECKING:
    from mypy_extensions import DefaultNamedArg, KwArg

import pytest


@dataclass
class LinkedObjectListTestCase:
    parent_object: Any
    linked_attribute_name: str
    existing_linked_object_names: tuple[str, ...]
    linked_object_constructor: Callable[[DefaultNamedArg(type=str, name="name"), KwArg(Any)], Any]


class LinkedObjectListTester:
    """Tests for object attributes which link to multiple other objects, as a list."""

    @staticmethod
    def test_iter(linked_object_case: LinkedObjectListTestCase):
        """
        Test iterating through the linked objects.
        """
        linked_object_list = getattr(
            linked_object_case.parent_object, linked_object_case.linked_attribute_name
        )
        assert len(linked_object_list) == len(linked_object_case.existing_linked_object_names)
        assert [obj.name for obj in linked_object_list] == list(
            linked_object_case.existing_linked_object_names
        )

    @staticmethod
    def test_getitem_first(linked_object_case_nonempty: LinkedObjectListTestCase):
        """
        Test accessing the first linked object.
        """
        linked_object_list = getattr(
            linked_object_case_nonempty.parent_object,
            linked_object_case_nonempty.linked_attribute_name,
        )

        assert (
            linked_object_list[0].name
            == linked_object_case_nonempty.existing_linked_object_names[0]
        )

    @staticmethod
    def test_getitem_negative_index(linked_object_case_nonempty: LinkedObjectListTestCase):
        """
        Test accessing the last linked object, with negative indexing.
        """
        linked_object_list = getattr(
            linked_object_case_nonempty.parent_object,
            linked_object_case_nonempty.linked_attribute_name,
        )

        assert (
            linked_object_list[-1].name
            == linked_object_case_nonempty.existing_linked_object_names[-1]
        )

    @staticmethod
    def test_getitem_full_slice(linked_object_case_nonempty: LinkedObjectListTestCase):
        """
        Test accessing all objects, with a slice ``[:]``.
        """
        linked_object_list = getattr(
            linked_object_case_nonempty.parent_object,
            linked_object_case_nonempty.linked_attribute_name,
        )

        assert [obj.name for obj in linked_object_list[:]] == list(
            linked_object_case_nonempty.existing_linked_object_names
        )

    @staticmethod
    def test_setitem_zero(linked_object_case_nonempty: LinkedObjectListTestCase):
        """
        Test replacing the first linked item.
        """
        linked_object_list = getattr(
            linked_object_case_nonempty.parent_object,
            linked_object_case_nonempty.linked_attribute_name,
        )

        new_obj = linked_object_case_nonempty.linked_object_constructor(name="New Object")
        linked_object_list[0] = new_obj

        assert (
            getattr(
                linked_object_case_nonempty.parent_object,
                linked_object_case_nonempty.linked_attribute_name,
            )[0].name
            == "New Object"
        )

    @staticmethod
    def test_delitem_slice(linked_object_case_nonempty: LinkedObjectListTestCase):
        """
        Test removing all linked items, via ``del`` with a slice.
        """
        linked_object_list = getattr(
            linked_object_case_nonempty.parent_object,
            linked_object_case_nonempty.linked_attribute_name,
        )

        assert (
            len(
                getattr(
                    linked_object_case_nonempty.parent_object,
                    linked_object_case_nonempty.linked_attribute_name,
                )
            )
            != 0
        )
        del linked_object_list[:]

        assert (
            len(
                getattr(
                    linked_object_case_nonempty.parent_object,
                    linked_object_case_nonempty.linked_attribute_name,
                )
            )
            == 0
        )

    @staticmethod
    def test_append(linked_object_case: LinkedObjectListTestCase):
        """
        Test adding linked items via ``.append()``
        """
        linked_object_list = getattr(
            linked_object_case.parent_object, linked_object_case.linked_attribute_name
        )
        expected_names = list(linked_object_case.existing_linked_object_names)
        for _ in range(10):
            new_child = linked_object_case.linked_object_constructor()
            linked_object_list.append(new_child)
            expected_names.append(new_child.name)

        # reload the 'linked_object_list' from the parent, to ensure the values are
        # propagated through
        linked_object_list = getattr(
            linked_object_case.parent_object, linked_object_case.linked_attribute_name
        )
        assert [obj.name for obj in linked_object_list] == expected_names

    @staticmethod
    def test_extend(linked_object_case: LinkedObjectListTestCase):
        """
        Test adding linked items via ``.extend()``
        """
        linked_object_list = getattr(
            linked_object_case.parent_object, linked_object_case.linked_attribute_name
        )
        expected_names = list(linked_object_case.existing_linked_object_names)
        new_objects = []
        for _ in range(10):
            new_child = linked_object_case.linked_object_constructor()
            expected_names.append(new_child.name)
            new_objects.append(new_child)

        linked_object_list.extend(new_objects)

        # reload the 'linked_object_list' from the parent, to ensure the values are
        # propagated through
        linked_object_list = getattr(
            linked_object_case.parent_object, linked_object_case.linked_attribute_name
        )
        assert [obj.name for obj in linked_object_list] == expected_names

    @staticmethod
    def test_append_unstored(linked_object_case_empty: LinkedObjectListTestCase):
        """
        Test that adding unstored linked items raises an error.
        """
        linked_object_list = getattr(
            linked_object_case_empty.parent_object, linked_object_case_empty.linked_attribute_name
        )
        child_unstored = linked_object_case_empty.linked_object_constructor().clone()
        with pytest.raises(RuntimeError):
            linked_object_list.append(child_unstored)

    @staticmethod
    def test_sort_by_name(linked_object_case_empty: LinkedObjectListTestCase):
        """
        Test that the linked objects can be sorted via ``.sort()``.
        """
        parent_object = linked_object_case_empty.parent_object
        linked_attribute_name = linked_object_case_empty.linked_attribute_name
        names_unsorted = ["A", "Z", "C", "F", "B"]

        child_objects = [
            linked_object_case_empty.linked_object_constructor(name=name) for name in names_unsorted
        ]
        setattr(parent_object, linked_attribute_name, child_objects)

        assert [obj.name for obj in getattr(parent_object, linked_attribute_name)] == names_unsorted

        getattr(parent_object, linked_attribute_name).sort()
        assert [obj.name for obj in getattr(parent_object, linked_attribute_name)] == sorted(
            names_unsorted
        )

        getattr(parent_object, linked_attribute_name).sort(reverse=True)
        assert [obj.name for obj in getattr(parent_object, linked_attribute_name)] == sorted(
            names_unsorted, reverse=True
        )

    @staticmethod
    def test_reverse(linked_object_case_empty: LinkedObjectListTestCase):
        """
        Test that the order of linked objects can be reversed.
        """
        parent_object = linked_object_case_empty.parent_object
        linked_attribute_name = linked_object_case_empty.linked_attribute_name

        names_initial = ["A", "Z", "C", "F", "B"]

        child_objects = [
            linked_object_case_empty.linked_object_constructor(name=name) for name in names_initial
        ]
        setattr(parent_object, linked_attribute_name, child_objects)

        assert [obj.name for obj in getattr(parent_object, linked_attribute_name)] == names_initial

        getattr(parent_object, linked_attribute_name).reverse()
        assert [obj.name for obj in getattr(parent_object, linked_attribute_name)] == list(
            reversed(names_initial)
        )

    @staticmethod
    def test_reversed_iter(linked_object_case_empty: LinkedObjectListTestCase):
        """
        Test that the linked objects can be iterated over in reverse order.
        """
        parent_object = linked_object_case_empty.parent_object
        linked_attribute_name = linked_object_case_empty.linked_attribute_name

        names_initial = ["A", "Z", "C", "F", "B"]

        child_objects = [
            linked_object_case_empty.linked_object_constructor(name=name) for name in names_initial
        ]
        setattr(parent_object, linked_attribute_name, child_objects)

        total_count = 0
        for expected_name, obj in zip(
            reversed(names_initial), reversed(getattr(parent_object, linked_attribute_name))
        ):
            assert obj.name == expected_name
            total_count += 1
        assert total_count == len(names_initial)

    @staticmethod
    def test_contains(linked_object_case_empty: LinkedObjectListTestCase):
        """
        Test the ``object in container`` check.
        """
        parent_object = linked_object_case_empty.parent_object
        linked_attribute_name = linked_object_case_empty.linked_attribute_name
        linked_object_constructor = linked_object_case_empty.linked_object_constructor

        objects_linked = []
        for _ in range(3):
            objects_linked.append(linked_object_constructor())
        setattr(parent_object, linked_attribute_name, objects_linked)

        objects_not_linked = []
        for _ in range(3):
            objects_not_linked.append(linked_object_constructor())

        assert all(obj in getattr(parent_object, linked_attribute_name) for obj in objects_linked)
        assert all(
            obj not in getattr(parent_object, linked_attribute_name) for obj in objects_not_linked
        )

    @staticmethod
    def test_count(linked_object_case_empty: LinkedObjectListTestCase):
        """
        Test the ``container.count(obj)`` method.
        """
        parent_object = linked_object_case_empty.parent_object
        linked_attribute_name = linked_object_case_empty.linked_attribute_name
        linked_object_constructor = linked_object_case_empty.linked_object_constructor

        objects_linked = []
        for _ in range(3):
            objects_linked.append(linked_object_constructor())
        setattr(parent_object, linked_attribute_name, objects_linked)

        objects_not_linked = []
        for _ in range(3):
            objects_not_linked.append(linked_object_constructor())

        assert all(
            getattr(parent_object, linked_attribute_name).count(obj) == 1 for obj in objects_linked
        )
        assert all(
            getattr(parent_object, linked_attribute_name).count(obj) == 0
            for obj in objects_not_linked
        )

    @staticmethod
    def test_index(linked_object_case_empty: LinkedObjectListTestCase):
        """
        Test that objects in the linked objects list can be found via ``.index()``.
        """
        parent_object = linked_object_case_empty.parent_object
        linked_attribute_name = linked_object_case_empty.linked_attribute_name
        linked_object_constructor = linked_object_case_empty.linked_object_constructor

        objects_linked = []
        for _ in range(3):
            objects_linked.append(linked_object_constructor())
        setattr(parent_object, linked_attribute_name, objects_linked)

        objects_not_linked = []
        for _ in range(3):
            objects_not_linked.append(linked_object_constructor())

        for i, obj in enumerate(objects_linked):
            assert getattr(parent_object, linked_attribute_name).index(obj) == i

        for obj in objects_not_linked:
            with pytest.raises(ValueError):
                getattr(parent_object, linked_attribute_name).index(obj)

    @staticmethod
    def test_insert(linked_object_case_empty: LinkedObjectListTestCase):
        """
        Test that the linked objects list can be inserted into.
        """
        parent_object = linked_object_case_empty.parent_object
        linked_attribute_name = linked_object_case_empty.linked_attribute_name
        linked_object_constructor = linked_object_case_empty.linked_object_constructor

        names_initial = ["A", "B", "C", "D"]

        child_objects = [linked_object_constructor(name=name) for name in names_initial]

        assert [obj.name for obj in getattr(parent_object, linked_attribute_name)] == []

        getattr(parent_object, linked_attribute_name).insert(0, child_objects[0])
        assert [obj.name for obj in getattr(parent_object, linked_attribute_name)] == ["A"]

        getattr(parent_object, linked_attribute_name).insert(0, child_objects[1])
        assert [obj.name for obj in getattr(parent_object, linked_attribute_name)] == ["B", "A"]

        getattr(parent_object, linked_attribute_name).insert(-1, child_objects[2])
        assert [obj.name for obj in getattr(parent_object, linked_attribute_name)] == [
            "B",
            "C",
            "A",
        ]

        getattr(parent_object, linked_attribute_name).insert(1, child_objects[3])
        assert [obj.name for obj in getattr(parent_object, linked_attribute_name)] == [
            "B",
            "D",
            "C",
            "A",
        ]

    @staticmethod
    def test_remove(linked_object_case_empty: LinkedObjectListTestCase):
        """
        Test objects can be removed by index.
        """
        parent_object = linked_object_case_empty.parent_object
        linked_attribute_name = linked_object_case_empty.linked_attribute_name
        linked_object_constructor = linked_object_case_empty.linked_object_constructor

        names_initial = ["A", "Z", "C", "F", "B"]

        child_objects = [linked_object_constructor(name=name) for name in names_initial]
        setattr(parent_object, linked_attribute_name, child_objects)

        getattr(parent_object, linked_attribute_name).remove(child_objects[2])
        assert [obj.name for obj in getattr(parent_object, linked_attribute_name)] == [
            "A",
            "Z",
            "F",
            "B",
        ]

    @staticmethod
    def test_pop(linked_object_case_empty: LinkedObjectListTestCase):
        """
        Test objects can be removed + returned by index, with ``.pop()``.
        """
        parent_object = linked_object_case_empty.parent_object
        linked_attribute_name = linked_object_case_empty.linked_attribute_name
        linked_object_constructor = linked_object_case_empty.linked_object_constructor

        names_initial = ["A", "Z", "C", "F", "B"]

        child_objects = [linked_object_constructor(name=name) for name in names_initial]
        setattr(parent_object, linked_attribute_name, child_objects)

        last_obj = getattr(parent_object, linked_attribute_name).pop()
        assert [obj.name for obj in getattr(parent_object, linked_attribute_name)] == [
            "A",
            "Z",
            "C",
            "F",
        ]
        assert last_obj.name == "B"

        removed_obj = getattr(parent_object, linked_attribute_name).pop(1)
        assert [obj.name for obj in getattr(parent_object, linked_attribute_name)] == [
            "A",
            "C",
            "F",
        ]
        assert removed_obj.name == "Z"

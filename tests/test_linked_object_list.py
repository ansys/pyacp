import pytest
from pytest_cases import parametrize_with_cases


def case_oss_to_elset_one_existing(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        oss = model.oriented_selection_sets["OrientedSelectionSet.1"]
        yield oss, "element_sets", tuple(["All_Elements"]), model.create_element_set


def case_oss_to_elset_empty(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        oss = model.create_oriented_selection_set()
        yield oss, "element_sets", tuple(), model.create_element_set


@parametrize_with_cases(
    "parent_object, list_attribute, expected_initial_names, child_constructor", cases="."
)
def test_iter(parent_object, list_attribute, expected_initial_names, child_constructor):
    linked_object_list = getattr(parent_object, list_attribute)
    assert len(linked_object_list) == len(expected_initial_names)
    assert [obj.name for obj in linked_object_list] == list(expected_initial_names)


@parametrize_with_cases(
    "parent_object, list_attribute, expected_initial_names, child_constructor",
    cases=".",
    glob="*existing",
)
def test_getitem_first(parent_object, list_attribute, expected_initial_names, child_constructor):
    linked_object_list = getattr(parent_object, list_attribute)

    assert linked_object_list[0].name == expected_initial_names[0]


@parametrize_with_cases(
    "parent_object, list_attribute, expected_initial_names, child_constructor",
    cases=".",
    glob="*existing",
)
def test_getitem_negative_index(
    parent_object, list_attribute, expected_initial_names, child_constructor
):
    linked_object_list = getattr(parent_object, list_attribute)

    assert linked_object_list[-1].name == expected_initial_names[-1]


@parametrize_with_cases(
    "parent_object, list_attribute, expected_initial_names, child_constructor",
    cases=".",
    glob="*existing",
)
def test_getitem_full_slice(
    parent_object, list_attribute, expected_initial_names, child_constructor
):
    linked_object_list = getattr(parent_object, list_attribute)

    assert [obj.name for obj in linked_object_list[:]] == list(expected_initial_names)


@parametrize_with_cases(
    "parent_object, list_attribute, expected_initial_names, child_constructor",
    cases=".",
    glob="*existing",
)
def test_setitem_zero(parent_object, list_attribute, expected_initial_names, child_constructor):
    linked_object_list = getattr(parent_object, list_attribute)

    new_obj = child_constructor(name="New Object")
    linked_object_list[0] = new_obj

    assert getattr(parent_object, list_attribute)[0].name == "New Object"


@parametrize_with_cases(
    "parent_object, list_attribute, expected_initial_names, child_constructor",
    cases=".",
    glob="*existing",
)
def test_delitem_slice(parent_object, list_attribute, expected_initial_names, child_constructor):
    linked_object_list = getattr(parent_object, list_attribute)

    assert len(getattr(parent_object, list_attribute)) != 0
    del linked_object_list[:]

    assert len(getattr(parent_object, list_attribute)) == 0


@parametrize_with_cases(
    "parent_object, list_attribute, expected_initial_names, child_constructor", cases="."
)
def test_append(parent_object, list_attribute, expected_initial_names, child_constructor):
    linked_object_list = getattr(parent_object, list_attribute)
    expected_names = list(expected_initial_names)
    for _ in range(10):
        new_child = child_constructor()
        linked_object_list.append(new_child)
        expected_names.append(new_child.name)

    # reload the 'linked_object_list' from the parent, to ensure the values are
    # propagated through
    linked_object_list = getattr(parent_object, list_attribute)
    assert [obj.name for obj in linked_object_list] == expected_names


@parametrize_with_cases(
    "parent_object, list_attribute, expected_initial_names, child_constructor", cases="."
)
def test_extend(parent_object, list_attribute, expected_initial_names, child_constructor):
    linked_object_list = getattr(parent_object, list_attribute)
    expected_names = list(expected_initial_names)
    new_objects = []
    for _ in range(10):
        new_child = child_constructor()
        expected_names.append(new_child.name)
        new_objects.append(new_child)

    linked_object_list.extend(new_objects)

    # reload the 'linked_object_list' from the parent, to ensure the values are
    # propagated through
    linked_object_list = getattr(parent_object, list_attribute)
    assert [obj.name for obj in linked_object_list] == expected_names


@parametrize_with_cases(
    "parent_object, list_attribute, expected_initial_names, child_constructor",
    cases=".",
    glob="*empty",
)
def test_append_unstored(parent_object, list_attribute, expected_initial_names, child_constructor):
    linked_object_list = getattr(parent_object, list_attribute)
    child_unstored = child_constructor().clone()
    with pytest.raises(RuntimeError):
        linked_object_list.append(child_unstored)


@parametrize_with_cases(
    "parent_object, list_attribute, expected_initial_names, child_constructor",
    cases=".",
    glob="*empty",
)
def test_sort_by_name(parent_object, list_attribute, expected_initial_names, child_constructor):
    names_unsorted = ["A", "Z", "C", "F", "B"]

    child_objects = [child_constructor(name=name) for name in names_unsorted]
    setattr(parent_object, list_attribute, child_objects)

    assert [obj.name for obj in getattr(parent_object, list_attribute)] == names_unsorted

    getattr(parent_object, list_attribute).sort()
    assert [obj.name for obj in getattr(parent_object, list_attribute)] == sorted(names_unsorted)

    getattr(parent_object, list_attribute).sort(reverse=True)
    assert [obj.name for obj in getattr(parent_object, list_attribute)] == sorted(
        names_unsorted, reverse=True
    )


@parametrize_with_cases(
    "parent_object, list_attribute, expected_initial_names, child_constructor",
    cases=".",
    glob="*empty",
)
def test_reverse(parent_object, list_attribute, expected_initial_names, child_constructor):
    names_initial = ["A", "Z", "C", "F", "B"]

    child_objects = [child_constructor(name=name) for name in names_initial]
    setattr(parent_object, list_attribute, child_objects)

    assert [obj.name for obj in getattr(parent_object, list_attribute)] == names_initial

    getattr(parent_object, list_attribute).reverse()
    assert [obj.name for obj in getattr(parent_object, list_attribute)] == list(
        reversed(names_initial)
    )


@parametrize_with_cases(
    "parent_object, list_attribute, expected_initial_names, child_constructor",
    cases=".",
    glob="*empty",
)
def test_reversed_iter(parent_object, list_attribute, expected_initial_names, child_constructor):
    names_initial = ["A", "Z", "C", "F", "B"]

    child_objects = [child_constructor(name=name) for name in names_initial]
    setattr(parent_object, list_attribute, child_objects)

    total_count = 0
    for expected_name, obj in zip(
        reversed(names_initial), reversed(getattr(parent_object, list_attribute))
    ):
        assert obj.name == expected_name
        total_count += 1
    assert total_count == len(names_initial)


@parametrize_with_cases(
    "parent_object, list_attribute, expected_initial_names, child_constructor",
    cases=".",
    glob="*empty",
)
def test_contains(parent_object, list_attribute, expected_initial_names, child_constructor):
    objects_linked = []
    for _ in range(3):
        objects_linked.append(child_constructor())
    setattr(parent_object, list_attribute, objects_linked)

    objects_not_linked = []
    for _ in range(3):
        objects_not_linked.append(child_constructor())

    assert all(obj in getattr(parent_object, list_attribute) for obj in objects_linked)
    assert all(obj not in getattr(parent_object, list_attribute) for obj in objects_not_linked)


@parametrize_with_cases(
    "parent_object, list_attribute, expected_initial_names, child_constructor",
    cases=".",
    glob="*empty",
)
def test_count(parent_object, list_attribute, expected_initial_names, child_constructor):
    objects_linked = []
    for _ in range(3):
        objects_linked.append(child_constructor())
    setattr(parent_object, list_attribute, objects_linked)

    objects_not_linked = []
    for _ in range(3):
        objects_not_linked.append(child_constructor())

    assert all(getattr(parent_object, list_attribute).count(obj) == 1 for obj in objects_linked)
    assert all(getattr(parent_object, list_attribute).count(obj) == 0 for obj in objects_not_linked)


@parametrize_with_cases(
    "parent_object, list_attribute, expected_initial_names, child_constructor",
    cases=".",
    glob="*empty",
)
def test_index(parent_object, list_attribute, expected_initial_names, child_constructor):
    objects_linked = []
    for _ in range(3):
        objects_linked.append(child_constructor())
    setattr(parent_object, list_attribute, objects_linked)

    objects_not_linked = []
    for _ in range(3):
        objects_not_linked.append(child_constructor())

    for i, obj in enumerate(objects_linked):
        assert getattr(parent_object, list_attribute).index(obj) == i

    for obj in objects_not_linked:
        with pytest.raises(ValueError):
            getattr(parent_object, list_attribute).index(obj)


@parametrize_with_cases(
    "parent_object, list_attribute, expected_initial_names, child_constructor",
    cases=".",
    glob="*empty",
)
def test_insert(parent_object, list_attribute, expected_initial_names, child_constructor):
    names_initial = ["A", "B", "C", "D"]

    child_objects = [child_constructor(name=name) for name in names_initial]

    assert [obj.name for obj in getattr(parent_object, list_attribute)] == []

    getattr(parent_object, list_attribute).insert(0, child_objects[0])
    assert [obj.name for obj in getattr(parent_object, list_attribute)] == ["A"]

    getattr(parent_object, list_attribute).insert(0, child_objects[1])
    assert [obj.name for obj in getattr(parent_object, list_attribute)] == ["B", "A"]

    getattr(parent_object, list_attribute).insert(-1, child_objects[2])
    assert [obj.name for obj in getattr(parent_object, list_attribute)] == ["B", "C", "A"]

    getattr(parent_object, list_attribute).insert(1, child_objects[3])
    assert [obj.name for obj in getattr(parent_object, list_attribute)] == ["B", "D", "C", "A"]


@parametrize_with_cases(
    "parent_object, list_attribute, expected_initial_names, child_constructor",
    cases=".",
    glob="*empty",
)
def test_remove(parent_object, list_attribute, expected_initial_names, child_constructor):
    names_initial = ["A", "Z", "C", "F", "B"]

    child_objects = [child_constructor(name=name) for name in names_initial]
    setattr(parent_object, list_attribute, child_objects)

    getattr(parent_object, list_attribute).remove(child_objects[2])
    assert [obj.name for obj in getattr(parent_object, list_attribute)] == ["A", "Z", "F", "B"]


@parametrize_with_cases(
    "parent_object, list_attribute, expected_initial_names, child_constructor",
    cases=".",
    glob="*empty",
)
def test_pop(parent_object, list_attribute, expected_initial_names, child_constructor):
    names_initial = ["A", "Z", "C", "F", "B"]

    child_objects = [child_constructor(name=name) for name in names_initial]
    setattr(parent_object, list_attribute, child_objects)

    last_obj = getattr(parent_object, list_attribute).pop()
    assert [obj.name for obj in getattr(parent_object, list_attribute)] == ["A", "Z", "C", "F"]
    assert last_obj.name == "B"

    removed_obj = getattr(parent_object, list_attribute).pop(1)
    assert [obj.name for obj in getattr(parent_object, list_attribute)] == ["A", "C", "F"]
    assert removed_obj.name == "Z"

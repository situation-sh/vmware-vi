# UncommittedUndoableDisk

Fault thrown when an attempt is made to move or clone an undoable disk with an uncommitted REDO log.  This is an error. Undoable disks may be moved but they must be committed. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.uncommitted_undoable_disk import UncommittedUndoableDisk

# TODO update the JSON string below
json = "{}"
# create an instance of UncommittedUndoableDisk from a JSON string
uncommitted_undoable_disk_instance = UncommittedUndoableDisk.from_json(json)
# print the JSON string representation of the object
print UncommittedUndoableDisk.to_json()

# convert the object into a dict
uncommitted_undoable_disk_dict = uncommitted_undoable_disk_instance.to_dict()
# create an instance of UncommittedUndoableDisk from a dict
uncommitted_undoable_disk_form_dict = uncommitted_undoable_disk.from_dict(uncommitted_undoable_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



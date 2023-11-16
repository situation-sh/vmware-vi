# MemorySnapshotOnIndependentDisk

Thrown if a request to take a memory snapshot is issued on a virtual machine with an independent disk. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.memory_snapshot_on_independent_disk import MemorySnapshotOnIndependentDisk

# TODO update the JSON string below
json = "{}"
# create an instance of MemorySnapshotOnIndependentDisk from a JSON string
memory_snapshot_on_independent_disk_instance = MemorySnapshotOnIndependentDisk.from_json(json)
# print the JSON string representation of the object
print MemorySnapshotOnIndependentDisk.to_json()

# convert the object into a dict
memory_snapshot_on_independent_disk_dict = memory_snapshot_on_independent_disk_instance.to_dict()
# create an instance of MemorySnapshotOnIndependentDisk from a dict
memory_snapshot_on_independent_disk_form_dict = memory_snapshot_on_independent_disk.from_dict(memory_snapshot_on_independent_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



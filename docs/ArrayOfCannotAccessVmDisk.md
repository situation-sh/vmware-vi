# ArrayOfCannotAccessVmDisk

A boxed array of *CannotAccessVmDisk*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CannotAccessVmDisk]**](CannotAccessVmDisk.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cannot_access_vm_disk import ArrayOfCannotAccessVmDisk

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCannotAccessVmDisk from a JSON string
array_of_cannot_access_vm_disk_instance = ArrayOfCannotAccessVmDisk.from_json(json)
# print the JSON string representation of the object
print ArrayOfCannotAccessVmDisk.to_json()

# convert the object into a dict
array_of_cannot_access_vm_disk_dict = array_of_cannot_access_vm_disk_instance.to_dict()
# create an instance of ArrayOfCannotAccessVmDisk from a dict
array_of_cannot_access_vm_disk_form_dict = array_of_cannot_access_vm_disk.from_dict(array_of_cannot_access_vm_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



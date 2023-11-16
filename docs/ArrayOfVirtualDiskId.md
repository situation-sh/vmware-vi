# ArrayOfVirtualDiskId

A boxed array of *VirtualDiskId*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualDiskId]**](VirtualDiskId.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_disk_id import ArrayOfVirtualDiskId

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualDiskId from a JSON string
array_of_virtual_disk_id_instance = ArrayOfVirtualDiskId.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualDiskId.to_json()

# convert the object into a dict
array_of_virtual_disk_id_dict = array_of_virtual_disk_id_instance.to_dict()
# create an instance of ArrayOfVirtualDiskId from a dict
array_of_virtual_disk_id_form_dict = array_of_virtual_disk_id.from_dict(array_of_virtual_disk_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



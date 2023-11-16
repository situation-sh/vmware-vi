# ArrayOfGuestInfoVirtualDiskMapping

A boxed array of *GuestInfoVirtualDiskMapping*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestInfoVirtualDiskMapping]**](GuestInfoVirtualDiskMapping.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_info_virtual_disk_mapping import ArrayOfGuestInfoVirtualDiskMapping

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestInfoVirtualDiskMapping from a JSON string
array_of_guest_info_virtual_disk_mapping_instance = ArrayOfGuestInfoVirtualDiskMapping.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestInfoVirtualDiskMapping.to_json()

# convert the object into a dict
array_of_guest_info_virtual_disk_mapping_dict = array_of_guest_info_virtual_disk_mapping_instance.to_dict()
# create an instance of ArrayOfGuestInfoVirtualDiskMapping from a dict
array_of_guest_info_virtual_disk_mapping_form_dict = array_of_guest_info_virtual_disk_mapping.from_dict(array_of_guest_info_virtual_disk_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



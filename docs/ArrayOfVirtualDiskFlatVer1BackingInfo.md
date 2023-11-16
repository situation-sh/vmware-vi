# ArrayOfVirtualDiskFlatVer1BackingInfo

A boxed array of *VirtualDiskFlatVer1BackingInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualDiskFlatVer1BackingInfo]**](VirtualDiskFlatVer1BackingInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_disk_flat_ver1_backing_info import ArrayOfVirtualDiskFlatVer1BackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualDiskFlatVer1BackingInfo from a JSON string
array_of_virtual_disk_flat_ver1_backing_info_instance = ArrayOfVirtualDiskFlatVer1BackingInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualDiskFlatVer1BackingInfo.to_json()

# convert the object into a dict
array_of_virtual_disk_flat_ver1_backing_info_dict = array_of_virtual_disk_flat_ver1_backing_info_instance.to_dict()
# create an instance of ArrayOfVirtualDiskFlatVer1BackingInfo from a dict
array_of_virtual_disk_flat_ver1_backing_info_form_dict = array_of_virtual_disk_flat_ver1_backing_info.from_dict(array_of_virtual_disk_flat_ver1_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ArrayOfVirtualDiskSparseVer1BackingInfo

A boxed array of *VirtualDiskSparseVer1BackingInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualDiskSparseVer1BackingInfo]**](VirtualDiskSparseVer1BackingInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_disk_sparse_ver1_backing_info import ArrayOfVirtualDiskSparseVer1BackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualDiskSparseVer1BackingInfo from a JSON string
array_of_virtual_disk_sparse_ver1_backing_info_instance = ArrayOfVirtualDiskSparseVer1BackingInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualDiskSparseVer1BackingInfo.to_json()

# convert the object into a dict
array_of_virtual_disk_sparse_ver1_backing_info_dict = array_of_virtual_disk_sparse_ver1_backing_info_instance.to_dict()
# create an instance of ArrayOfVirtualDiskSparseVer1BackingInfo from a dict
array_of_virtual_disk_sparse_ver1_backing_info_form_dict = array_of_virtual_disk_sparse_ver1_backing_info.from_dict(array_of_virtual_disk_sparse_ver1_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



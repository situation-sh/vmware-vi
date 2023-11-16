# SeSparseVirtualDiskSpec

Specification used to create an Flex-SE based virtual disk  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grain_size_kb** | **int** | The grain size in kB for Flex-SE disk types.  Default value will be used if unset.  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.se_sparse_virtual_disk_spec import SeSparseVirtualDiskSpec

# TODO update the JSON string below
json = "{}"
# create an instance of SeSparseVirtualDiskSpec from a JSON string
se_sparse_virtual_disk_spec_instance = SeSparseVirtualDiskSpec.from_json(json)
# print the JSON string representation of the object
print SeSparseVirtualDiskSpec.to_json()

# convert the object into a dict
se_sparse_virtual_disk_spec_dict = se_sparse_virtual_disk_spec_instance.to_dict()
# create an instance of SeSparseVirtualDiskSpec from a dict
se_sparse_virtual_disk_spec_form_dict = se_sparse_virtual_disk_spec.from_dict(se_sparse_virtual_disk_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



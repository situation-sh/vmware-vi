# RegisterDiskRequestType

The parameters of *VcenterVStorageObjectManager.RegisterDisk*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | URL path to the virtual disk.  | 
**name** | **str** | The descriptive name of the disk object. If unset the name will be automatically determined from the path. @see vim.vslm.BaseConfigInfo#name  | [optional] 

## Example

```python
from vmware_vi.models.register_disk_request_type import RegisterDiskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterDiskRequestType from a JSON string
register_disk_request_type_instance = RegisterDiskRequestType.from_json(json)
# print the JSON string representation of the object
print RegisterDiskRequestType.to_json()

# convert the object into a dict
register_disk_request_type_dict = register_disk_request_type_instance.to_dict()
# create an instance of RegisterDiskRequestType from a dict
register_disk_request_type_form_dict = register_disk_request_type.from_dict(register_disk_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



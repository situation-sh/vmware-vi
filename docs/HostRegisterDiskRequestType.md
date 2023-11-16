# HostRegisterDiskRequestType

The parameters of *HostVStorageObjectManager.HostRegisterDisk*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | URL or datastore path to the virtual disk.  | 
**name** | **str** | The descriptive name of the disk object. If unset the name will be automatically determined from the path. @see vim.vslm.BaseConfigInfo#name  | [optional] 

## Example

```python
from vmware_vi.models.host_register_disk_request_type import HostRegisterDiskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HostRegisterDiskRequestType from a JSON string
host_register_disk_request_type_instance = HostRegisterDiskRequestType.from_json(json)
# print the JSON string representation of the object
print HostRegisterDiskRequestType.to_json()

# convert the object into a dict
host_register_disk_request_type_dict = host_register_disk_request_type_instance.to_dict()
# create an instance of HostRegisterDiskRequestType from a dict
host_register_disk_request_type_form_dict = host_register_disk_request_type.from_dict(host_register_disk_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



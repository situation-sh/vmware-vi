# HostCreateDiskRequestType

The parameters of *HostVStorageObjectManager.HostCreateDisk_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**VslmCreateSpec**](VslmCreateSpec.md) |  | 

## Example

```python
from vmware_vi.models.host_create_disk_request_type import HostCreateDiskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HostCreateDiskRequestType from a JSON string
host_create_disk_request_type_instance = HostCreateDiskRequestType.from_json(json)
# print the JSON string representation of the object
print HostCreateDiskRequestType.to_json()

# convert the object into a dict
host_create_disk_request_type_dict = host_create_disk_request_type_instance.to_dict()
# create an instance of HostCreateDiskRequestType from a dict
host_create_disk_request_type_form_dict = host_create_disk_request_type.from_dict(host_create_disk_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



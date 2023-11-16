# HostInflateDiskRequestType

The parameters of *HostVStorageObjectManager.HostInflateDisk_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.host_inflate_disk_request_type import HostInflateDiskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HostInflateDiskRequestType from a JSON string
host_inflate_disk_request_type_instance = HostInflateDiskRequestType.from_json(json)
# print the JSON string representation of the object
print HostInflateDiskRequestType.to_json()

# convert the object into a dict
host_inflate_disk_request_type_dict = host_inflate_disk_request_type_instance.to_dict()
# create an instance of HostInflateDiskRequestType from a dict
host_inflate_disk_request_type_form_dict = host_inflate_disk_request_type.from_dict(host_inflate_disk_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



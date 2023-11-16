# VirtualCdromRemoteAtapiBackingInfo

The VirtualCdrom.RemoteAtapiBackingInfo data class represents a remote ATAPI device backing for a virtual CD-ROM. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_cdrom_remote_atapi_backing_info import VirtualCdromRemoteAtapiBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualCdromRemoteAtapiBackingInfo from a JSON string
virtual_cdrom_remote_atapi_backing_info_instance = VirtualCdromRemoteAtapiBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualCdromRemoteAtapiBackingInfo.to_json()

# convert the object into a dict
virtual_cdrom_remote_atapi_backing_info_dict = virtual_cdrom_remote_atapi_backing_info_instance.to_dict()
# create an instance of VirtualCdromRemoteAtapiBackingInfo from a dict
virtual_cdrom_remote_atapi_backing_info_form_dict = virtual_cdrom_remote_atapi_backing_info.from_dict(virtual_cdrom_remote_atapi_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



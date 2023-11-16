# VirtualCdromRemotePassthroughBackingOption

The VirtualCdromOption.RemotePassthroughBackingOption data object type contains the options for a remote pass-through CD-ROM device backing.  Note that the server cannot present a list of valid remote backing devices because it is unable to scan remote hosts. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclusive** | [**BoolOption**](BoolOption.md) |  | 

## Example

```python
from vmware_vi.models.virtual_cdrom_remote_passthrough_backing_option import VirtualCdromRemotePassthroughBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualCdromRemotePassthroughBackingOption from a JSON string
virtual_cdrom_remote_passthrough_backing_option_instance = VirtualCdromRemotePassthroughBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualCdromRemotePassthroughBackingOption.to_json()

# convert the object into a dict
virtual_cdrom_remote_passthrough_backing_option_dict = virtual_cdrom_remote_passthrough_backing_option_instance.to_dict()
# create an instance of VirtualCdromRemotePassthroughBackingOption from a dict
virtual_cdrom_remote_passthrough_backing_option_form_dict = virtual_cdrom_remote_passthrough_backing_option.from_dict(virtual_cdrom_remote_passthrough_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



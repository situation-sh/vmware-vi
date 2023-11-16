# WakeOnLanNotSupported

The virtual machine and at least one of its virtual NICs are configured to use Wake-on-LAN, but the host does not support Wake-on-LAN for the virtual machine's selected guest OS.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.wake_on_lan_not_supported import WakeOnLanNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of WakeOnLanNotSupported from a JSON string
wake_on_lan_not_supported_instance = WakeOnLanNotSupported.from_json(json)
# print the JSON string representation of the object
print WakeOnLanNotSupported.to_json()

# convert the object into a dict
wake_on_lan_not_supported_dict = wake_on_lan_not_supported_instance.to_dict()
# create an instance of WakeOnLanNotSupported from a dict
wake_on_lan_not_supported_form_dict = wake_on_lan_not_supported.from_dict(wake_on_lan_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



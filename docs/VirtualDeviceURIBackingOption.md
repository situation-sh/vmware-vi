# VirtualDeviceURIBackingOption

The *VirtualDeviceURIBackingOption* data object type describes network communication options for virtual devices.  When establishing a connection with a remote system on the network, the virtual machine can act as a server or a client. When the virtual machine acts as a server, it accepts a connection. When the virtual machine acts as a client, it initiates the connection.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**directions** | [**ChoiceOption**](ChoiceOption.md) |  | 

## Example

```python
from vmware_vi.models.virtual_device_uri_backing_option import VirtualDeviceURIBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDeviceURIBackingOption from a JSON string
virtual_device_uri_backing_option_instance = VirtualDeviceURIBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualDeviceURIBackingOption.to_json()

# convert the object into a dict
virtual_device_uri_backing_option_dict = virtual_device_uri_backing_option_instance.to_dict()
# create an instance of VirtualDeviceURIBackingOption from a dict
virtual_device_uri_backing_option_form_dict = virtual_device_uri_backing_option.from_dict(virtual_device_uri_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



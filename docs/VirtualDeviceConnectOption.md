# VirtualDeviceConnectOption

The ConnectOption data object type contains information about options for connectable virtual devices. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_connected** | [**BoolOption**](BoolOption.md) |  | 
**allow_guest_control** | [**BoolOption**](BoolOption.md) |  | 

## Example

```python
from vmware_vi.models.virtual_device_connect_option import VirtualDeviceConnectOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDeviceConnectOption from a JSON string
virtual_device_connect_option_instance = VirtualDeviceConnectOption.from_json(json)
# print the JSON string representation of the object
print VirtualDeviceConnectOption.to_json()

# convert the object into a dict
virtual_device_connect_option_dict = virtual_device_connect_option_instance.to_dict()
# create an instance of VirtualDeviceConnectOption from a dict
virtual_device_connect_option_form_dict = virtual_device_connect_option.from_dict(virtual_device_connect_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



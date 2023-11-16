# ArrayOfVirtualDeviceConnectOption

A boxed array of *VirtualDeviceConnectOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualDeviceConnectOption]**](VirtualDeviceConnectOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_device_connect_option import ArrayOfVirtualDeviceConnectOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualDeviceConnectOption from a JSON string
array_of_virtual_device_connect_option_instance = ArrayOfVirtualDeviceConnectOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualDeviceConnectOption.to_json()

# convert the object into a dict
array_of_virtual_device_connect_option_dict = array_of_virtual_device_connect_option_instance.to_dict()
# create an instance of ArrayOfVirtualDeviceConnectOption from a dict
array_of_virtual_device_connect_option_form_dict = array_of_virtual_device_connect_option.from_dict(array_of_virtual_device_connect_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



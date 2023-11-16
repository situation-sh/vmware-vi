# ArrayOfDeviceControllerNotSupported

A boxed array of *DeviceControllerNotSupported*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DeviceControllerNotSupported]**](DeviceControllerNotSupported.md) |  | 

## Example

```python
from vmware_vi.models.array_of_device_controller_not_supported import ArrayOfDeviceControllerNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDeviceControllerNotSupported from a JSON string
array_of_device_controller_not_supported_instance = ArrayOfDeviceControllerNotSupported.from_json(json)
# print the JSON string representation of the object
print ArrayOfDeviceControllerNotSupported.to_json()

# convert the object into a dict
array_of_device_controller_not_supported_dict = array_of_device_controller_not_supported_instance.to_dict()
# create an instance of ArrayOfDeviceControllerNotSupported from a dict
array_of_device_controller_not_supported_form_dict = array_of_device_controller_not_supported.from_dict(array_of_device_controller_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



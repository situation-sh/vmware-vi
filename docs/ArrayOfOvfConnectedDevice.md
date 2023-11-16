# ArrayOfOvfConnectedDevice

A boxed array of *OvfConnectedDevice*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfConnectedDevice]**](OvfConnectedDevice.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_connected_device import ArrayOfOvfConnectedDevice

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfConnectedDevice from a JSON string
array_of_ovf_connected_device_instance = ArrayOfOvfConnectedDevice.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfConnectedDevice.to_json()

# convert the object into a dict
array_of_ovf_connected_device_dict = array_of_ovf_connected_device_instance.to_dict()
# create an instance of ArrayOfOvfConnectedDevice from a dict
array_of_ovf_connected_device_form_dict = array_of_ovf_connected_device.from_dict(array_of_ovf_connected_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



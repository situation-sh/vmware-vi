# ArrayOfOvfUnknownDevice

A boxed array of *OvfUnknownDevice*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfUnknownDevice]**](OvfUnknownDevice.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_unknown_device import ArrayOfOvfUnknownDevice

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfUnknownDevice from a JSON string
array_of_ovf_unknown_device_instance = ArrayOfOvfUnknownDevice.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfUnknownDevice.to_json()

# convert the object into a dict
array_of_ovf_unknown_device_dict = array_of_ovf_unknown_device_instance.to_dict()
# create an instance of ArrayOfOvfUnknownDevice from a dict
array_of_ovf_unknown_device_form_dict = array_of_ovf_unknown_device.from_dict(array_of_ovf_unknown_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



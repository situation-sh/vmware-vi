# ArrayOfVirtualDevice

A boxed array of *VirtualDevice*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualDevice]**](VirtualDevice.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_device import ArrayOfVirtualDevice

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualDevice from a JSON string
array_of_virtual_device_instance = ArrayOfVirtualDevice.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualDevice.to_json()

# convert the object into a dict
array_of_virtual_device_dict = array_of_virtual_device_instance.to_dict()
# create an instance of ArrayOfVirtualDevice from a dict
array_of_virtual_device_form_dict = array_of_virtual_device.from_dict(array_of_virtual_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



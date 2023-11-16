# ArrayOfHostDevice

A boxed array of *HostDevice*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostDevice]**](HostDevice.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_device import ArrayOfHostDevice

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostDevice from a JSON string
array_of_host_device_instance = ArrayOfHostDevice.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostDevice.to_json()

# convert the object into a dict
array_of_host_device_dict = array_of_host_device_instance.to_dict()
# create an instance of ArrayOfHostDevice from a dict
array_of_host_device_form_dict = array_of_host_device.from_dict(array_of_host_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



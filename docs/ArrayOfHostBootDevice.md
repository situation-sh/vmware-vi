# ArrayOfHostBootDevice

A boxed array of *HostBootDevice*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostBootDevice]**](HostBootDevice.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_boot_device import ArrayOfHostBootDevice

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostBootDevice from a JSON string
array_of_host_boot_device_instance = ArrayOfHostBootDevice.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostBootDevice.to_json()

# convert the object into a dict
array_of_host_boot_device_dict = array_of_host_boot_device_instance.to_dict()
# create an instance of ArrayOfHostBootDevice from a dict
array_of_host_boot_device_form_dict = array_of_host_boot_device.from_dict(array_of_host_boot_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



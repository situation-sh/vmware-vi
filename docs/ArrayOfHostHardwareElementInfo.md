# ArrayOfHostHardwareElementInfo

A boxed array of *HostHardwareElementInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostHardwareElementInfo]**](HostHardwareElementInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_hardware_element_info import ArrayOfHostHardwareElementInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostHardwareElementInfo from a JSON string
array_of_host_hardware_element_info_instance = ArrayOfHostHardwareElementInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostHardwareElementInfo.to_json()

# convert the object into a dict
array_of_host_hardware_element_info_dict = array_of_host_hardware_element_info_instance.to_dict()
# create an instance of ArrayOfHostHardwareElementInfo from a dict
array_of_host_hardware_element_info_form_dict = array_of_host_hardware_element_info.from_dict(array_of_host_hardware_element_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



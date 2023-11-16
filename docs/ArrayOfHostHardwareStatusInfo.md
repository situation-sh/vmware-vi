# ArrayOfHostHardwareStatusInfo

A boxed array of *HostHardwareStatusInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostHardwareStatusInfo]**](HostHardwareStatusInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_hardware_status_info import ArrayOfHostHardwareStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostHardwareStatusInfo from a JSON string
array_of_host_hardware_status_info_instance = ArrayOfHostHardwareStatusInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostHardwareStatusInfo.to_json()

# convert the object into a dict
array_of_host_hardware_status_info_dict = array_of_host_hardware_status_info_instance.to_dict()
# create an instance of ArrayOfHostHardwareStatusInfo from a dict
array_of_host_hardware_status_info_form_dict = array_of_host_hardware_status_info.from_dict(array_of_host_hardware_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



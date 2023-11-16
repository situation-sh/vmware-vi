# ArrayOfHostDiskConfigurationResult

A boxed array of *HostDiskConfigurationResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostDiskConfigurationResult]**](HostDiskConfigurationResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_disk_configuration_result import ArrayOfHostDiskConfigurationResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostDiskConfigurationResult from a JSON string
array_of_host_disk_configuration_result_instance = ArrayOfHostDiskConfigurationResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostDiskConfigurationResult.to_json()

# convert the object into a dict
array_of_host_disk_configuration_result_dict = array_of_host_disk_configuration_result_instance.to_dict()
# create an instance of ArrayOfHostDiskConfigurationResult from a dict
array_of_host_disk_configuration_result_form_dict = array_of_host_disk_configuration_result.from_dict(array_of_host_disk_configuration_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



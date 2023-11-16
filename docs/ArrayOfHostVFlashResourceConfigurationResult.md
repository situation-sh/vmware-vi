# ArrayOfHostVFlashResourceConfigurationResult

A boxed array of *HostVFlashResourceConfigurationResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostVFlashResourceConfigurationResult]**](HostVFlashResourceConfigurationResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_v_flash_resource_configuration_result import ArrayOfHostVFlashResourceConfigurationResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostVFlashResourceConfigurationResult from a JSON string
array_of_host_v_flash_resource_configuration_result_instance = ArrayOfHostVFlashResourceConfigurationResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostVFlashResourceConfigurationResult.to_json()

# convert the object into a dict
array_of_host_v_flash_resource_configuration_result_dict = array_of_host_v_flash_resource_configuration_result_instance.to_dict()
# create an instance of ArrayOfHostVFlashResourceConfigurationResult from a dict
array_of_host_v_flash_resource_configuration_result_form_dict = array_of_host_v_flash_resource_configuration_result.from_dict(array_of_host_v_flash_resource_configuration_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ArrayOfHostSystemSwapConfiguration

A boxed array of *HostSystemSwapConfiguration*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostSystemSwapConfiguration]**](HostSystemSwapConfiguration.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_system_swap_configuration import ArrayOfHostSystemSwapConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostSystemSwapConfiguration from a JSON string
array_of_host_system_swap_configuration_instance = ArrayOfHostSystemSwapConfiguration.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostSystemSwapConfiguration.to_json()

# convert the object into a dict
array_of_host_system_swap_configuration_dict = array_of_host_system_swap_configuration_instance.to_dict()
# create an instance of ArrayOfHostSystemSwapConfiguration from a dict
array_of_host_system_swap_configuration_form_dict = array_of_host_system_swap_configuration.from_dict(array_of_host_system_swap_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



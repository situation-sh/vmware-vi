# ArrayOfHostServiceConfig

A boxed array of *HostServiceConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostServiceConfig]**](HostServiceConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_service_config import ArrayOfHostServiceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostServiceConfig from a JSON string
array_of_host_service_config_instance = ArrayOfHostServiceConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostServiceConfig.to_json()

# convert the object into a dict
array_of_host_service_config_dict = array_of_host_service_config_instance.to_dict()
# create an instance of ArrayOfHostServiceConfig from a dict
array_of_host_service_config_form_dict = array_of_host_service_config.from_dict(array_of_host_service_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



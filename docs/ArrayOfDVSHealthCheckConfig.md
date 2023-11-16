# ArrayOfDVSHealthCheckConfig

A boxed array of *DVSHealthCheckConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DVSHealthCheckConfig]**](DVSHealthCheckConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_health_check_config import ArrayOfDVSHealthCheckConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDVSHealthCheckConfig from a JSON string
array_of_dvs_health_check_config_instance = ArrayOfDVSHealthCheckConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfDVSHealthCheckConfig.to_json()

# convert the object into a dict
array_of_dvs_health_check_config_dict = array_of_dvs_health_check_config_instance.to_dict()
# create an instance of ArrayOfDVSHealthCheckConfig from a dict
array_of_dvs_health_check_config_form_dict = array_of_dvs_health_check_config.from_dict(array_of_dvs_health_check_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



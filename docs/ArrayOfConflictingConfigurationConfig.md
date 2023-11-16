# ArrayOfConflictingConfigurationConfig

A boxed array of *ConflictingConfigurationConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ConflictingConfigurationConfig]**](ConflictingConfigurationConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_conflicting_configuration_config import ArrayOfConflictingConfigurationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfConflictingConfigurationConfig from a JSON string
array_of_conflicting_configuration_config_instance = ArrayOfConflictingConfigurationConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfConflictingConfigurationConfig.to_json()

# convert the object into a dict
array_of_conflicting_configuration_config_dict = array_of_conflicting_configuration_config_instance.to_dict()
# create an instance of ArrayOfConflictingConfigurationConfig from a dict
array_of_conflicting_configuration_config_form_dict = array_of_conflicting_configuration_config.from_dict(array_of_conflicting_configuration_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



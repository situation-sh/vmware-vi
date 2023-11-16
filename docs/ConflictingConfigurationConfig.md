# ConflictingConfigurationConfig

This class defines the configuration that is in conflict.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**property_path** | **str** | The property paths that are in conflict.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.conflicting_configuration_config import ConflictingConfigurationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ConflictingConfigurationConfig from a JSON string
conflicting_configuration_config_instance = ConflictingConfigurationConfig.from_json(json)
# print the JSON string representation of the object
print ConflictingConfigurationConfig.to_json()

# convert the object into a dict
conflicting_configuration_config_dict = conflicting_configuration_config_instance.to_dict()
# create an instance of ConflictingConfigurationConfig from a dict
conflicting_configuration_config_form_dict = conflicting_configuration_config.from_dict(conflicting_configuration_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



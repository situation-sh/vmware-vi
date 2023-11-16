# ConflictingConfiguration

Thrown if the configurations of the objects are in conflict.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_in_conflict** | [**List[ConflictingConfigurationConfig]**](ConflictingConfigurationConfig.md) | The configurations that are in conflict.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.conflicting_configuration import ConflictingConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ConflictingConfiguration from a JSON string
conflicting_configuration_instance = ConflictingConfiguration.from_json(json)
# print the JSON string representation of the object
print ConflictingConfiguration.to_json()

# convert the object into a dict
conflicting_configuration_dict = conflicting_configuration_instance.to_dict()
# create an instance of ConflictingConfiguration from a dict
conflicting_configuration_form_dict = conflicting_configuration.from_dict(conflicting_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



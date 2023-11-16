# ArrayOfConflictingConfiguration

A boxed array of *ConflictingConfiguration*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ConflictingConfiguration]**](ConflictingConfiguration.md) |  | 

## Example

```python
from vmware_vi.models.array_of_conflicting_configuration import ArrayOfConflictingConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfConflictingConfiguration from a JSON string
array_of_conflicting_configuration_instance = ArrayOfConflictingConfiguration.from_json(json)
# print the JSON string representation of the object
print ArrayOfConflictingConfiguration.to_json()

# convert the object into a dict
array_of_conflicting_configuration_dict = array_of_conflicting_configuration_instance.to_dict()
# create an instance of ArrayOfConflictingConfiguration from a dict
array_of_conflicting_configuration_form_dict = array_of_conflicting_configuration.from_dict(array_of_conflicting_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



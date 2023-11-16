# ArrayOfDpmBehavior

A boxed array of *DpmBehavior_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DpmBehaviorEnum]**](DpmBehaviorEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dpm_behavior import ArrayOfDpmBehavior

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDpmBehavior from a JSON string
array_of_dpm_behavior_instance = ArrayOfDpmBehavior.from_json(json)
# print the JSON string representation of the object
print ArrayOfDpmBehavior.to_json()

# convert the object into a dict
array_of_dpm_behavior_dict = array_of_dpm_behavior_instance.to_dict()
# create an instance of ArrayOfDpmBehavior from a dict
array_of_dpm_behavior_form_dict = array_of_dpm_behavior.from_dict(array_of_dpm_behavior_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



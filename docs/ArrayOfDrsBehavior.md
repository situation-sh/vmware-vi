# ArrayOfDrsBehavior

A boxed array of *DrsBehavior_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DrsBehaviorEnum]**](DrsBehaviorEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_drs_behavior import ArrayOfDrsBehavior

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDrsBehavior from a JSON string
array_of_drs_behavior_instance = ArrayOfDrsBehavior.from_json(json)
# print the JSON string representation of the object
print ArrayOfDrsBehavior.to_json()

# convert the object into a dict
array_of_drs_behavior_dict = array_of_drs_behavior_instance.to_dict()
# create an instance of ArrayOfDrsBehavior from a dict
array_of_drs_behavior_form_dict = array_of_drs_behavior.from_dict(array_of_drs_behavior_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



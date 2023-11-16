# ArrayOfBoolPolicy

A boxed array of *BoolPolicy*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[BoolPolicy]**](BoolPolicy.md) |  | 

## Example

```python
from vmware_vi.models.array_of_bool_policy import ArrayOfBoolPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfBoolPolicy from a JSON string
array_of_bool_policy_instance = ArrayOfBoolPolicy.from_json(json)
# print the JSON string representation of the object
print ArrayOfBoolPolicy.to_json()

# convert the object into a dict
array_of_bool_policy_dict = array_of_bool_policy_instance.to_dict()
# create an instance of ArrayOfBoolPolicy from a dict
array_of_bool_policy_form_dict = array_of_bool_policy.from_dict(array_of_bool_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



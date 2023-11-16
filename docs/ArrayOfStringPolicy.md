# ArrayOfStringPolicy

A boxed array of *StringPolicy*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[StringPolicy]**](StringPolicy.md) |  | 

## Example

```python
from vmware_vi.models.array_of_string_policy import ArrayOfStringPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfStringPolicy from a JSON string
array_of_string_policy_instance = ArrayOfStringPolicy.from_json(json)
# print the JSON string representation of the object
print ArrayOfStringPolicy.to_json()

# convert the object into a dict
array_of_string_policy_dict = array_of_string_policy_instance.to_dict()
# create an instance of ArrayOfStringPolicy from a dict
array_of_string_policy_form_dict = array_of_string_policy.from_dict(array_of_string_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ArrayOfLongPolicy

A boxed array of *LongPolicy*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LongPolicy]**](LongPolicy.md) |  | 

## Example

```python
from vmware_vi.models.array_of_long_policy import ArrayOfLongPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLongPolicy from a JSON string
array_of_long_policy_instance = ArrayOfLongPolicy.from_json(json)
# print the JSON string representation of the object
print ArrayOfLongPolicy.to_json()

# convert the object into a dict
array_of_long_policy_dict = array_of_long_policy_instance.to_dict()
# create an instance of ArrayOfLongPolicy from a dict
array_of_long_policy_form_dict = array_of_long_policy.from_dict(array_of_long_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



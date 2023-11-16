# ArrayOfInheritablePolicy

A boxed array of *InheritablePolicy*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InheritablePolicy]**](InheritablePolicy.md) |  | 

## Example

```python
from vmware_vi.models.array_of_inheritable_policy import ArrayOfInheritablePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInheritablePolicy from a JSON string
array_of_inheritable_policy_instance = ArrayOfInheritablePolicy.from_json(json)
# print the JSON string representation of the object
print ArrayOfInheritablePolicy.to_json()

# convert the object into a dict
array_of_inheritable_policy_dict = array_of_inheritable_policy_instance.to_dict()
# create an instance of ArrayOfInheritablePolicy from a dict
array_of_inheritable_policy_form_dict = array_of_inheritable_policy.from_dict(array_of_inheritable_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



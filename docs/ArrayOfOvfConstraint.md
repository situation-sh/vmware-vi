# ArrayOfOvfConstraint

A boxed array of *OvfConstraint*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfConstraint]**](OvfConstraint.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_constraint import ArrayOfOvfConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfConstraint from a JSON string
array_of_ovf_constraint_instance = ArrayOfOvfConstraint.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfConstraint.to_json()

# convert the object into a dict
array_of_ovf_constraint_dict = array_of_ovf_constraint_instance.to_dict()
# create an instance of ArrayOfOvfConstraint from a dict
array_of_ovf_constraint_form_dict = array_of_ovf_constraint.from_dict(array_of_ovf_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



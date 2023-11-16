# ArrayOfOvfHostResourceConstraint

A boxed array of *OvfHostResourceConstraint*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfHostResourceConstraint]**](OvfHostResourceConstraint.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_host_resource_constraint import ArrayOfOvfHostResourceConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfHostResourceConstraint from a JSON string
array_of_ovf_host_resource_constraint_instance = ArrayOfOvfHostResourceConstraint.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfHostResourceConstraint.to_json()

# convert the object into a dict
array_of_ovf_host_resource_constraint_dict = array_of_ovf_host_resource_constraint_instance.to_dict()
# create an instance of ArrayOfOvfHostResourceConstraint from a dict
array_of_ovf_host_resource_constraint_form_dict = array_of_ovf_host_resource_constraint.from_dict(array_of_ovf_host_resource_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ArrayOfSolutionUserRequired

A boxed array of *SolutionUserRequired*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SolutionUserRequired]**](SolutionUserRequired.md) |  | 

## Example

```python
from vmware_vi.models.array_of_solution_user_required import ArrayOfSolutionUserRequired

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSolutionUserRequired from a JSON string
array_of_solution_user_required_instance = ArrayOfSolutionUserRequired.from_json(json)
# print the JSON string representation of the object
print ArrayOfSolutionUserRequired.to_json()

# convert the object into a dict
array_of_solution_user_required_dict = array_of_solution_user_required_instance.to_dict()
# create an instance of ArrayOfSolutionUserRequired from a dict
array_of_solution_user_required_form_dict = array_of_solution_user_required.from_dict(array_of_solution_user_required_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



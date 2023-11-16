# SolutionUserRequired

Thrown when an operation is denied because the entity invoking it is not a Solution User.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.solution_user_required import SolutionUserRequired

# TODO update the JSON string below
json = "{}"
# create an instance of SolutionUserRequired from a JSON string
solution_user_required_instance = SolutionUserRequired.from_json(json)
# print the JSON string representation of the object
print SolutionUserRequired.to_json()

# convert the object into a dict
solution_user_required_dict = solution_user_required_instance.to_dict()
# create an instance of SolutionUserRequired from a dict
solution_user_required_form_dict = solution_user_required.from_dict(solution_user_required_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



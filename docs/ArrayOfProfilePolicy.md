# ArrayOfProfilePolicy

A boxed array of *ProfilePolicy*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ProfilePolicy]**](ProfilePolicy.md) |  | 

## Example

```python
from vmware_vi.models.array_of_profile_policy import ArrayOfProfilePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfProfilePolicy from a JSON string
array_of_profile_policy_instance = ArrayOfProfilePolicy.from_json(json)
# print the JSON string representation of the object
print ArrayOfProfilePolicy.to_json()

# convert the object into a dict
array_of_profile_policy_dict = array_of_profile_policy_instance.to_dict()
# create an instance of ArrayOfProfilePolicy from a dict
array_of_profile_policy_form_dict = array_of_profile_policy.from_dict(array_of_profile_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



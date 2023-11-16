# ArrayOfNetStackInstanceProfile

A boxed array of *NetStackInstanceProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NetStackInstanceProfile]**](NetStackInstanceProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_net_stack_instance_profile import ArrayOfNetStackInstanceProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNetStackInstanceProfile from a JSON string
array_of_net_stack_instance_profile_instance = ArrayOfNetStackInstanceProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfNetStackInstanceProfile.to_json()

# convert the object into a dict
array_of_net_stack_instance_profile_dict = array_of_net_stack_instance_profile_instance.to_dict()
# create an instance of ArrayOfNetStackInstanceProfile from a dict
array_of_net_stack_instance_profile_form_dict = array_of_net_stack_instance_profile.from_dict(array_of_net_stack_instance_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



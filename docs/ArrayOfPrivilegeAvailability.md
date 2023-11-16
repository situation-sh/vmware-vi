# ArrayOfPrivilegeAvailability

A boxed array of *PrivilegeAvailability*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PrivilegeAvailability]**](PrivilegeAvailability.md) |  | 

## Example

```python
from vmware_vi.models.array_of_privilege_availability import ArrayOfPrivilegeAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPrivilegeAvailability from a JSON string
array_of_privilege_availability_instance = ArrayOfPrivilegeAvailability.from_json(json)
# print the JSON string representation of the object
print ArrayOfPrivilegeAvailability.to_json()

# convert the object into a dict
array_of_privilege_availability_dict = array_of_privilege_availability_instance.to_dict()
# create an instance of ArrayOfPrivilegeAvailability from a dict
array_of_privilege_availability_form_dict = array_of_privilege_availability.from_dict(array_of_privilege_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



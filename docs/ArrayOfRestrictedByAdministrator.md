# ArrayOfRestrictedByAdministrator

A boxed array of *RestrictedByAdministrator*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[RestrictedByAdministrator]**](RestrictedByAdministrator.md) |  | 

## Example

```python
from vmware_vi.models.array_of_restricted_by_administrator import ArrayOfRestrictedByAdministrator

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfRestrictedByAdministrator from a JSON string
array_of_restricted_by_administrator_instance = ArrayOfRestrictedByAdministrator.from_json(json)
# print the JSON string representation of the object
print ArrayOfRestrictedByAdministrator.to_json()

# convert the object into a dict
array_of_restricted_by_administrator_dict = array_of_restricted_by_administrator_instance.to_dict()
# create an instance of ArrayOfRestrictedByAdministrator from a dict
array_of_restricted_by_administrator_form_dict = array_of_restricted_by_administrator.from_dict(array_of_restricted_by_administrator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ArrayOfEntityPrivilege

A boxed array of *EntityPrivilege*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[EntityPrivilege]**](EntityPrivilege.md) |  | 

## Example

```python
from vmware_vi.models.array_of_entity_privilege import ArrayOfEntityPrivilege

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfEntityPrivilege from a JSON string
array_of_entity_privilege_instance = ArrayOfEntityPrivilege.from_json(json)
# print the JSON string representation of the object
print ArrayOfEntityPrivilege.to_json()

# convert the object into a dict
array_of_entity_privilege_dict = array_of_entity_privilege_instance.to_dict()
# create an instance of ArrayOfEntityPrivilege from a dict
array_of_entity_privilege_form_dict = array_of_entity_privilege.from_dict(array_of_entity_privilege_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



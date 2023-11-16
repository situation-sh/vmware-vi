# EntityPrivilege

This class defines whether a set of privileges are granted for a managed entity.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**priv_availability** | [**List[PrivilegeAvailability]**](PrivilegeAvailability.md) | whether a set of privileges are granted for the managed entity.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.entity_privilege import EntityPrivilege

# TODO update the JSON string below
json = "{}"
# create an instance of EntityPrivilege from a JSON string
entity_privilege_instance = EntityPrivilege.from_json(json)
# print the JSON string representation of the object
print EntityPrivilege.to_json()

# convert the object into a dict
entity_privilege_dict = entity_privilege_instance.to_dict()
# create an instance of EntityPrivilege from a dict
entity_privilege_form_dict = entity_privilege.from_dict(entity_privilege_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



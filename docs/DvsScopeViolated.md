# DvsScopeViolated

Deprecated as of vSphere API 5.5.  Thrown if a entity trying to connect to a port or portgroup but it is not in the port or portgroup's scope.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The configured scope.  ***Since:*** vSphere API 4.0  Refers instances of *ManagedEntity*.  | 
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.dvs_scope_violated import DvsScopeViolated

# TODO update the JSON string below
json = "{}"
# create an instance of DvsScopeViolated from a JSON string
dvs_scope_violated_instance = DvsScopeViolated.from_json(json)
# print the JSON string representation of the object
print DvsScopeViolated.to_json()

# convert the object into a dict
dvs_scope_violated_dict = dvs_scope_violated_instance.to_dict()
# create an instance of DvsScopeViolated from a dict
dvs_scope_violated_form_dict = dvs_scope_violated.from_dict(dvs_scope_violated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



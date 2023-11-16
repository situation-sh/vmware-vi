# ManagedByInfo

The ManagedByInfo data object contains information about the extension responsible for the life-cycle of the entity.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension_key** | **str** | Key of the extension managing the entity.  ***Since:*** vSphere API 5.0  | 
**type** | **str** | Managed entity type, as defined by the extension managing the entity.  An extension can manage different types of entities - different kinds of virtual machines, vApps, etc. - and this property is used to find the corresponding *managedEntityInfo* entry from the extension.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.managed_by_info import ManagedByInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedByInfo from a JSON string
managed_by_info_instance = ManagedByInfo.from_json(json)
# print the JSON string representation of the object
print ManagedByInfo.to_json()

# convert the object into a dict
managed_by_info_dict = managed_by_info_instance.to_dict()
# create an instance of ManagedByInfo from a dict
managed_by_info_form_dict = managed_by_info.from_dict(managed_by_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# StorageRequirement

Describes the storage requirement to perform a consolidation operation.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**free_space_required_in_kb** | **int** | Space required.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.storage_requirement import StorageRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of StorageRequirement from a JSON string
storage_requirement_instance = StorageRequirement.from_json(json)
# print the JSON string representation of the object
print StorageRequirement.to_json()

# convert the object into a dict
storage_requirement_dict = storage_requirement_instance.to_dict()
# create an instance of StorageRequirement from a dict
storage_requirement_form_dict = storage_requirement.from_dict(storage_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DVSManagerPhysicalNicsList

This class is used to store valid PhysicalNics for a specific host 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**physical_nics** | [**List[PhysicalNic]**](PhysicalNic.md) |  | [optional] 

## Example

```python
from vmware_vi.models.dvs_manager_physical_nics_list import DVSManagerPhysicalNicsList

# TODO update the JSON string below
json = "{}"
# create an instance of DVSManagerPhysicalNicsList from a JSON string
dvs_manager_physical_nics_list_instance = DVSManagerPhysicalNicsList.from_json(json)
# print the JSON string representation of the object
print DVSManagerPhysicalNicsList.to_json()

# convert the object into a dict
dvs_manager_physical_nics_list_dict = dvs_manager_physical_nics_list_instance.to_dict()
# create an instance of DVSManagerPhysicalNicsList from a dict
dvs_manager_physical_nics_list_form_dict = dvs_manager_physical_nics_list.from_dict(dvs_manager_physical_nics_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# IscsiDependencyEntity

Defines a dependency entity.  Contains the affected Virtual NIC device name and iSCSI HBA name (if Virtual NIC is associated with the HBA). See *IscsiMigrationDependency*  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pnic_device** | **str** | The affected Physical NIC device  ***Since:*** vSphere API 5.0  | 
**vnic_device** | **str** | The affected Virtual NIC device  ***Since:*** vSphere API 5.0  | 
**vmhba_name** | **str** | The iSCSI HBA that the Virtual NIC is associated with, if any.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.iscsi_dependency_entity import IscsiDependencyEntity

# TODO update the JSON string below
json = "{}"
# create an instance of IscsiDependencyEntity from a JSON string
iscsi_dependency_entity_instance = IscsiDependencyEntity.from_json(json)
# print the JSON string representation of the object
print IscsiDependencyEntity.to_json()

# convert the object into a dict
iscsi_dependency_entity_dict = iscsi_dependency_entity_instance.to_dict()
# create an instance of IscsiDependencyEntity from a dict
iscsi_dependency_entity_form_dict = iscsi_dependency_entity.from_dict(iscsi_dependency_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



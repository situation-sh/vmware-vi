# DVSManagerImportEntityRequestType

The parameters of *DistributedVirtualSwitchManager.DVSManagerImportEntity_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_backup** | [**List[EntityBackupConfig]**](EntityBackupConfig.md) | Configuration of one or more entities to be imported. The entity backup configuration is returned by the *DistributedVirtualSwitchManager.DVSManagerExportEntity_Task* method.  ***Since:*** vSphere API 5.1  | 
**import_type** | **str** | Specifies whether to create a new configuration or restore a previous configuration. See *EntityImportType_enum* for valid values.  | 

## Example

```python
from vmware_vi.models.dvs_manager_import_entity_request_type import DVSManagerImportEntityRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DVSManagerImportEntityRequestType from a JSON string
dvs_manager_import_entity_request_type_instance = DVSManagerImportEntityRequestType.from_json(json)
# print the JSON string representation of the object
print DVSManagerImportEntityRequestType.to_json()

# convert the object into a dict
dvs_manager_import_entity_request_type_dict = dvs_manager_import_entity_request_type_instance.to_dict()
# create an instance of DVSManagerImportEntityRequestType from a dict
dvs_manager_import_entity_request_type_form_dict = dvs_manager_import_entity_request_type.from_dict(dvs_manager_import_entity_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



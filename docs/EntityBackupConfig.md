# EntityBackupConfig

The *EntityBackupConfig* data object contains *VmwareDistributedVirtualSwitch* or *DistributedVirtualPortgroup* backup configuration data produced by the *DistributedVirtualSwitchManager.DVSManagerExportEntity_Task* method.  It also contains properties that support *DistributedVirtualSwitchManager.DVSManagerImportEntity_Task* operations.  A *DistributedVirtualSwitchManager.DVSManagerExportEntity_Task* operation sets properties that identify the entity instance (*EntityBackupConfig.entityType*, *EntityBackupConfig.key*, and *EntityBackupConfig.name*) and inventory location (*EntityBackupConfig.container*). When you import a backup configuration, you can set the <code>key</code>, <code>name</code>, and <code>container</code> properties in accordance with the <code>importType</code> specified in the call to *DistributedVirtualSwitchManager.DVSManagerImportEntity_Task*. See *EntityImportType_enum*.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | Type of the exported entity (*DistributedVirtualSwitchManager.DVSManagerExportEntity_Task*).  See *EntityType_enum* for valid values.  ***Since:*** vSphere API 5.1  | 
**config_blob** | **bytearray** | Opaque blob that contains the configuration of the entity.  ***Since:*** vSphere API 5.1  | 
**key** | **str** | Unique identifier of the exported entity or the entity to be restored through an import operation. - If you are importing a virtual distributed switch and the import type is   *applyToEntitySpecified*,   set the &lt;code&gt;key&lt;/code&gt; to   *DistributedVirtualSwitch*.*DistributedVirtualSwitch.uuid*. - If you are importing a virtual distributed portgroup and the import type is   *applyToEntitySpecified*,   set the &lt;code&gt;key&lt;/code&gt; to   *DistributedVirtualPortgroup*.*DistributedVirtualPortgroup.key*.    The Server ignores the key value when the import operation creates a new entity.  ***Since:*** vSphere API 5.1  | [optional] 
**name** | **str** | Name of the exported entity or the entity to be restored with the backup configuration.  If you are importing an entity and the import type is *applyToEntitySpecified*, the Server will use this value to rename the existing entity.  ***Since:*** vSphere API 5.1  | [optional] 
**container** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**config_version** | **str** | Configuration version.  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.entity_backup_config import EntityBackupConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EntityBackupConfig from a JSON string
entity_backup_config_instance = EntityBackupConfig.from_json(json)
# print the JSON string representation of the object
print EntityBackupConfig.to_json()

# convert the object into a dict
entity_backup_config_dict = entity_backup_config_instance.to_dict()
# create an instance of EntityBackupConfig from a dict
entity_backup_config_form_dict = entity_backup_config.from_dict(entity_backup_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



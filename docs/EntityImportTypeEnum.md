# EntityImportTypeEnum

The *EntityImportType_enum* enum defines the import type for a *DistributedVirtualSwitchManager*.*DistributedVirtualSwitchManager.DVSManagerImportEntity_Task* operation.  Possible values: - `createEntityWithNewIdentifier`: Create the entity with new identifiers.      Specify the   *EntityBackupConfig*.*EntityBackupConfig.name* and   *EntityBackupConfig*.*EntityBackupConfig.container*   properties.      The Server ignores any value for the   *EntityBackupConfig*.*EntityBackupConfig.key*   property. - `createEntityWithOriginalIdentifier`: Recreate the entities with the original identifiers of the entity from which backup was created.      The Server throws an exception if an entity with the same identifier already exists.   This option will also add the host members to the *DistributedVirtualSwitch* and will   try to get the virtual machine networking back with the same *DistributedVirtualPortgroup*.   Specify a *Folder* as the   *EntityBackupConfig*.*EntityBackupConfig.container*   for *EntityBackupConfig*.*EntityBackupConfig.entityType*   \"distributedVirtualSwitch\".      The Server ignores any values for the   *EntityBackupConfig*.*EntityBackupConfig.key* and   *EntityBackupConfig*.*EntityBackupConfig.name*   properties. - `applyToEntitySpecified`: Apply the configuration specified in the   *EntityBackupConfig*.*EntityBackupConfig.configBlob*   property to the entity specified in the   *EntityBackupConfig*.*EntityBackupConfig.entityType* and   *EntityBackupConfig*.*EntityBackupConfig.key*   properties.      If you specify   *EntityBackupConfig*.*EntityBackupConfig.name*,   the Server uses the specified name to rename the entity.      The Server ignores any value for the   *EntityBackupConfig*.*EntityBackupConfig.container*   property.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



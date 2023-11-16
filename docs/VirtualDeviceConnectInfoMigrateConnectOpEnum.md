# VirtualDeviceConnectInfoMigrateConnectOpEnum

Contains information about connectable virtual devices when the virtual machine restores from a migration.  Possible values: - `connect`: Attempt to connect the virtual device when the virtual machine   restores from a migration.      This property has no effect if it   is set on a device that is already connected. - `disconnect`: Attempt to disconnect the virtual device when the virtual machine   restores from a migration.      This property has no effect if it   is set on a device that is already disconnected. - `unset`: Unset the property, which resets the device to its default state.      Under most circumstances, a device will return to the same   connection state before the migration was initiated.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



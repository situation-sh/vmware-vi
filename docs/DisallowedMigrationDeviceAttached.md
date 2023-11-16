# DisallowedMigrationDeviceAttached

The virtual machine is using a type of device that prevents migration. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fault** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.disallowed_migration_device_attached import DisallowedMigrationDeviceAttached

# TODO update the JSON string below
json = "{}"
# create an instance of DisallowedMigrationDeviceAttached from a JSON string
disallowed_migration_device_attached_instance = DisallowedMigrationDeviceAttached.from_json(json)
# print the JSON string representation of the object
print DisallowedMigrationDeviceAttached.to_json()

# convert the object into a dict
disallowed_migration_device_attached_dict = disallowed_migration_device_attached_instance.to_dict()
# create an instance of DisallowedMigrationDeviceAttached from a dict
disallowed_migration_device_attached_form_dict = disallowed_migration_device_attached.from_dict(disallowed_migration_device_attached_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



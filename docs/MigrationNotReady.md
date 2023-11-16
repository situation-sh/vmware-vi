# MigrationNotReady

The VM to be migrated is not ready for the migration operation.  This might because the VM is still in the progress of powering on or resuming from a suspended state.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 

## Example

```python
from vmware_vi.models.migration_not_ready import MigrationNotReady

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationNotReady from a JSON string
migration_not_ready_instance = MigrationNotReady.from_json(json)
# print the JSON string representation of the object
print MigrationNotReady.to_json()

# convert the object into a dict
migration_not_ready_dict = migration_not_ready_instance.to_dict()
# create an instance of MigrationNotReady from a dict
migration_not_ready_form_dict = migration_not_ready.from_dict(migration_not_ready_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



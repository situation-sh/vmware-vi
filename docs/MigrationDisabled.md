# MigrationDisabled

An MigrationDisabled fault is thrown if the migration failed due to disabled migration  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.migration_disabled import MigrationDisabled

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationDisabled from a JSON string
migration_disabled_instance = MigrationDisabled.from_json(json)
# print the JSON string representation of the object
print MigrationDisabled.to_json()

# convert the object into a dict
migration_disabled_dict = migration_disabled_instance.to_dict()
# create an instance of MigrationDisabled from a dict
migration_disabled_form_dict = migration_disabled.from_dict(migration_disabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MigrationFeatureNotSupported

A migration operation that requires feature support on source and destination hosts is lacking support on the host.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at_source_host** | **bool** | Whether this error is for the source host.  ***Since:*** VI API 2.5  | 
**failed_host_name** | **str** | The name of the host.  ***Since:*** VI API 2.5  | 
**failed_host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.migration_feature_not_supported import MigrationFeatureNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationFeatureNotSupported from a JSON string
migration_feature_not_supported_instance = MigrationFeatureNotSupported.from_json(json)
# print the JSON string representation of the object
print MigrationFeatureNotSupported.to_json()

# convert the object into a dict
migration_feature_not_supported_dict = migration_feature_not_supported_instance.to_dict()
# create an instance of MigrationFeatureNotSupported from a dict
migration_feature_not_supported_form_dict = migration_feature_not_supported.from_dict(migration_feature_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



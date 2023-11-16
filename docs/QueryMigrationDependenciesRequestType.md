# QueryMigrationDependenciesRequestType

The parameters of *IscsiManager.QueryMigrationDependencies*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pnic_device** | **List[str]** | List of Physical NICs to be migrated  | 

## Example

```python
from vmware_vi.models.query_migration_dependencies_request_type import QueryMigrationDependenciesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryMigrationDependenciesRequestType from a JSON string
query_migration_dependencies_request_type_instance = QueryMigrationDependenciesRequestType.from_json(json)
# print the JSON string representation of the object
print QueryMigrationDependenciesRequestType.to_json()

# convert the object into a dict
query_migration_dependencies_request_type_dict = query_migration_dependencies_request_type_instance.to_dict()
# create an instance of QueryMigrationDependenciesRequestType from a dict
query_migration_dependencies_request_type_form_dict = query_migration_dependencies_request_type.from_dict(query_migration_dependencies_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



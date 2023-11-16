# ValidateMigrationRequestType

The parameters of *ServiceInstance.ValidateMigration*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The set of virtual machines intended for migration.  Refers instances of *VirtualMachine*.  | 
**state** | [**VirtualMachinePowerStateEnum**](VirtualMachinePowerStateEnum.md) |  | [optional] 
**test_type** | **List[str]** | The set of tests to run. If this argument is not set, all tests will be run.  | [optional] 
**pool** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.validate_migration_request_type import ValidateMigrationRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateMigrationRequestType from a JSON string
validate_migration_request_type_instance = ValidateMigrationRequestType.from_json(json)
# print the JSON string representation of the object
print ValidateMigrationRequestType.to_json()

# convert the object into a dict
validate_migration_request_type_dict = validate_migration_request_type_instance.to_dict()
# create an instance of ValidateMigrationRequestType from a dict
validate_migration_request_type_form_dict = validate_migration_request_type.from_dict(validate_migration_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



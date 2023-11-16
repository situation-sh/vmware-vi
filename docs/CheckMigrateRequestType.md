# CheckMigrateRequestType

The parameters of *VirtualMachineProvisioningChecker.CheckMigrate_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**pool** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**state** | [**VirtualMachinePowerStateEnum**](VirtualMachinePowerStateEnum.md) |  | [optional] 
**test_type** | **List[str]** | The set of tests to run. If this argument is not set, all tests will be run. See *CheckTestType_enum* for possible values.  | [optional] 

## Example

```python
from vmware_vi.models.check_migrate_request_type import CheckMigrateRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CheckMigrateRequestType from a JSON string
check_migrate_request_type_instance = CheckMigrateRequestType.from_json(json)
# print the JSON string representation of the object
print CheckMigrateRequestType.to_json()

# convert the object into a dict
check_migrate_request_type_dict = check_migrate_request_type_instance.to_dict()
# create an instance of CheckMigrateRequestType from a dict
check_migrate_request_type_form_dict = check_migrate_request_type.from_dict(check_migrate_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



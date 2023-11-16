# CheckCloneRequestType

The parameters of *VirtualMachineProvisioningChecker.CheckClone_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**folder** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**name** | **str** | The name of the new virtual machine.  | 
**spec** | [**VirtualMachineCloneSpec**](VirtualMachineCloneSpec.md) |  | 
**test_type** | **List[str]** | The set of tests to run. If this argument is not set, all tests will be run. See *CheckTestType_enum* for possible values.  | [optional] 

## Example

```python
from vmware_vi.models.check_clone_request_type import CheckCloneRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CheckCloneRequestType from a JSON string
check_clone_request_type_instance = CheckCloneRequestType.from_json(json)
# print the JSON string representation of the object
print CheckCloneRequestType.to_json()

# convert the object into a dict
check_clone_request_type_dict = check_clone_request_type_instance.to_dict()
# create an instance of CheckCloneRequestType from a dict
check_clone_request_type_form_dict = check_clone_request_type.from_dict(check_clone_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



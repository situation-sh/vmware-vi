# CheckRelocateRequestType

The parameters of *VirtualMachineProvisioningChecker.CheckRelocate_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**spec** | [**VirtualMachineRelocateSpec**](VirtualMachineRelocateSpec.md) |  | 
**test_type** | **List[str]** | The set of tests to run. If this argument is not set, all tests will be run. See *CheckTestType_enum* for possible values.  | [optional] 

## Example

```python
from vmware_vi.models.check_relocate_request_type import CheckRelocateRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CheckRelocateRequestType from a JSON string
check_relocate_request_type_instance = CheckRelocateRequestType.from_json(json)
# print the JSON string representation of the object
print CheckRelocateRequestType.to_json()

# convert the object into a dict
check_relocate_request_type_dict = check_relocate_request_type_instance.to_dict()
# create an instance of CheckRelocateRequestType from a dict
check_relocate_request_type_form_dict = check_relocate_request_type.from_dict(check_relocate_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



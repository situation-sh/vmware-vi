# CheckCompatibilityRequestType

The parameters of *VirtualMachineCompatibilityChecker.CheckCompatibility_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**pool** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**test_type** | **List[str]** | The set of tests to run. If this argument is not set, all tests will be run. See *CheckTestType_enum* for possible values.  | [optional] 

## Example

```python
from vmware_vi.models.check_compatibility_request_type import CheckCompatibilityRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CheckCompatibilityRequestType from a JSON string
check_compatibility_request_type_instance = CheckCompatibilityRequestType.from_json(json)
# print the JSON string representation of the object
print CheckCompatibilityRequestType.to_json()

# convert the object into a dict
check_compatibility_request_type_dict = check_compatibility_request_type_instance.to_dict()
# create an instance of CheckCompatibilityRequestType from a dict
check_compatibility_request_type_form_dict = check_compatibility_request_type.from_dict(check_compatibility_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



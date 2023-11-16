# CheckPowerOnRequestType

The parameters of *VirtualMachineCompatibilityChecker.CheckPowerOn_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**pool** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**test_type** | **List[str]** | The set of tests to run. If this argument is not set, all tests will be run. See *CheckTestType_enum* for possible values.  | [optional] 

## Example

```python
from vmware_vi.models.check_power_on_request_type import CheckPowerOnRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CheckPowerOnRequestType from a JSON string
check_power_on_request_type_instance = CheckPowerOnRequestType.from_json(json)
# print the JSON string representation of the object
print CheckPowerOnRequestType.to_json()

# convert the object into a dict
check_power_on_request_type_dict = check_power_on_request_type_instance.to_dict()
# create an instance of CheckPowerOnRequestType from a dict
check_power_on_request_type_form_dict = check_power_on_request_type.from_dict(check_power_on_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



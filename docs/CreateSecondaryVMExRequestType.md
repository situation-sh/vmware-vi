# CreateSecondaryVMExRequestType

The parameters of *VirtualMachine.CreateSecondaryVMEx_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**spec** | [**FaultToleranceConfigSpec**](FaultToleranceConfigSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.create_secondary_vmex_request_type import CreateSecondaryVMExRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSecondaryVMExRequestType from a JSON string
create_secondary_vmex_request_type_instance = CreateSecondaryVMExRequestType.from_json(json)
# print the JSON string representation of the object
print CreateSecondaryVMExRequestType.to_json()

# convert the object into a dict
create_secondary_vmex_request_type_dict = create_secondary_vmex_request_type_instance.to_dict()
# create an instance of CreateSecondaryVMExRequestType from a dict
create_secondary_vmex_request_type_form_dict = create_secondary_vmex_request_type.from_dict(create_secondary_vmex_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



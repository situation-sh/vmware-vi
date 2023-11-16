# InstantCloneRequestType

The parameters of *VirtualMachine.InstantClone_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**VirtualMachineInstantCloneSpec**](VirtualMachineInstantCloneSpec.md) |  | 

## Example

```python
from vmware_vi.models.instant_clone_request_type import InstantCloneRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of InstantCloneRequestType from a JSON string
instant_clone_request_type_instance = InstantCloneRequestType.from_json(json)
# print the JSON string representation of the object
print InstantCloneRequestType.to_json()

# convert the object into a dict
instant_clone_request_type_dict = instant_clone_request_type_instance.to_dict()
# create an instance of InstantCloneRequestType from a dict
instant_clone_request_type_form_dict = instant_clone_request_type.from_dict(instant_clone_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MethodFault

The base data object type for all the object model faults that an application might handle. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fault_cause** | [**MethodFault**](MethodFault.md) |  | [optional] 
**fault_message** | [**List[LocalizableMessage]**](LocalizableMessage.md) | Message which has details about the error Message can also contain a key to message catalog which can be used to generate better localized messages.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.method_fault import MethodFault

# TODO update the JSON string below
json = "{}"
# create an instance of MethodFault from a JSON string
method_fault_instance = MethodFault.from_json(json)
# print the JSON string representation of the object
print MethodFault.to_json()

# convert the object into a dict
method_fault_dict = method_fault_instance.to_dict()
# create an instance of MethodFault from a dict
method_fault_form_dict = method_fault.from_dict(method_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



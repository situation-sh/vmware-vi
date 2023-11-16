# LocalizedMethodFault

A wrapper class used to pass MethodFault data objects over the wire along with a localized display message for the fault. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fault** | [**MethodFault**](MethodFault.md) |  | 
**localized_message** | **str** | The localized message that would be sent in the faultstring element of the SOAP Fault.  It is optional so that clients are not required to send a localized message to the server, but servers are required to send the localized message to clients.  | [optional] 

## Example

```python
from vmware_vi.models.localized_method_fault import LocalizedMethodFault

# TODO update the JSON string below
json = "{}"
# create an instance of LocalizedMethodFault from a JSON string
localized_method_fault_instance = LocalizedMethodFault.from_json(json)
# print the JSON string representation of the object
print LocalizedMethodFault.to_json()

# convert the object into a dict
localized_method_fault_dict = localized_method_fault_instance.to_dict()
# create an instance of LocalizedMethodFault from a dict
localized_method_fault_form_dict = localized_method_fault.from_dict(localized_method_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



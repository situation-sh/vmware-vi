# UnexpectedFault

An UnexpectedFault may be thrown when a newer version of the server reports a error that a cannot be converted to a fault that a client that is using an older version of the API would expect. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fault_name** | **str** | Name of the unexpected fault.  | 
**fault** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.unexpected_fault import UnexpectedFault

# TODO update the JSON string below
json = "{}"
# create an instance of UnexpectedFault from a JSON string
unexpected_fault_instance = UnexpectedFault.from_json(json)
# print the JSON string representation of the object
print UnexpectedFault.to_json()

# convert the object into a dict
unexpected_fault_dict = unexpected_fault_instance.to_dict()
# create an instance of UnexpectedFault from a dict
unexpected_fault_form_dict = unexpected_fault.from_dict(unexpected_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



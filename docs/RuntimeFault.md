# RuntimeFault

The base data object type for all runtime faults that can be thrown by a method. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.runtime_fault import RuntimeFault

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeFault from a JSON string
runtime_fault_instance = RuntimeFault.from_json(json)
# print the JSON string representation of the object
print RuntimeFault.to_json()

# convert the object into a dict
runtime_fault_dict = runtime_fault_instance.to_dict()
# create an instance of RuntimeFault from a dict
runtime_fault_form_dict = runtime_fault.from_dict(runtime_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



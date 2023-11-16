# ArrayOfOperationDisallowedOnHost

A boxed array of *OperationDisallowedOnHost*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OperationDisallowedOnHost]**](OperationDisallowedOnHost.md) |  | 

## Example

```python
from vmware_vi.models.array_of_operation_disallowed_on_host import ArrayOfOperationDisallowedOnHost

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOperationDisallowedOnHost from a JSON string
array_of_operation_disallowed_on_host_instance = ArrayOfOperationDisallowedOnHost.from_json(json)
# print the JSON string representation of the object
print ArrayOfOperationDisallowedOnHost.to_json()

# convert the object into a dict
array_of_operation_disallowed_on_host_dict = array_of_operation_disallowed_on_host_instance.to_dict()
# create an instance of ArrayOfOperationDisallowedOnHost from a dict
array_of_operation_disallowed_on_host_form_dict = array_of_operation_disallowed_on_host.from_dict(array_of_operation_disallowed_on_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



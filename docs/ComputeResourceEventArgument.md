# ComputeResourceEventArgument

The event argument is a ComputeResource object. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compute_resource** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.compute_resource_event_argument import ComputeResourceEventArgument

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeResourceEventArgument from a JSON string
compute_resource_event_argument_instance = ComputeResourceEventArgument.from_json(json)
# print the JSON string representation of the object
print ComputeResourceEventArgument.to_json()

# convert the object into a dict
compute_resource_event_argument_dict = compute_resource_event_argument_instance.to_dict()
# create an instance of ComputeResourceEventArgument from a dict
compute_resource_event_argument_form_dict = compute_resource_event_argument.from_dict(compute_resource_event_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



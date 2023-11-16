# ArrayOfComputeResourceEventArgument

A boxed array of *ComputeResourceEventArgument*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ComputeResourceEventArgument]**](ComputeResourceEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.array_of_compute_resource_event_argument import ArrayOfComputeResourceEventArgument

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfComputeResourceEventArgument from a JSON string
array_of_compute_resource_event_argument_instance = ArrayOfComputeResourceEventArgument.from_json(json)
# print the JSON string representation of the object
print ArrayOfComputeResourceEventArgument.to_json()

# convert the object into a dict
array_of_compute_resource_event_argument_dict = array_of_compute_resource_event_argument_instance.to_dict()
# create an instance of ArrayOfComputeResourceEventArgument from a dict
array_of_compute_resource_event_argument_form_dict = array_of_compute_resource_event_argument.from_dict(array_of_compute_resource_event_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



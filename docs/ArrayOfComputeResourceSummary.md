# ArrayOfComputeResourceSummary

A boxed array of *ComputeResourceSummary*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ComputeResourceSummary]**](ComputeResourceSummary.md) |  | 

## Example

```python
from vmware_vi.models.array_of_compute_resource_summary import ArrayOfComputeResourceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfComputeResourceSummary from a JSON string
array_of_compute_resource_summary_instance = ArrayOfComputeResourceSummary.from_json(json)
# print the JSON string representation of the object
print ArrayOfComputeResourceSummary.to_json()

# convert the object into a dict
array_of_compute_resource_summary_dict = array_of_compute_resource_summary_instance.to_dict()
# create an instance of ArrayOfComputeResourceSummary from a dict
array_of_compute_resource_summary_form_dict = array_of_compute_resource_summary.from_dict(array_of_compute_resource_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



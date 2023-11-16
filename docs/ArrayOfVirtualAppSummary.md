# ArrayOfVirtualAppSummary

A boxed array of *VirtualAppSummary*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualAppSummary]**](VirtualAppSummary.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_app_summary import ArrayOfVirtualAppSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualAppSummary from a JSON string
array_of_virtual_app_summary_instance = ArrayOfVirtualAppSummary.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualAppSummary.to_json()

# convert the object into a dict
array_of_virtual_app_summary_dict = array_of_virtual_app_summary_instance.to_dict()
# create an instance of ArrayOfVirtualAppSummary from a dict
array_of_virtual_app_summary_form_dict = array_of_virtual_app_summary.from_dict(array_of_virtual_app_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



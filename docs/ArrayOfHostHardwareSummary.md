# ArrayOfHostHardwareSummary

A boxed array of *HostHardwareSummary*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostHardwareSummary]**](HostHardwareSummary.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_hardware_summary import ArrayOfHostHardwareSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostHardwareSummary from a JSON string
array_of_host_hardware_summary_instance = ArrayOfHostHardwareSummary.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostHardwareSummary.to_json()

# convert the object into a dict
array_of_host_hardware_summary_dict = array_of_host_hardware_summary_instance.to_dict()
# create an instance of ArrayOfHostHardwareSummary from a dict
array_of_host_hardware_summary_form_dict = array_of_host_hardware_summary.from_dict(array_of_host_hardware_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



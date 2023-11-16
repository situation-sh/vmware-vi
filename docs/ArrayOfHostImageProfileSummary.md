# ArrayOfHostImageProfileSummary

A boxed array of *HostImageProfileSummary*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostImageProfileSummary]**](HostImageProfileSummary.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_image_profile_summary import ArrayOfHostImageProfileSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostImageProfileSummary from a JSON string
array_of_host_image_profile_summary_instance = ArrayOfHostImageProfileSummary.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostImageProfileSummary.to_json()

# convert the object into a dict
array_of_host_image_profile_summary_dict = array_of_host_image_profile_summary_instance.to_dict()
# create an instance of ArrayOfHostImageProfileSummary from a dict
array_of_host_image_profile_summary_form_dict = array_of_host_image_profile_summary.from_dict(array_of_host_image_profile_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



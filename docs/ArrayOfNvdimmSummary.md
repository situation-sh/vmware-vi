# ArrayOfNvdimmSummary

A boxed array of *NvdimmSummary*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NvdimmSummary]**](NvdimmSummary.md) |  | 

## Example

```python
from vmware_vi.models.array_of_nvdimm_summary import ArrayOfNvdimmSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNvdimmSummary from a JSON string
array_of_nvdimm_summary_instance = ArrayOfNvdimmSummary.from_json(json)
# print the JSON string representation of the object
print ArrayOfNvdimmSummary.to_json()

# convert the object into a dict
array_of_nvdimm_summary_dict = array_of_nvdimm_summary_instance.to_dict()
# create an instance of ArrayOfNvdimmSummary from a dict
array_of_nvdimm_summary_form_dict = array_of_nvdimm_summary.from_dict(array_of_nvdimm_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



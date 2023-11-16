# ArrayOfNvdimmInterleaveSetInfo

A boxed array of *NvdimmInterleaveSetInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NvdimmInterleaveSetInfo]**](NvdimmInterleaveSetInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_nvdimm_interleave_set_info import ArrayOfNvdimmInterleaveSetInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNvdimmInterleaveSetInfo from a JSON string
array_of_nvdimm_interleave_set_info_instance = ArrayOfNvdimmInterleaveSetInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfNvdimmInterleaveSetInfo.to_json()

# convert the object into a dict
array_of_nvdimm_interleave_set_info_dict = array_of_nvdimm_interleave_set_info_instance.to_dict()
# create an instance of ArrayOfNvdimmInterleaveSetInfo from a dict
array_of_nvdimm_interleave_set_info_form_dict = array_of_nvdimm_interleave_set_info.from_dict(array_of_nvdimm_interleave_set_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



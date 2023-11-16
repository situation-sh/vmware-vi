# ArrayOfNvdimmDimmInfo

A boxed array of *NvdimmDimmInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NvdimmDimmInfo]**](NvdimmDimmInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_nvdimm_dimm_info import ArrayOfNvdimmDimmInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNvdimmDimmInfo from a JSON string
array_of_nvdimm_dimm_info_instance = ArrayOfNvdimmDimmInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfNvdimmDimmInfo.to_json()

# convert the object into a dict
array_of_nvdimm_dimm_info_dict = array_of_nvdimm_dimm_info_instance.to_dict()
# create an instance of ArrayOfNvdimmDimmInfo from a dict
array_of_nvdimm_dimm_info_form_dict = array_of_nvdimm_dimm_info.from_dict(array_of_nvdimm_dimm_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



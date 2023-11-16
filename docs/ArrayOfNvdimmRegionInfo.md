# ArrayOfNvdimmRegionInfo

A boxed array of *NvdimmRegionInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NvdimmRegionInfo]**](NvdimmRegionInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_nvdimm_region_info import ArrayOfNvdimmRegionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNvdimmRegionInfo from a JSON string
array_of_nvdimm_region_info_instance = ArrayOfNvdimmRegionInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfNvdimmRegionInfo.to_json()

# convert the object into a dict
array_of_nvdimm_region_info_dict = array_of_nvdimm_region_info_instance.to_dict()
# create an instance of ArrayOfNvdimmRegionInfo from a dict
array_of_nvdimm_region_info_form_dict = array_of_nvdimm_region_info.from_dict(array_of_nvdimm_region_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



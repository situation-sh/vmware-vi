# ArrayOfNvdimmHealthInfo

A boxed array of *NvdimmHealthInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NvdimmHealthInfo]**](NvdimmHealthInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_nvdimm_health_info import ArrayOfNvdimmHealthInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNvdimmHealthInfo from a JSON string
array_of_nvdimm_health_info_instance = ArrayOfNvdimmHealthInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfNvdimmHealthInfo.to_json()

# convert the object into a dict
array_of_nvdimm_health_info_dict = array_of_nvdimm_health_info_instance.to_dict()
# create an instance of ArrayOfNvdimmHealthInfo from a dict
array_of_nvdimm_health_info_form_dict = array_of_nvdimm_health_info.from_dict(array_of_nvdimm_health_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



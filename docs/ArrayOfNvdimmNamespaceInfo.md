# ArrayOfNvdimmNamespaceInfo

A boxed array of *NvdimmNamespaceInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NvdimmNamespaceInfo]**](NvdimmNamespaceInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_nvdimm_namespace_info import ArrayOfNvdimmNamespaceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNvdimmNamespaceInfo from a JSON string
array_of_nvdimm_namespace_info_instance = ArrayOfNvdimmNamespaceInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfNvdimmNamespaceInfo.to_json()

# convert the object into a dict
array_of_nvdimm_namespace_info_dict = array_of_nvdimm_namespace_info_instance.to_dict()
# create an instance of ArrayOfNvdimmNamespaceInfo from a dict
array_of_nvdimm_namespace_info_form_dict = array_of_nvdimm_namespace_info.from_dict(array_of_nvdimm_namespace_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



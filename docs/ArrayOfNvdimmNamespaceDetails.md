# ArrayOfNvdimmNamespaceDetails

A boxed array of *NvdimmNamespaceDetails*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NvdimmNamespaceDetails]**](NvdimmNamespaceDetails.md) |  | 

## Example

```python
from vmware_vi.models.array_of_nvdimm_namespace_details import ArrayOfNvdimmNamespaceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNvdimmNamespaceDetails from a JSON string
array_of_nvdimm_namespace_details_instance = ArrayOfNvdimmNamespaceDetails.from_json(json)
# print the JSON string representation of the object
print ArrayOfNvdimmNamespaceDetails.to_json()

# convert the object into a dict
array_of_nvdimm_namespace_details_dict = array_of_nvdimm_namespace_details_instance.to_dict()
# create an instance of ArrayOfNvdimmNamespaceDetails from a dict
array_of_nvdimm_namespace_details_form_dict = array_of_nvdimm_namespace_details.from_dict(array_of_nvdimm_namespace_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



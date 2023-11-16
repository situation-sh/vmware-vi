# ArrayOfNvdimmGuid

A boxed array of *NvdimmGuid*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NvdimmGuid]**](NvdimmGuid.md) |  | 

## Example

```python
from vmware_vi.models.array_of_nvdimm_guid import ArrayOfNvdimmGuid

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNvdimmGuid from a JSON string
array_of_nvdimm_guid_instance = ArrayOfNvdimmGuid.from_json(json)
# print the JSON string representation of the object
print ArrayOfNvdimmGuid.to_json()

# convert the object into a dict
array_of_nvdimm_guid_dict = array_of_nvdimm_guid_instance.to_dict()
# create an instance of ArrayOfNvdimmGuid from a dict
array_of_nvdimm_guid_form_dict = array_of_nvdimm_guid.from_dict(array_of_nvdimm_guid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



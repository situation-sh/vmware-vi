# NvdimmGuid

A unique identifier used for namespaces  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Universally unique identifier in string format  ***Since:*** vSphere API 6.7  | 

## Example

```python
from vmware_vi.models.nvdimm_guid import NvdimmGuid

# TODO update the JSON string below
json = "{}"
# create an instance of NvdimmGuid from a JSON string
nvdimm_guid_instance = NvdimmGuid.from_json(json)
# print the JSON string representation of the object
print NvdimmGuid.to_json()

# convert the object into a dict
nvdimm_guid_dict = nvdimm_guid_instance.to_dict()
# create an instance of NvdimmGuid from a dict
nvdimm_guid_form_dict = nvdimm_guid.from_dict(nvdimm_guid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



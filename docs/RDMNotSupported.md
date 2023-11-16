# RDMNotSupported

The virtual machine is configured with a Raw Disk Mapping.  This is not supported on the host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.rdm_not_supported import RDMNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of RDMNotSupported from a JSON string
rdm_not_supported_instance = RDMNotSupported.from_json(json)
# print the JSON string representation of the object
print RDMNotSupported.to_json()

# convert the object into a dict
rdm_not_supported_dict = rdm_not_supported_instance.to_dict()
# create an instance of RDMNotSupported from a dict
rdm_not_supported_form_dict = rdm_not_supported.from_dict(rdm_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



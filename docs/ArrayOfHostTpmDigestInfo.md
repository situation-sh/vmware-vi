# ArrayOfHostTpmDigestInfo

A boxed array of *HostTpmDigestInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostTpmDigestInfo]**](HostTpmDigestInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_tpm_digest_info import ArrayOfHostTpmDigestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostTpmDigestInfo from a JSON string
array_of_host_tpm_digest_info_instance = ArrayOfHostTpmDigestInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostTpmDigestInfo.to_json()

# convert the object into a dict
array_of_host_tpm_digest_info_dict = array_of_host_tpm_digest_info_instance.to_dict()
# create an instance of ArrayOfHostTpmDigestInfo from a dict
array_of_host_tpm_digest_info_form_dict = array_of_host_tpm_digest_info.from_dict(array_of_host_tpm_digest_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



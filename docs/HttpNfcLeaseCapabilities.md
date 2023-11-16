# HttpNfcLeaseCapabilities

Descriptor of the lease capabilities.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pull_mode_supported** | **bool** | True if overall this lease can be upgraded to pull mode and all hosts in this lease support pull mode.  Prerequisite before calling pullFromUrls.  ***Since:*** vSphere API 6.7  | 
**cors_supported** | **bool** | True if all hosts in the lease support HTTP CORS.  ***Since:*** vSphere API 6.7  | 

## Example

```python
from vmware_vi.models.http_nfc_lease_capabilities import HttpNfcLeaseCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of HttpNfcLeaseCapabilities from a JSON string
http_nfc_lease_capabilities_instance = HttpNfcLeaseCapabilities.from_json(json)
# print the JSON string representation of the object
print HttpNfcLeaseCapabilities.to_json()

# convert the object into a dict
http_nfc_lease_capabilities_dict = http_nfc_lease_capabilities_instance.to_dict()
# create an instance of HttpNfcLeaseCapabilities from a dict
http_nfc_lease_capabilities_form_dict = http_nfc_lease_capabilities.from_dict(http_nfc_lease_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



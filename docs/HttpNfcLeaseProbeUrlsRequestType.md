# HttpNfcLeaseProbeUrlsRequestType

The parameters of *HttpNfcLease.HttpNfcLeaseProbeUrls*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[HttpNfcLeaseSourceFile]**](HttpNfcLeaseSourceFile.md) | \\[in\\] List of remote source file descriptors There should be the same number of *HttpNfcLeaseSourceFile* as *HttpNfcLeaseDeviceUrl* provided by this lease.  ***Since:*** vSphere API 6.7  | [optional] 
**timeout** | **int** | \\[in\\] time in seconds for each url validation. Maximum timeout is 60.  | [optional] 

## Example

```python
from vmware_vi.models.http_nfc_lease_probe_urls_request_type import HttpNfcLeaseProbeUrlsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HttpNfcLeaseProbeUrlsRequestType from a JSON string
http_nfc_lease_probe_urls_request_type_instance = HttpNfcLeaseProbeUrlsRequestType.from_json(json)
# print the JSON string representation of the object
print HttpNfcLeaseProbeUrlsRequestType.to_json()

# convert the object into a dict
http_nfc_lease_probe_urls_request_type_dict = http_nfc_lease_probe_urls_request_type_instance.to_dict()
# create an instance of HttpNfcLeaseProbeUrlsRequestType from a dict
http_nfc_lease_probe_urls_request_type_form_dict = http_nfc_lease_probe_urls_request_type.from_dict(http_nfc_lease_probe_urls_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



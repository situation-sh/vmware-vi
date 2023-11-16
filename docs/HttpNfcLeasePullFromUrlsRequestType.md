# HttpNfcLeasePullFromUrlsRequestType

The parameters of *HttpNfcLease.HttpNfcLeasePullFromUrls_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[HttpNfcLeaseSourceFile]**](HttpNfcLeaseSourceFile.md) | \\[in\\] List of remote source file descriptors There should be the same number of *HttpNfcLeaseSourceFile* as *HttpNfcLeaseDeviceUrl* provided by this lease. Privilege VApp.PullFromUrls is required.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.http_nfc_lease_pull_from_urls_request_type import HttpNfcLeasePullFromUrlsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HttpNfcLeasePullFromUrlsRequestType from a JSON string
http_nfc_lease_pull_from_urls_request_type_instance = HttpNfcLeasePullFromUrlsRequestType.from_json(json)
# print the JSON string representation of the object
print HttpNfcLeasePullFromUrlsRequestType.to_json()

# convert the object into a dict
http_nfc_lease_pull_from_urls_request_type_dict = http_nfc_lease_pull_from_urls_request_type_instance.to_dict()
# create an instance of HttpNfcLeasePullFromUrlsRequestType from a dict
http_nfc_lease_pull_from_urls_request_type_form_dict = http_nfc_lease_pull_from_urls_request_type.from_dict(http_nfc_lease_pull_from_urls_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



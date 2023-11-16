# HttpNfcLeaseProbeResult

Descriptor of ProbeResult  ***Since:*** vSphere API 7.0.2.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_accessible** | **bool** | True if target host can access the web server.  ***Since:*** vSphere API 7.0.2.0  | 

## Example

```python
from vmware_vi.models.http_nfc_lease_probe_result import HttpNfcLeaseProbeResult

# TODO update the JSON string below
json = "{}"
# create an instance of HttpNfcLeaseProbeResult from a JSON string
http_nfc_lease_probe_result_instance = HttpNfcLeaseProbeResult.from_json(json)
# print the JSON string representation of the object
print HttpNfcLeaseProbeResult.to_json()

# convert the object into a dict
http_nfc_lease_probe_result_dict = http_nfc_lease_probe_result_instance.to_dict()
# create an instance of HttpNfcLeaseProbeResult from a dict
http_nfc_lease_probe_result_form_dict = http_nfc_lease_probe_result.from_dict(http_nfc_lease_probe_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



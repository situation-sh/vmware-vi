# HttpNfcLeaseHostInfo

Contains information about how to connect to a given host.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The host url will be of the form      https://hostname/nfc/ticket id/ The url can be used for both POST requests to a single device and for multi-POST requests to multiple devices. A single-POST URL is formed by adding the target id to the hostUrl:      https://hostname/nfc/ticket id/target id a multi-POST URL looks like      https://hostname/nfc/ticket id/multi?targets&#x3D;id1,id2,id3,...  ***Since:*** vSphere API 4.1  | 
**ssl_thumbprint** | **str** | SSL thumbprint for the host the URL refers to.  Empty if no SSL thumbprint is available or needed.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.http_nfc_lease_host_info import HttpNfcLeaseHostInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HttpNfcLeaseHostInfo from a JSON string
http_nfc_lease_host_info_instance = HttpNfcLeaseHostInfo.from_json(json)
# print the JSON string representation of the object
print HttpNfcLeaseHostInfo.to_json()

# convert the object into a dict
http_nfc_lease_host_info_dict = http_nfc_lease_host_info_instance.to_dict()
# create an instance of HttpNfcLeaseHostInfo from a dict
http_nfc_lease_host_info_form_dict = http_nfc_lease_host_info.from_dict(http_nfc_lease_host_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# HostNfcConnectionInfo

NfcConnectionInfo contains information about an NFC connection on the host.  ***Since:*** vSphere API 7.0.3.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**streaming_memory_consumed** | **int** | NFC streaming memory used by the connection in bytes.  ***Since:*** vSphere API 7.0.3.0  | [optional] 

## Example

```python
from vmware_vi.models.host_nfc_connection_info import HostNfcConnectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostNfcConnectionInfo from a JSON string
host_nfc_connection_info_instance = HostNfcConnectionInfo.from_json(json)
# print the JSON string representation of the object
print HostNfcConnectionInfo.to_json()

# convert the object into a dict
host_nfc_connection_info_dict = host_nfc_connection_info_instance.to_dict()
# create an instance of HostNfcConnectionInfo from a dict
host_nfc_connection_info_form_dict = host_nfc_connection_info.from_dict(host_nfc_connection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



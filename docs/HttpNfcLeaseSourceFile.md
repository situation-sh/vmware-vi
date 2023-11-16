# HttpNfcLeaseSourceFile

Descriptor of the remote source file used in pull scenario.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_device_id** | **str** | Target device id that will be used to store remote file.  Uniquely identifies host, vm and device. Given by this lease in *HttpNfcLeaseDeviceUrl.importKey*.  ***Since:*** vSphere API 6.7  | 
**url** | **str** | Full url of the source file, for example https://server/path/disk-1.vmdk.  Or url to OVA, in that case *HttpNfcLeaseSourceFile.memberName* should be specified.  ***Since:*** vSphere API 6.7  | 
**member_name** | **str** | Used only when OVA is specified in *HttpNfcLeaseSourceFile.url*.  Should contain file name to extract from OVA.  ***Since:*** vSphere API 6.7  | [optional] 
**create** | **bool** | True if PUT should be used for upload, otherwise POST.  Same as *OvfFileItem.create*  ***Since:*** vSphere API 6.7  | 
**ssl_thumbprint** | **str** | Esx has no CA database for checking arbitrary certificates.  Client should verify the server certificate and provide certificate thumbprint here.  ***Since:*** vSphere API 6.7  | [optional] 
**http_headers** | [**List[KeyValue]**](KeyValue.md) | For the case when remote server requires authentication or any other type of custom HTTP headers be provided with the request.  ***Since:*** vSphere API 6.7  | [optional] 
**size** | **int** | Size of the file, if known.  Otherwise it will be determined by a HEAD request. Not used for OVA members.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.http_nfc_lease_source_file import HttpNfcLeaseSourceFile

# TODO update the JSON string below
json = "{}"
# create an instance of HttpNfcLeaseSourceFile from a JSON string
http_nfc_lease_source_file_instance = HttpNfcLeaseSourceFile.from_json(json)
# print the JSON string representation of the object
print HttpNfcLeaseSourceFile.to_json()

# convert the object into a dict
http_nfc_lease_source_file_dict = http_nfc_lease_source_file_instance.to_dict()
# create an instance of HttpNfcLeaseSourceFile from a dict
http_nfc_lease_source_file_form_dict = http_nfc_lease_source_file.from_dict(http_nfc_lease_source_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



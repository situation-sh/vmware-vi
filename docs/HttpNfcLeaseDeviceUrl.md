# HttpNfcLeaseDeviceUrl

Provides a mapping from logical device IDs to upload/download URLs.  For export, a single device id is returned based on the object identifiers for the objects.  For import, two device ids are returned. One based on the object names used in the ImportSpec, and one based on the object identifiers for the created objects. This is immutable and would match the id if an ExportLease is latter created.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The immutable identifier for the device.  This is set for both import/export leases.  ***Since:*** vSphere API 4.0  | 
**import_key** | **str** | Identifies the device based on the names in an ImportSpec.  This is only set for import leases.  ***Since:*** vSphere API 4.0  | 
**url** | **str** |  | 
**ssl_thumbprint** | **str** | SSL thumbprint for the host the URL refers to.  Empty if no SSL thumbprint is available or needed.  ***Since:*** vSphere API 4.0  | 
**disk** | **bool** | Optional value to specify if the attached file is a disk in vmdk format.  ***Since:*** vSphere API 4.1  | [optional] 
**target_id** | **str** | Id for this target.  This only used for multi-POSTing, where a single HTTP POST is applied to multiple targets.  ***Since:*** vSphere API 4.1  | [optional] 
**datastore_key** | **str** | Key for the datastore this disk is on.  This is used to look up hosts which can be used to multi-POST disk contents, in the host map of the lease.  ***Since:*** vSphere API 4.1  | [optional] 
**file_size** | **int** | Specifies the size of the file backing for this device.  This property is only set for non-disk file backings.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.http_nfc_lease_device_url import HttpNfcLeaseDeviceUrl

# TODO update the JSON string below
json = "{}"
# create an instance of HttpNfcLeaseDeviceUrl from a JSON string
http_nfc_lease_device_url_instance = HttpNfcLeaseDeviceUrl.from_json(json)
# print the JSON string representation of the object
print HttpNfcLeaseDeviceUrl.to_json()

# convert the object into a dict
http_nfc_lease_device_url_dict = http_nfc_lease_device_url_instance.to_dict()
# create an instance of HttpNfcLeaseDeviceUrl from a dict
http_nfc_lease_device_url_form_dict = http_nfc_lease_device_url.from_dict(http_nfc_lease_device_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


